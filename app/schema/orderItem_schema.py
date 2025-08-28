from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateOrderItem(BaseModel):
    order_id:int
    product_id:int
    quantity:int
    price:int
    
    class Config:
        from_attributes = True

class UpdateOrderItem(BaseModel):
    order_id : Optional[int]
    product_id: Optional[int]
    quantity: Optional[int]
    price:Optional[int]

    class Config:
        from_attributes = True

class OutputOrderItem(BaseModel):
    id:int
    order_id:int
    product_id:int
    quantity:int
    price:int

    class Config:
        from_attributes = True