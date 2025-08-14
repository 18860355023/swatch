# schemas/alarm.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 创建和更新时使用的模型
class AlarmInfoCreate(BaseModel):
    device_id: str
    alarm_type: str
    alarm_level: int
    alarm_time: datetime
    status: Optional[str] = "active"
    description: Optional[str] = None

# 响应时使用的模型
class AlarmInfoResponse(BaseModel):
    id: int
    device_id: str
    alarm_type: str
    alarm_level: int
    alarm_time: datetime
    status: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True  # 支持 SQLAlchemy 转换为 Pydantic
