import json
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List
from models.orm_base import get_db
from models.health.model import HealthData, HealthWeeklyReport, TempData, BooldData, OxygenData, HeartData, StepData
from schemas.health_sch import *
from utils.use_redis import redis_client

health_router = APIRouter()


# --------------------- 健康管理 API ---------------------

# 新增健康数据
@health_router.post("/health_data/", response_model=HealthDataResponse)
async def create_health_data(data: HealthDataCreate, db: Session = Depends(get_db)):
    db_data = HealthData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

# 查询所有健康数据
@health_router.get("/health_data/", response_model=List[HealthDataResponse])
async def get_all_health_data(db: Session = Depends(get_db)):
    return db.query(HealthData).all()

# 查询单条健康数据
@health_router.get("/health_data/{device_id}", summary="查询最新健康数据")
async def get_health_data(device_id: str, db: Session = Depends(get_db)):
    steps = redis_client.get(f"device:{device_id}:steps")
    weight = redis_client.get(f"device:{device_id}:weight")
    height = redis_client.get(f"device:{device_id}:height")
    temp = redis_client.get(f"device:{device_id}:temp")
    blood = redis_client.get(f"device:{device_id}:blood")
    oxygen = redis_client.get(f"device:{device_id}:oxygen")
    heart_rate = redis_client.get(f"device:{device_id}:heart_rate")
    health_dict = {
        "steps": json.loads(steps) if steps else "-",
        "weight": json.loads(weight) if weight else "-",
        "height": json.loads(height) if height else "-",
        "temp": json.loads(temp) if temp else "-",
        "blood": json.loads(blood) if blood else "-",
        "oxygen": json.loads(oxygen) if oxygen else "-",
        "heart_rate": json.loads(heart_rate) if heart_rate else "-"
    }
    return {"code": 200, "message": "success", "data": health_dict}

# 更新健康数据
@health_router.put("/health_data/{data_id}", response_model=HealthDataResponse)
async def update_health_data(data_id: int, update_data: HealthDataUpdate, db: Session = Depends(get_db)):
    db_data = db.query(HealthData).filter(HealthData.id == data_id).first()
    if not db_data:
        raise HTTPException(status_code=404, detail="Health data not found")

    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_data, key, value)

    db.commit()
    db.refresh(db_data)
    return db_data

# 删除健康数据
@health_router.delete("/health_data/{data_id}")
async def delete_health_data(data_id: int, db: Session = Depends(get_db)):
    db_data = db.query(HealthData).filter(HealthData.id == data_id).first()
    if not db_data:
        raise HTTPException(status_code=404, detail="Health data not found")

    db.delete(db_data)
    db.commit()
    return {"message": "Health data deleted successfully"}


# --------------------- 健康周报 API ---------------------

# 新增健康周报
@health_router.post("/health_weekly_report/", response_model=HealthWeeklyReportResponse)
async def create_health_weekly_report(report: HealthWeeklyReportCreate, db: Session = Depends(get_db)):
    db_report = HealthWeeklyReport(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return {"code": 200, "message": "success"}

# 查询所有健康周报
@health_router.get("/health_weekly_report/", response_model=List[HealthWeeklyReportResponse])
async def get_all_health_weekly_reports(db: Session = Depends(get_db)):
    return db.query(HealthWeeklyReport).all()

# 查询单条健康周报
@health_router.get("/health_weekly_report/{report_id}", response_model=HealthWeeklyReportResponse)
async def get_health_weekly_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(HealthWeeklyReport).filter(HealthWeeklyReport.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Weekly report not found")
    return report

# 更新健康周报
@health_router.put("/health_weekly_report/{report_id}", response_model=HealthWeeklyReportResponse)
async def update_health_weekly_report(report_id: int, update_data: HealthWeeklyReportUpdate, db: Session = Depends(get_db)):
    db_report = db.query(HealthWeeklyReport).filter(HealthWeeklyReport.id == report_id).first()
    if not db_report:
        raise HTTPException(status_code=404, detail="Weekly report not found")

    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_report, key, value)

    db.commit()
    db.refresh(db_report)
    return db_report

# 删除健康周报
@health_router.delete("/health_weekly_report/{report_id}")
async def delete_health_weekly_report(report_id: int, db: Session = Depends(get_db)):
    db_report = db.query(HealthWeeklyReport).filter(HealthWeeklyReport.id == report_id).first()
    if not db_report:
        raise HTTPException(status_code=404, detail="Weekly report not found")

    db.delete(db_report)
    db.commit()
    return {"message": "Weekly report deleted successfully"}



# 新增体温数据
@health_router.post("/temp_data/", summary="新增体温数据")
async def create_temp_data(temp_data: TempDataCreate, db: Session = Depends(get_db)):
    try:
        db_temp_data = TempData(device_id=temp_data.device_id, temp=temp_data.temp)
        db.add(db_temp_data)
        db.commit()
        db.refresh(db_temp_data)
        return {"code": 200, "message": "success"}
    except Exception:
        import traceback
        traceback.print_exc()

# 新增血压数据
@health_router.post("/boold_data/", summary="新增血压数据")
async def create_boold_data(boold_data: BooldDataCreate, db: Session = Depends(get_db)):
    db_boold_data = BooldData(device_id=boold_data.device_id, boold=boold_data.boold)
    db.add(db_boold_data)
    db.commit()
    db.refresh(db_boold_data)
    return {"code": 200, "message": "success"}

# 新增血氧数据
@health_router.post("/oxygen_data/", summary="新增血氧数据")
async def create_oxygen_data(oxygen_data: OxygenDataCreate, db: Session = Depends(get_db)):
    db_oxygen_data = OxygenData(device_id=oxygen_data.device_id, oxygen=oxygen_data.oxygen)
    db.add(db_oxygen_data)
    db.commit()
    db.refresh(db_oxygen_data)
    return {"code": 200, "message": "success"}

# 新增心率数据
@health_router.post("/heart_data/", summary="新增心率数据")
async def create_heart_data(heart_data: HeartDataCreate, db: Session = Depends(get_db)):
    db_heart_data = HeartData(device_id=heart_data.device_id, heart_rate=heart_data.heart_rate)
    db.add(db_heart_data)
    db.commit()
    db.refresh(db_heart_data)
    return {"code": 200, "message": "success"}

# 新增步数数据
@health_router.post("/step_data/", summary="新增步数数据")
async def create_step_data(step_data: StepDataCreate, db: Session = Depends(get_db)):
    db_step_data = StepData(device_id=step_data.device_id, steps=step_data.steps)
    db.add(db_step_data)
    db.commit()
    db.refresh(db_step_data)
    return {"code": 200, "message": "success"}
