from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 接口调用日志 - 创建模型
class APICallLogCreate(BaseModel):
    method: str
    path: str
    client_ip: Optional[str] = None
    status_code: int
    request_body: Optional[str] = None
    response_body: Optional[str] = None
    user_agent: Optional[str] = None

# 接口调用日志 - 响应模型
class APICallLogResponse(BaseModel):
    id: int
    method: str
    path: str
    client_ip: Optional[str] = None
    status_code: int
    request_body: Optional[str] = None
    response_body: Optional[str] = None
    user_agent: Optional[str] = None
    # created_at: datetime

    class Config:
        orm_mode = True
