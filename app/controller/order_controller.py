from app.services.order_service import OrderService
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.schema.order_schema import *
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.utils.permission import require_permission
from app.enums.enums import Permission


router = APIRouter()

@router.post("")
async def create_order_controller(payload:CreateOrder, db:AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.CREATE_ORDER_CONTROLLER))):
    service = OrderService(db)
    result = await service.create_order_service(payload)
    return result


@router.get("")
async def get_all_order_controller(db:AsyncSession = Depends(get_db), permission_check:None = Depends(require_permission(Permission.GET_ALL_ORDER_CONTROLLER))):
    service = OrderService(db)
    result = await service.get_all_order_service()
    return result

@router.get("/id/{id}")
async def get_order_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = OrderService(db)
    result = await service.get_order_by_id_service(id)
    return result

@router.put("/update/{id}")
async def update_order_by_id(id:int, payload:UpdateOrder, db:AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.UPDATE_ORDER_BY_ID))):
    service = OrderService(db)
    result = await service.update_order_by_id_service(id, payload)
    return result

@router.delete("/delete/{id}")
async def delete_order_by_id(id:int, db : AsyncSession = Depends(get_db)):
    service = OrderService(db)
    result = await service.delete_order_by_id_service(id)
    return {
        "message":"Order deleted successfully"
    }