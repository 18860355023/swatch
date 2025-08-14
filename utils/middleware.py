import logging
import jwt
import json
from fastapi import FastAPI, Depends, HTTPException, Header, Request
from fastapi import status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from settings import *
from utils.use_redis import login_redis
from fastapi import  Request
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, JSONResponse, StreamingResponse
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Callable
from models.orm_base import SessionLocal,get_db,APICallLog


def getAuthRes(authorization):
    if not authorization:
        return False
    try:
        token_key = jwt.decode(authorization, key=None, options={'verify_signature': False}).get("login_user_key") # type: ignore
        print(f"token_key {token_key}")
        res = login_redis.get('login_tokens:' + token_key).decode()
        # redis 缓存的是java序列化对象， 把关键字剔除，否则无法json解析。
        res = res.replace('Set', '')
        res = res.replace('L,', ',')
        dec = json.loads(res)
        user_status = True if dec["user"]["status"] == '0' else False
        return user_status
    except Exception as e:
        print(f"getAuthRes failed : {str(e)}")
        return False
    

class MyMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        method = request.method
        path = request.url.path
        client_ip = request.client.host  # type: ignore
        user_agent = request.headers.get("User-Agent", "")

        # 读取请求体
        request_body = await request.body()
        request_body_str = request_body.decode() if request_body else ""

        # 捕获响应
        response = await call_next(request)

        # 如果是 StreamingResponse，则读取并记录响应体
        response_body = b""
        async def response_iterator():
            nonlocal response_body
            async for chunk in response.body_iterator:
                response_body += chunk
                yield chunk

        # 重新构造响应
        new_response = StreamingResponse(
            response_iterator(),
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )

        response_body_str = response_body.decode() if response_body else ""

        # 记录 API 调用日志
        db: Session = SessionLocal()
        try:
            log_entry = APICallLog(
                method=method,
                path=path,
                client_ip=client_ip,
                status_code=response.status_code,
                request_body=request_body_str,
                response_body=response_body_str,
                user_agent=user_agent
            )
            db.add(log_entry)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Logging Error: {e}")
        finally:
            db.close()

        # 返回新的 StreamingResponse
        return new_response



white_list = [
    "/docs",
    "/api/openapi.json",
    "/openapi.json",
]


class permssionsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_path = request.get("path")
        # 公共接口
        if request_path in white_list:
            response = await call_next(request)
            return response

        token = request.headers["Authorization"].split("Bearer ")[1]
        print(token)
        perm = getAuthRes(token)
        if not perm:
            return JSONResponse(content={
                "msg": f"请求访问：{request_path}，认证失败，无法访问系统资源",
                "code": 401
            }, status_code=200)
        response = await call_next(request)
        return response



# 验证 Token 的函数
def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
        return payload
    except jwt.JWTError: # type: ignore
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

# Token 认证的依赖注入函数
def get_current_user(token: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> str:
    return verify_token(token.credentials)["sub"]

# 自定义 Token 认证中间件
async def auth_middleware(request, call_next):
    # try:
    #     token = request.headers["Authorization"].split("Bearer ")[1]
    #     # return token
    #     # verify_token(token)
    # except (KeyError, IndexError):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing or invalid")

    response = await call_next(request)
    return response