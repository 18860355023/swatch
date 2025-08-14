from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, JSON
from models.orm_base import BaseModel


# 体温
class TempData(BaseModel):
    __tablename__ = 'temp_data'
    __table_args__ = {'comment': '体温'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    temp = Column(Float, comment="体温")


# 血压
class BooldData(BaseModel):
    __tablename__ = 'boold_data'
    __table_args__ = {'comment': '血压'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    boold = Column(String, comment="血压(舒张压/收缩压)")


# 血氧
class OxygenData(BaseModel):
    __tablename__ = 'oxygen_data'
    __table_args__ = {'comment': '血氧'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    oxygen = Column(Float, comment="血氧")


# 心率
class HeartData(BaseModel):
    __tablename__ = 'heart_data'
    __table_args__ = {'comment': '心率'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    heart_rate = Column(Integer, comment="心率")


# 步数
class StepData(BaseModel):
    __tablename__ = 'step_data'
    __table_args__ = {'comment': '步数'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    steps = Column(Integer, comment="步数")


# 健康管理
class HealthData(BaseModel):
    __tablename__ = 'health_data'
    __table_args__ = {'comment': '健康管理'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, comment="设备ID")
    sleep = Column(Float, comment="睡眠时长（小时）")
    weight = Column(Float, comment="体重（kg）")
    height = Column(Float, comment="身高（cm）")


# 健康周报
class HealthWeeklyReport(BaseModel):
    __tablename__ = 'health_weekly_report'
    __table_args__ = {'comment': '健康周报'}
    
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, comment="设备ID")
    week_start_date = Column(DateTime, comment="周开始日期（周一）")
    week_end_date = Column(DateTime, comment="周结束日期（周日）")
    average_steps = Column(Float, comment="平均步数")
    steps_statistics = Column(JSON, comment="步数统计")
    steps_analysis = Column(String, comment="步数分析")
    average_sleep = Column(Float, comment="平均睡眠时长（小时）")
    sleep_statistics = Column(JSON, comment="睡眠统计")
    sleep_analysis = Column(String, comment="睡眠分析")
    average_weight = Column(Float, comment="平均体重（kg）")
    weight_statistics = Column(JSON, comment="体重统计")
    weight_analysis = Column(String, comment="体重分析")
    average_heart_rate = Column(Float, comment="平均心率（次/分钟）")
    heart_rate_statistics = Column(JSON, comment="心率统计")
    heart_rate_analysis = Column(String, comment="心率分析")
    average_blood_oxygen = Column(Float, comment="平均血氧饱和度")
    blood_oxygen_statistics = Column(JSON, comment="血氧饱和度统计")
    blood_oxygen_analysis = Column(String, comment="血氧饱和度分析")
