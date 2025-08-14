from pydantic import BaseModel,root_validator
from datetime import datetime
from typing import List, Optional



# Pydantic 模型（用于 API 响应）
class DeviceInfoResponse(BaseModel):
    id: int
    device_name: str
    device_id: str
    device_status: bool
    iccid: Optional[str] = None
    phone_number: Optional[str] = None
    battery_level: Optional[float] = None
    signal_strength: Optional[float] = None
    version: Optional[str] = None

    class Config:
        orm_mode = True

# Pydantic 模型（用于创建 & 更新）
class DeviceInfoCreate(BaseModel):
    device_name: str
    device_id: str
    device_status: bool = True
    iccid: Optional[str] = None
    phone_number: Optional[str] = None
    battery_level: Optional[float] = None
    signal_strength: Optional[float] = None
    version: Optional[str] = None
