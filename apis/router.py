from fastapi import APIRouter

from apis.device.view import device_router
from apis.log.view import log_router
from apis.command.view import cmd_router
from apis.health.view import health_router
from apis.localtion.view import localtion_router
from apis.weather.view import weather_router
from apis.alarm.view import alarm_router


api_router = APIRouter()

# 根路由
api_router.include_router(device_router, prefix="/device_manage",tags=["设备管理"])
api_router.include_router(log_router, prefix="/log_manage",tags=["日志管理"])
api_router.include_router(cmd_router, prefix="/cmd_manage",tags=["指令管理"])
api_router.include_router(health_router, prefix="/health_manage",tags=["健康管理"])
api_router.include_router(localtion_router, prefix="/localtion_manage",tags=["位置信息"])
api_router.include_router(alarm_router, prefix="/alarm_manage",tags=["报警管理"])
api_router.include_router(weather_router, prefix="/weather_manage",tags=["天气信息"])
