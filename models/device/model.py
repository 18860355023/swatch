from models.orm_base import BaseModel
from sqlalchemy import Column, Boolean, Integer, String, Text, DateTime, CheckConstraint, DateTime, Float, UniqueConstraint
from datetime import datetime

# 设备基本信息
class DeviceInfo(BaseModel):
    __tablename__ = 'device_info'
    __table_args__ = {'comment': '设备基本信息'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, comment="设备名称")
    device_id = Column(String, unique=True, comment="设备唯一标识")
    device_status = Column(Boolean, comment="设备状态（是否在线）")
    iccid = Column(String, comment="ICCID（SIM卡号）")
    phone_number = Column(String, comment="绑定的手机号码")
    battery_level = Column(Float, comment="电池电量（%）")
    signal_strength = Column(Float, comment="信号强度")
    version = Column(String, comment="设备版本号")