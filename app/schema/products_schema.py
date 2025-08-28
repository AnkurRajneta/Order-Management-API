from pydantic import BaseModel, EmailStr
from typing import Optional 
from app.enums.enums import Stock, Category

class CreateProduct(BaseModel):
    name: str
    category: Category
    price: int
    stock: Stock

    class Config:
        from_attributes = True

class UpdateProduct(BaseModel):
    name : Optional[str]
    category:Optional[Category]
    price:Optional[int]
    stock:Optional[Stock]

    class Config:
        from_attributes = True


class OutputProduct(BaseModel):
    id: int
    name:str
    category: Category
    price:int
    stock: Stock

    class Config:
        from_attributes = True
