# schemas/location.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 用于创建和更新位置信息
class LocationInfoCreate(BaseModel):
    device_id: str
    latitude: float
    longitude: float
    address: Optional[str] = None
    direction: Optional[float] = None
    altitude: Optional[float] = None
    speed: Optional[float] = None
    satellite_count: Optional[int] = None
    base_station_count: Optional[int] = None
    base_station_info: Optional[str] = None
    wifi_count: Optional[int] = None


