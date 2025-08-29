from app.services.user_service import UserService
from app.schema.user_schema import *
from fastapi import APIRouter,HTTPException, Depends, status
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.utils.permission import require_permission


router = APIRouter()


@router.post("")
async def create_user_controller(payload:CreateUser, db:AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.CREATE_USER_CONTROLLER))):
    service = UserService(db)
    result = await service.create_user_service(payload)
    return result

@router.get("/email/check/{email}")
async def get_user_by_email_controller(email:EmailStr, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result = await service.get_user_by_email(email)
    return result



@router.get("")
async def get_all_user_controller(db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result = await service.get_all_user_service()
    return result

@router.get("/id/{id}")
async def get_user_by_id_controller(id:int,db:AsyncSession = Depends(get_db)):
    service = UserService(db)
    result = await service.get_user_by_id_service(id)
    return result

@router.put("/update/{id}")
async def update_user_by_id_controller(id:int, payload:UpdateUser, db:AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.UPDATE_USER_BY_ID_CONTROLLER))):
    service = UserService(db)
    result = await service.update_user_by_id_service(id, payload)
    return result

@router.delete("/delete/{id}")
async def delete_user_by_id_controller(id:int, db:AsyncSession = Depends(get_db),permission_check:None = Depends(require_permission(Permission.DELETE_USER_BY_ID_CONTROLLER))):
    service = UserService(db)
    result = await service.delete_user_by_id_service(id)
    return {"message":"User deleted successfully"}