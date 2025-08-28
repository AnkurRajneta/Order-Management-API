from pydantic import BaseModel, EmailStr
from typing import Optional
from app.enums.enums import Status
from ..schema.user_schema import UserOut

class CreateOrder(BaseModel):
    customer_id :int
    total_amount : int
    status: Status

    class Config:
        from_attributes = True

class UpdateOrder(BaseModel):
    customer_id: Optional[int]
    total_amount:Optional[int]
    status:Optional[Status]

    class Config:
        from_attributes = True

class OrderOut(BaseModel):
    id:int
    customer_id:int
    total_amount: int
    status:Status
    user:UserOut