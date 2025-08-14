from models.orm_base import BaseModel
from sqlalchemy import Column, Integer, String


# 报警信息
class AlarmInfo(BaseModel):
    __tablename__ = 'alarm_info'
    __table_args__ = {'comment': '报警信息'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    alarm_name = Column(String, comment="报警名称")
    alarm_status = Column(String, comment="报警状态（触发/未触发）")