# routers/weather.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List
from models.orm_base import get_db
from models.weather.model import WeatherInfo
from schemas.weather_sch import WeatherInfoCreate

weather_router = APIRouter()

# 创建天气信息
@weather_router.post("/weather/", summary="创建天气信息")
async def create_weather(weather: WeatherInfoCreate, db: Session = Depends(get_db)):
    db_weather = WeatherInfo(**weather.dict())
    db.add(db_weather)
    db.commit()
    return {"code": 200, "message": "success"}

# 获取所有天气信息
@weather_router.get("/weather/", summary="获取所有天气信息")
async def read_weather(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weather_list = db.query(WeatherInfo).offset(skip).limit(limit).all()
    return {"code": 200, "message": "success", "data": weather_list}

# 获取单个天气信息
@weather_router.get("/weather/{device_id}", summary="获取单个天气信息")
async def read_weather(device_id: str, db: Session = Depends(get_db)):
    weather = db.query(WeatherInfo).filter(WeatherInfo.device_id == device_id).order_by(desc(WeatherInfo.createdTime)).first()
    if weather is None:
        raise HTTPException(status_code=404, detail="Weather not found")
    return {"code": 200, "message": "success", "data": weather}


# 删除天气信息
@weather_router.delete("/weather/{weather_id}", summary="删除天气信息")
async def delete_weather(weather_id: int, db: Session = Depends(get_db)):
    db_weather = db.query(WeatherInfo).filter(WeatherInfo.id == weather_id).first()
    if db_weather is None:
        raise HTTPException(status_code=404, detail="Weather not found")
    db.delete(db_weather)
    db.commit()
    return db_weather
