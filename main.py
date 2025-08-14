import os
import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from settings import *
from apis.router import api_router
from models.orm_base import Base, engine
from utils.middleware import LogMiddleware

# 初始化app实例
app = FastAPI(title=APP_NAME, openapi_url=f"{API_PREFIX}/openapi.json")

# 设置CORS站点
app.add_middleware(
    CORSMiddleware,
    # 允许跨域的源列表
    allow_origins=["*"],
    # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)
# app.add_middleware(LogMiddleware)
# app.add_middleware(permssionsMiddleware)

# 路由注册
app.include_router(api_router, prefix=API_PREFIX)


@app.get("/")
async def ping():
    return {"code":0,"msg":"ok"}

if __name__ == '__main__':
    # print(count_routes(app))
    # 将model创建为表 checkfirst=True 默认也是 True，即如果数据库存在则不再创建
    Base.metadata.create_all(engine, checkfirst=True)
    # 本地测试将数据库切换为本地sqlite
    # 写入测试数据
    # add_test_data()
    # 清空数据库
    uvicorn.run(app="main:app", host='0.0.0.0', port=6003)