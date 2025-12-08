from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserRequest(BaseModel):
    name: str
    email: EmailStr
    role_id: int
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role_id: int
    created_at: datetime
    
    class Config:
        orm_mode = True