import json
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List
from models.orm_base import get_db 
from models.command.model import Command, CommandInfo
from schemas.command_sch import CommandInfoCreate, CommandInfoUpdate, CommandInfoResponse
from utils.use_redis import redis_client
from settings import MANUFACTURER


cmd_router = APIRouter()


# # 创建 Command
# @cmd_router.post("/commands/", response_model=CommandResponse)
# async def create_command(command: CommandCreate, db: Session = Depends(get_db)):
#     db_command = Command(**command.dict())
#     db.add(db_command)
#     db.commit()
#     db.refresh(db_command)
#     return db_command

# # 查询所有 Command
# @cmd_router.get("/commands/", response_model=List[CommandResponse])
# async def read_commands(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     commands = db.query(Command).offset(skip).limit(limit).all()
#     return commands

# # 查询单个 Command
# @cmd_router.get("/commands/{command_id}", response_model=CommandResponse)
# async def read_command(command_id: int, db: Session = Depends(get_db)):
#     command = db.query(Command).filter(Command.id == command_id).first()
#     if not command:
#         raise HTTPException(status_code=404, detail="Command not found")
#     return command

# # 更新 Command
# @cmd_router.put("/commands/{command_id}", response_model=CommandResponse)
# async def update_command(command_id: int, command_update: CommandUpdate, db: Session = Depends(get_db)):
#     db_command = db.query(Command).filter(Command.id == command_id).first()
#     if not db_command:
#         raise HTTPException(status_code=404, detail="Command not found")

#     for key, value in command_update.dict(exclude_unset=True).items():
#         setattr(db_command, key, value)

#     db.commit()
#     db.refresh(db_command)
#     return db_command

# # 删除 Command
# @cmd_router.delete("/commands/{command_id}")
# async def delete_command(command_id: int, db: Session = Depends(get_db)):
#     db_command = db.query(Command).filter(Command.id == command_id).first()
#     if not db_command:
#         raise HTTPException(status_code=404, detail="Command not found")

#     db.delete(db_command)
#     db.commit()
#     return {"message": "Command deleted successfully"}



# CommandInfo 的 CRUD 操作
# 新增指令记录
@cmd_router.post("/command_info/", summary="新增指令记录")
async def create_command(command: CommandInfoCreate, db: Session = Depends(get_db)):
    try:
        cname = command.command_name
        prs = command.command_params
        cct = f"{cname},{prs}" if prs else f"{cname}"
        cmd_str = f"{MANUFACTURER}*{command.device_id}*{format(len(cct), '04x')}*{cct}"
        redis_client.set(f"command:{command.device_id}:{cname}", cmd_str)
        db_command = CommandInfo(**command.dict())
        db.add(db_command)
        db.commit()
        return {"code": 200, "message": "success"}
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail="command_params must be a valid JSON string")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# 查询所有指令记录
@cmd_router.get("/command_info/", summary="查询所有指令记录")
async def get_all_commands(db: Session = Depends(get_db)):
    command_list = db.query(CommandInfo).all()
    return {"code": 200, "message": "success", "data": command_list}

# 查询单个指令记录
@cmd_router.get("/command_info/{device_id}", summary="查询指定设备的所有指令")
async def get_command(device_id: str, db: Session = Depends(get_db)):
    command_list = db.query(CommandInfo).filter(CommandInfo.device_id == device_id, CommandInfo.command_status == '1').all()
    if not command_list:
        raise HTTPException(status_code=404, detail="Command not found")
    return {"code": 200, "message": "success", "data": command_list}

# # 更新指令记录
# @cmd_router.put("/command_info/{command_id}", response_model=CommandInfoResponse)
# async def update_command(command_id: int, command_update: CommandInfoUpdate, db: Session = Depends(get_db)):
#     db_command = db.query(CommandInfo).filter(CommandInfo.id == command_id).first()
#     if not db_command:
#         raise HTTPException(status_code=404, detail="Command not found")

#     for key, value in command_update.dict(exclude_unset=True).items():
#         setattr(db_command, key, value)

#     db.commit()
#     db.refresh(db_command)
#     return db_command

# # 删除指令记录
# @cmd_router.delete("/command_info/{command_id}")
# async def delete_command(command_id: int, db: Session = Depends(get_db)):
#     db_command = db.query(CommandInfo).filter(CommandInfo.id == command_id).first()
#     if not db_command:
#         raise HTTPException(status_code=404, detail="Command not found")

#     db.delete(db_command)
#     db.commit()
#     return {"message": "Command deleted successfully"}
