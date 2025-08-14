from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

# 健康管理 Pydantic 模型
class HealthDataCreate(BaseModel):
    device_id: str
    sleep: Optional[float] = None
    weight: Optional[float] = None
    height: Optional[float] = None

class HealthDataUpdate(BaseModel):
    steps: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None

class HealthDataResponse(HealthDataCreate):
    id: int

    class Config:
        orm_mode = True


# 健康周报 Pydantic 模型
class HealthWeeklyReportCreate(BaseModel):
    device_id: int
    week_start_date: datetime
    week_end_date: datetime
    average_steps: Optional[float] = None
    steps_statistics: Optional[Dict] = None
    steps_analysis: Optional[str] = None
    average_sleep: Optional[float] = None
    sleep_statistics: Optional[Dict] = None
    sleep_analysis: Optional[str] = None
    average_weight: Optional[float] = None
    weight_statistics: Optional[Dict] = None
    weight_analysis: Optional[str] = None
    average_heart_rate: Optional[float] = None
    heart_rate_statistics: Optional[Dict] = None
    heart_rate_analysis: Optional[str] = None
    average_blood_oxygen: Optional[float] = None
    blood_oxygen_statistics: Optional[Dict] = None
    blood_oxygen_analysis: Optional[str] = None

class HealthWeeklyReportUpdate(BaseModel):
    average_steps: Optional[float] = None
    steps_statistics: Optional[Dict] = None
    steps_analysis: Optional[str] = None
    average_sleep: Optional[float] = None
    sleep_statistics: Optional[Dict] = None
    sleep_analysis: Optional[str] = None
    average_weight: Optional[float] = None
    weight_statistics: Optional[Dict] = None
    weight_analysis: Optional[str] = None
    average_heart_rate: Optional[float] = None
    heart_rate_statistics: Optional[Dict] = None
    heart_rate_analysis: Optional[str] = None
    average_blood_oxygen: Optional[float] = None
    blood_oxygen_statistics: Optional[Dict] = None
    blood_oxygen_analysis: Optional[str] = None

class HealthWeeklyReportResponse(HealthWeeklyReportCreate):
    id: int

    class Config:
        orm_mode = True


# 体温数据模型
class TempDataCreate(BaseModel):
    device_id: str
    temp: float

# 血压数据模型
class BooldDataCreate(BaseModel):
    device_id: str
    boold: str

# 血氧数据模型
class OxygenDataCreate(BaseModel):
    device_id: str
    oxygen: float

# 心率数据模型
class HeartDataCreate(BaseModel):
    device_id: str
    heart_rate: int

# 步数数据模型
class StepDataCreate(BaseModel):
    device_id: str
    steps: int

