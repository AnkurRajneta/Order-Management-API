from app.models.role_model import RoleModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.role_schema import CreateRole, UpdateRole
from fastapi import HTTPException,status


class RoleRepository:
    def __init__(self, db:AsyncSession):
        self.db = db

    async def create_role_repository(self,payload:CreateRole):
        new_role = RoleModel(name = payload.name)

        self.db.add(new_role)
        await self.db.commit()
        await self.db.refresh(new_role)
        return new_role
    
    async def get_all_role_repository(self):
        stmt = select(RoleModel)
        result = await self.db.execute(stmt)
        return result.scalars().all()
    

    async def get_role_by_id_repository(self, id:int):
        stmt = select(RoleModel).where(RoleModel.id == id)
        result = await self.db.execute(stmt)
        return result.scalars().first()
    
    async def update_role_by_id_repository(self, id:int, payload:UpdateRole):
        stmt = select(RoleModel).where(RoleModel.id == id)
        result = await self.db.execute(stmt)
        updated_result = result.scalars().first()
        
        if not updated_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role Not found")
        
        updated_result.name = payload.name
        await self.db.commit()
        await self.db.refresh(updated_result)
        return updated_result
    
    async def delete_role_by_id_repository(self, id:int):
        stmt = select(RoleModel).where(RoleModel.id == id)
        result = await self.db.execute(stmt)
        deleted_result = result.scalars().first()

        if not deleted_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Role not found")
        
        await self.db.delete(deleted_result)
        await self.db.commit()
        return {"message":"Deleted successfully"}




