from app.services.product_service import ProductService
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.schema.products_schema import *
from typing import List
from app.utils.permission import require_permission
from app.enums.enums import Permission

router = APIRouter()

@router.post("")
async def create_product_controller(payload:CreateProduct, db:AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.CREATE_PRODUCT_CONTROLLER))):
    service = ProductService(db)
    return await service.create_product_service(payload)


@router.get("", response_model=List[OutputProduct])
async def get_product_all_controller(db:AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.GET_PRODUCT_ALL_CONTROLLER))):
    service = ProductService(db)
    return await service.get_all_product_service()

@router.get("/id/{id}", response_model = OutputProduct)
async def get_product_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = ProductService(db)
    return await service.get_product_by_id_service(id)

@router.put("/update/{id}")
async def update_product_by_id_controller(id:int, payload:UpdateProduct, db:AsyncSession = Depends(get_db), permission_check:None = Depends(require_permission(Permission.UPDATE_PRODUCT_BY_ID_CONTROLLER))):
    service = ProductService(db)
    return await service.update_product_by_id_service(id, payload)

@router.delete("/{id}")
async def delete_product_by_id_controller(id:int, db: AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.DELETE_PRODUCT_BY_ID_CONTROLLER))):
    service = ProductService(db)
    return await service.delete_product_by_id_service(id)