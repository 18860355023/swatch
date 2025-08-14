# routers/location.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.orm_base import get_db
from models.localtion.model import LocationInfo
from schemas.localtion_sch import LocationInfoCreate

localtion_router = APIRouter()

# 创建位置信息
@localtion_router.post("/locations/")
async def create_location(location: LocationInfoCreate, db: Session = Depends(get_db)):
    db_location = LocationInfo(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return {"code": 200, "message": "success"}

# 获取所有位置信息
@localtion_router.get("/locations/")
async def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = db.query(LocationInfo).offset(skip).limit(limit).all()
    return {"code": 200, "message": "success", "data": locations}

# 获取单个位置信息
@localtion_router.get("/locations/{location_id}")
async def read_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(LocationInfo).filter(LocationInfo.id == location_id).first()
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return {"code": 200, "message": "success", "data": location}

# 更新位置信息
@localtion_router.put("/locations/{location_id}")
async def update_location(location_id: int, location: LocationInfoCreate, db: Session = Depends(get_db)):
    db_location = db.query(LocationInfo).filter(LocationInfo.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    for key, value in location.dict().items():
        setattr(db_location, key, value)
    db.commit()
    db.refresh(db_location)
    return {"code": 200, "message": "success"}

# 删除位置信息
@localtion_router.delete("/locations/{location_id}")
async def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = db.query(LocationInfo).filter(LocationInfo.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(db_location)
    db.commit()
    return {"code": 200, "message": "success"}
