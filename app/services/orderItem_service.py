from app.repository.orderItem_repository import OrderItemRepository
from fastapi import APIRouter, Depends, HTTPException
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.orderItem_schema import CreateOrderItem, UpdateOrderItem

class OrderItemService:
    def __init__(self, db:AsyncSession):
        self.repo = OrderItemRepository(db)

    async def create_orderItem_service(self, payload:CreateOrderItem):
        return await self.repo.create_orderItem_repository(payload)
    
    async def get_all_orderItem_service(self):
        return await self.repo.get_all_orderItem_repository()
    
    async def get_orderItem_by_id_service(self,id:int):
        return await self.repo.get_orderItem_by_id_repository(id)
    
    async def update_orderItem_by_id_service(self, id:int, payload:UpdateOrderItem):
        return await self.repo.update_orderItem_by_id_repository(id, payload)
    
    async def delete_orderItem_by_id_service(self, id:int):
        return await self.repo.delete_orderItem_by_id_repository(id)
