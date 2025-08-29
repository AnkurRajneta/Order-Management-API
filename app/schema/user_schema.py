from pydantic import BaseModel, EmailStr
from typing import Optional, List
from app.enums.enums import *
from app.schema.role_schema import RoleOut

class CreateUser(BaseModel):
    username:str
    email:  EmailStr
    password:str
    role_id:int

    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    username: Optional[str]
    email:Optional[EmailStr]
    password:Optional[str]
    role_id : Optional[int]
    
    class Config:
        from_attributes = True


class UserOut(BaseModel):
    id:int
    username:str
    email:EmailStr
    password:str
    role_id:int
    
    class Config:
        from_attributes = True

class UserCombinedOut(BaseModel):
    id:int
    username:str
    email:EmailStr
    password:str
    role_id:int
    role:RoleOut

    class Config:
        from_attributes = True
