from app.services.role_service import RoleService
from fastapi import APIRouter, HTTPException, Depends
from app.config.database import get_db
from app.schema.role_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


router = APIRouter()

@router.post("")
async def create_role_controller(payload:CreateRole, db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.create_role_service(payload)
    return result

@router.get("", response_model=List[RoleOut])
async def get_all_role_controller(db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.get_all_role_service()
    return result

@router.get("/id/{id}", response_model=RoleOut)
async def get_role_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.get_role_by_id_service(id)
    return result

@router.put("/update/{id}")
async def update_role_by_controller(id:int, payload:UpdateRole, db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.update_role_by_id_service(id, payload)
    return result

@router.delete("/{id}")
async def delete_role_by_id_controller(id:int, db:AsyncSession = Depends(get_db)):
    service = RoleService(db)
    result = await service.delete_role_by_id_service(id)
    return {
        "message": "role deleted successfully"
    }