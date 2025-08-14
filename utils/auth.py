from datetime import datetime, timedelta
from typing import Any, Union, Optional
from jose import jwt
from fastapi import Header

ALGORITHM = "HS256"

config = {
    # 加密密钥
    "SECRET_KEY" : "amxc901e1-em1wlqkd",
    # 过期时间
    "ACCESS_TOKEN_EXPIRE_MINUTES": 60*24
}


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    # 生成token
    :param subject: 保存到token的值
    :param expires_delta: 过期时间
    :return:
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config["ACCESS_TOKEN_EXPIRE_MINUTES"]
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config["SECRET_KEY"], algorithm=ALGORITHM)
    return encoded_jwt


def check_jwt_token(
     token: Optional[str] = Header(..., alias="X-token")
) -> Union[str, Any]:
    """
    解析验证 headers中为X-token的值
    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            config.SECRET_KEY, algorithms=[ALGORITHM]
        )
        return payload
    except (jwt.JWTError, jwt.ExpiredSignatureError, AttributeError):
        # 抛出自定义异常， 然后捕获统一响应
        # raise custom_exc.TokenAuthError(err_desc="access token fail")
        print("超时")
        pass
