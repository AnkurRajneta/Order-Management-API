from app.repository.user_repository import UserRepository
from app.schema.user_schema import CreateUser, UpdateUser
from sqlalchemy.ext.asyncio import AsyncSession

class UserService:
    def __init__(self, db:AsyncSession):
        self.repo = UserRepository(db)

    async def create_user_service(self, payload:CreateUser):
        return await self.repo.create_user_repository(payload)
    
    async def get_all_user_service(self):
        return await self.repo.get_all_user_repository()
    
    async def get_user_by_id_service(self, id:int):
        return await self.repo.get_user_by_id_repository(id)
    
    async def update_user_by_id_service(self, id:int, payload:UpdateUser):
        return await self.repo.update_user_by_id_repository(id, payload)
    
    async def delete_user_by_id_service(self, id:int):
        return await self.repo.delete_user_by_id_repository(id)