from app.repository.order_repository import OrderRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.order_schema import CreateOrder, UpdateOrder


class OrderService:
    def __init__(self, db:AsyncSession):
        self.repo = OrderRepository(db)

    async def create_order_service(self, payload:CreateOrder):
        return await self.repo.create_order_repository(payload)
    
    async def get_all_order_service(self):
        return await self.repo.get_all_order_repository()
    
    async def get_order_by_id_service(self, id:int):
        return await self.repo.get_order_by_id_repository(id)
    
    async def update_order_by_id_service(self,id:int,payload: UpdateOrder):
        return await self.repo.update_order_by_id_repository(id, payload)
    
    async def delete_order_by_id_service(self, id:int):
        return await self.repo.delete_order_by_id_repository(id)