from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from models.orm_base import BaseModel
from datetime import datetime


# 天气信息
class WeatherInfo(BaseModel):
    __tablename__ = 'weather_info'
    __table_args__ = {'comment': '天气信息'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    weather_description = Column(String, comment="天气描述（如：晴、阴、雨等）")
    weather_code = Column(Integer, comment="天气编号（根据气象API给出的编号）")
    current_temperature = Column(Float, comment="当前温度（°C）")
    min_temperature = Column(Float, comment="最低温度（°C）")
    max_temperature = Column(Float, comment="最高温度（°C）")
    city_name = Column(String, comment="城市名称")
