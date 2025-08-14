from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.orm_base import get_db
from models.orm_base import APICallLog  # SQLAlchemy模型
from schemas.log_sch import APICallLogCreate, APICallLogResponse

log_router = APIRouter()

# 创建接口调用日志
@log_router.post("/api_call_logs/", response_model=APICallLogResponse)
async def create_api_call_log(log: APICallLogCreate, db: Session = Depends(get_db)):
    db_log = APICallLog(**log.dict(exclude_unset=True))
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# 获取所有接口调用日志
@log_router.get("/api_call_logs/", response_model=List[APICallLogResponse])
async def read_api_call_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = db.query(APICallLog).offset(skip).limit(limit).all()
    return logs

# 获取单个接口调用日志
@log_router.get("/api_call_logs/{log_id}", response_model=APICallLogResponse)
async def read_api_call_log(log_id: int, db: Session = Depends(get_db)):
    log = db.query(APICallLog).filter(APICallLog.id == log_id).first()
    if log is None:
        raise HTTPException(status_code=404, detail="API call log not found")
    return log

# 更新接口调用日志
@log_router.put("/api_call_logs/{log_id}", response_model=APICallLogResponse)
async def update_api_call_log(log_id: int, log: APICallLogCreate, db: Session = Depends(get_db)):
    db_log = db.query(APICallLog).filter(APICallLog.id == log_id).first()
    if db_log is None:
        raise HTTPException(status_code=404, detail="API call log not found")
    for key, value in log.dict(exclude_unset=True).items():
        setattr(db_log, key, value)
    db.commit()
    db.refresh(db_log)
    return db_log

# 删除接口调用日志
@log_router.delete("/api_call_logs/{log_id}", response_model=APICallLogResponse)
async def delete_api_call_log(log_id: int, db: Session = Depends(get_db)):
    db_log = db.query(APICallLog).filter(APICallLog.id == log_id).first()
    if db_log is None:
        raise HTTPException(status_code=404, detail="API call log not found")
    db.delete(db_log)
    db.commit()
    return db_log
