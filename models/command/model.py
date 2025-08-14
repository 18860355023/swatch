from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime,JSON
from models.orm_base import BaseModel


# 指令信息
class Command(BaseModel):
    __tablename__ = 'command'
    __table_args__ = {'comment': '指令信息'}
    
    id = Column(Integer, primary_key=True, index=True)
    command_name = Column(String, comment="指令名称")
    command_params = Column(JSON, comment="指令参数")


# 指令记录
class CommandInfo(BaseModel):
    __tablename__ = 'command_info'
    __table_args__ = {'comment': '指令记录'}
    
    id = Column(Integer, primary_key=True, index=True)
    command_name = Column(String, comment="指令名称")
    device_id = Column(String, comment="设备ID")
    command_params = Column(String, nullable=True, comment="指令参数")
    command_status = Column(String, default="1", comment="指令状态（1-待下发，2-下发成功，3-下发失败，4-已取消）")



# # 指令生命周期
# class CommandLifeCycle(BaseModel):
#     __tablename__ = 'command_life_cycle'
#     __table_args__ = {'comment': '指令生命周期'}
    
#     id = Column(Integer, primary_key=True, index=True)
#     command_id = Column(Integer, comment="指令ID")
#     command_status = Column(String, comment="指令状态")
#     issued_time = Column(DateTime, comment="指令变更时间")