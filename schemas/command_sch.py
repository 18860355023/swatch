from pydantic import BaseModel
from typing import Optional


# Command 创建模型
class CommandCreate(BaseModel):
    command_name: str
    command_type: str
    description: Optional[str] = None

# Command 更新模型
class CommandUpdate(BaseModel):
    command_name: Optional[str] = None
    command_type: Optional[str] = None
    description: Optional[str] = None

# Command 响应模型
class CommandResponse(BaseModel):
    id: int
    command_name: str
    command_type: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

# CommandInfo 创建模型
class CommandInfoCreate(BaseModel):
    command_name: str
    device_id: str
    command_params: Optional[str] = None
    command_status: Optional[int] = '1'

# CommandInfo 更新模型
class CommandInfoUpdate(BaseModel):
    status: Optional[str] = None
    result: Optional[str] = None

# CommandInfo 响应模型
class CommandInfoResponse(BaseModel):
    id: int
    command_id: int
    status: str
    # executed_at: datetime
    result: Optional[str] = None
    # created_at: datetime

    class Config:
        orm_mode = True

