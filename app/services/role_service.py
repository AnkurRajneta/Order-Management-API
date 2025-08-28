from app.repository.role_repository import RoleRepository
from app.schema.role_schema import CreateRole, UpdateRole
from sqlalchemy.ext.asyncio import AsyncSession


class RoleService:
    def __init__(self, db:AsyncSession):
        self.repo = RoleRepository(db)

    async def create_role_service(self, payload:CreateRole):
        return await self.repo.create_role_repository(payload)
    
    async def get_all_role_service(self):
        return await self.repo.get_all_role_repository()
    
    async def get_role_by_id_service(self, id:int):
        return await self.repo.get_role_by_id_repository(id)
    
    async def update_role_by_id_service(self, id:int, payload:UpdateRole):
        return await self.repo.update_role_by_id_repository(id, payload)
    
    async def delete_role_by_id_service(self, id:int):
        return await self.repo.delete_role_by_id_repository(id)