# schemas/weather.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 用于创建和更新天气信息
class WeatherInfoCreate(BaseModel):
    device_id: str
    weather_description: str
    city_name: str
    current_temperature: float
    weather_code: Optional[float] = None
    min_temperature: Optional[float] = None
    max_temperature: Optional[str] = None

