from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from models.orm_base import BaseModel
from datetime import datetime


# 位置信息
class LocationInfo(BaseModel):
    __tablename__ = 'location_info'
    __table_args__ = {'comment': '位置信息'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    longitude = Column(Float, comment="经度")
    latitude = Column(Float, comment="纬度")
    address = Column(String, comment="详细地址")
    direction = Column(Float, comment="方向（角度）")
    altitude = Column(Float, comment="海拔高度")
    speed = Column(Float, comment="速度（米/秒）")
    satellite_count = Column(Integer, comment="当前卫星数量")
    base_station_count = Column(Integer, comment="基站数量")
    base_station_info = Column(String, comment="基站信息")
    wifi_count = Column(Integer, comment="Wi-Fi数量")
