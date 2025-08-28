from app.services.orderItem_service import OrderItemService
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schema.orderItem_schema import *
from app.config.database import get_db


router = APIRouter()

@router.post("")
async def create_orderItem_controller(payload:CreateOrderItem, db:AsyncSession = Depends(get_db)):
    service = OrderItemService(db)
    result = await service.create_orderItem_service(payload)
    return result

@router.get("", response_model=List[OutputOrderItem])
async def get_orderItem_controller(db:AsyncSession = Depends(get_db)):
    service = OrderItemService(db)
    result = await service.get_all_orderItem_service()
    return result


@router.get("/id/{id}", response_model=OutputOrderItem)
async def get_orderItem_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = OrderItemService(db)
    result = await service.get_orderItem_by_id_service(id)
    return result

@router.put("/update/{id}")
async def update_orderItem_by_id_controller(id:int, payload:UpdateOrderItem, db:AsyncSession = Depends(get_db)):
    service = OrderItemService(db)
    result = await service.update_orderItem_by_id_service(id, payload)
    return result

@router.delete("/{id}")
async def delete_orderItem_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = OrderItemService(db)
    result = await service.delete_orderItem_by_id_service(id)
    return {
        "message" : "OrderItem deleted Successfully"
    }

