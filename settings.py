import urllib

from pydantic import AnyHttpUrl
from typing import List
import os

ENV = os.environ.get("fast_env", "DEV")  # 本次启动环境
APP_NAME = "smartwatch-backend"
# api前缀
API_PREFIX = "/api"
# jwt密钥,建议随机生成一个
SECRET_KEY = "ShsUP9qIP2Xui2GpXRY6y74v2JSVS0Q2YOXJ22VjwkI"
# token过期时间
ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60
# 跨域白名单
# BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:8080"]

# POSTGRESQL数据库配置
PG_DB_USER = "watchtest"
PG_DBPASSWORD = "Qwerty123!"
PG_DB_HOST = "8.148.22.77"
PG_DB_PORT = 5432
PG_DB_NAME = "smartwatch"

# RABBITMQ配置
RABBITMQ_HOST = "8.148.22.77"
RABBITMQ_PORT = 5672
RABBITMQ_USER = "guest"
RABBITMQ_PASSWORD = "guest"

# REDIS配置
REDIS_HOST = '8.148.22.77'
REDIS_PORT = 6379
REDIS_PASSWORD = 'shxx&2025testUP!'

# 启动端口配置
PORT = 6003
# 是否热加载
RELOAD = False

# jwt 密钥
JWT_KEY = 'HtkNQxU9bobqoyvkX6Ke7munEY'


# 厂商名称
MANUFACTURER = "DW"



