import json
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List
from models.orm_base import get_db
from models.device.model import DeviceInfo
from schemas.device_sch import DeviceInfoCreate, DeviceInfoResponse
from utils.use_redis import redis_client


device_router = APIRouter()

# 创建设备
@device_router.post("/devices/", summary="创建设备")
async def create_device(device: DeviceInfoCreate, db: Session = Depends(get_db)):
    # print(device.dict())
    device_id = device.device_id
    try:
        devcie_obj = db.query(DeviceInfo).filter(DeviceInfo.device_id == device_id).first()
        if devcie_obj:
            for key, value in device.dict().items():
                setattr(devcie_obj, key, value)
            db.commit()
            db.refresh(devcie_obj)
            return {"code": 200, "message": "success"}
        
        db_device = DeviceInfo(**device.dict())
        db.add(db_device)
        db.commit()
        db.refresh(db_device)
        return {"code": 200, "message": "success"}
    except Exception as e:
        return {"code": 400, "message": f"err:{str(e)}"}

# 获取所有设备
@device_router.get("/devices/", response_model=List[DeviceInfoResponse], summary="获取所有设备")
async def read_devices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    devices = db.query(DeviceInfo).offset(skip).limit(limit).all()
    return {"code": 200, "message": "success", "data": devices}

# 获取单个设备(id)
@device_router.get("/devices/{id}", response_model=DeviceInfoResponse, summary="获取单个设备(主键id)")
async def read_device(id: int, db: Session = Depends(get_db)):
    device = db.query(DeviceInfo).filter(DeviceInfo.id == id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return {"code": 200, "message": "success", "data": device}

# 获取单个设备(设备编号)
@device_router.get("/devices/{device_id}", response_model=DeviceInfoResponse, summary="获取单个设备(设备编号)")
async def read_device(device_id: str, db: Session = Depends(get_db)):
    device = db.query(DeviceInfo).filter(DeviceInfo.device_id == device_id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return {"code": 200, "message": "success", "data": device}

# 更新设备(设备编号)
@device_router.put("/devices/{device_id}", response_model=DeviceInfoResponse, summary="更新设备(设备编号)")
async def update_device(device_id: str, device: DeviceInfoCreate, db: Session = Depends(get_db)):
    db_device = db.query(DeviceInfo).filter(DeviceInfo.device_id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    for key, value in device.dict().items():
        setattr(db_device, key, value)
    db.commit()
    db.refresh(db_device)
    return {"code": 200, "message": "success", "data": db_device}

# 删除设备(设备编号)
@device_router.delete("/devices/{device_id}", response_model=DeviceInfoResponse, summary="删除设备(设备编号)")
async def delete_device(device_id: str, db: Session = Depends(get_db)):
    db_device = db.query(DeviceInfo).filter(DeviceInfo.device_id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(db_device)
    db.commit()
    return {"code": 200, "message": "success", "data": db_device}
