from app.models import OrderItemModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.orderItem_schema import CreateOrderItem, UpdateOrderItem
from sqlalchemy import select
from fastapi import HTTPException, status
from sqlalchemy.orm import selectinload

class OrderItemRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_orderItem_repository(self, payload:CreateOrderItem):
        new_orderItem = OrderItemModel(order_id = payload.order_id,
                                       product_id = payload.product_id,
                                       quantity = payload.quantity,
                                       price = payload.price)
        
        self.db.add(new_orderItem)
        await self.db.commit()
        await self.db.refresh(new_orderItem)
        return new_orderItem
    

    async def get_all_orderItem_repository(self):
        stmt = select(OrderItemModel)
        result =await self.db.execute(stmt)
        return  result.scalars().all()
    
    async def get_orderItem_by_id_repository(self, id:int):
        stmt = select(OrderItemModel).where(OrderItemModel.id == id)
        result = await self.db.execute(stmt)
        return result.scalars().first()
    

    async def update_orderItem_by_id_repository(self, id:int, payload:UpdateOrderItem):
        stmt = select(OrderItemModel).where(OrderItemModel.id ==id)
        result = await self.db.execute(stmt)
        updated_result = result.scalars().first()

        if not updated_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderItem not found")
        
        updated_result.order_id = payload.order_id
        updated_result.product_id = payload.product_id
        updated_result.quantity = payload.quantity
        updated_result.price = payload.price

        await self.db.commit()
        await self.db.refresh(updated_result)
        return updated_result
    
    async def delete_orderItem_by_id_repository(self, id:int):
        stmt = select(OrderItemModel).where(OrderItemModel.id == id)
        result = await self.db.execute(stmt)
        deleted_result = result.scalars().first()

        if not deleted_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderItem not found")
        
        await self.db.delete(deleted_result)
        await self.db.commit()
        return {
            "message":"OrderItem deleted successful"
        }
