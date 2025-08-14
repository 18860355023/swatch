# routers/alarm.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.orm_base import get_db
from models.alarm.model import AlarmInfo
from schemas.alarm_sch import AlarmInfoCreate, AlarmInfoResponse

alarm_router = APIRouter()

# # 创建报警信息
# @alarm_router.post("/alarms/", response_model=AlarmInfoResponse)
# async def create_alarm(alarm: AlarmInfoCreate, db: Session = Depends(get_db)):
#     db_alarm = AlarmInfo(**alarm.dict())
#     db.add(db_alarm)
#     db.commit()
#     db.refresh(db_alarm)
#     return db_alarm

# # 获取所有报警信息
# @alarm_router.get("/alarms/", response_model=List[AlarmInfoResponse])
# async def read_alarms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     alarms = db.query(AlarmInfo).offset(skip).limit(limit).all()
#     return alarms

# # 获取单个报警信息
# @alarm_router.get("/alarms/{alarm_id}", response_model=AlarmInfoResponse)
# async def read_alarm(alarm_id: int, db: Session = Depends(get_db)):
#     alarm = db.query(AlarmInfo).filter(AlarmInfo.id == alarm_id).first()
#     if alarm is None:
#         raise HTTPException(status_code=404, detail="Alarm not found")
#     return alarm

# # 更新报警信息
# @alarm_router.put("/alarms/{alarm_id}", response_model=AlarmInfoResponse)
# async def update_alarm(alarm_id: int, alarm: AlarmInfoCreate, db: Session = Depends(get_db)):
#     db_alarm = db.query(AlarmInfo).filter(AlarmInfo.id == alarm_id).first()
#     if db_alarm is None:
#         raise HTTPException(status_code=404, detail="Alarm not found")
#     for key, value in alarm.dict().items():
#         setattr(db_alarm, key, value)
#     db.commit()
#     db.refresh(db_alarm)
#     return db_alarm

# # 删除报警信息
# @alarm_router.delete("/alarms/{alarm_id}", response_model=AlarmInfoResponse)
# async def delete_alarm(alarm_id: int, db: Session = Depends(get_db)):
#     db_alarm = db.query(AlarmInfo).filter(AlarmInfo.id == alarm_id).first()
#     if db_alarm is None:
#         raise HTTPException(status_code=404, detail="Alarm not found")
#     db.delete(db_alarm)
#     db.commit()
#     return db_alarm
