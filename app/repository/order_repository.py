from app.models.order_model import OrderModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.order_schema import CreateOrder, UpdateOrder
from sqlalchemy import select
from fastapi import HTTPException, status
from sqlalchemy.orm import selectinload


class OrderRepository:
    def __init__(self, db:AsyncSession):
        self.db = db

    async def create_order_repository(self, payload:CreateOrder):
        new_order = OrderModel(customer_id = payload.customer_id,
                               total_amount = payload.total_amount,
                                status = payload.status )
        
        self.db.add(new_order)
        await self.db.commit()
        await self.db.refresh(new_order)
        return new_order
    

    async def get_all_order_repository(self):
        stmt = select(OrderModel).options(selectinload(OrderModel.user))
        result =await self.db.execute(stmt)
        return result.scalars().all()
    
    async def get_order_by_id_repository(self, id:int):
        stmt = select(OrderModel).where(OrderModel.id == id)
        result = await self.db.execute(stmt)
        return result.scalars().first()
    

    async def update_order_by_id_repository(self, id:int, payload:UpdateOrder):
        stmt = select(OrderModel).where(OrderModel.id ==id)
        result = await self.db.execute(stmt)
        updated_result =  result.scalars().first()

        if not updated_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Order not found")
        
        updated_result.customer_id = payload.customer_id
        updated_result.total_amount = payload.total_amount
        updated_result.status = payload.status

        await self.db.commit()
        await self.db.refresh(updated_result)
        return updated_result
    

    async def delete_order_by_id_repository(self, id:int):
        stmt = select(OrderModel).where(OrderModel.id == id)
        result = await self.db.execute(stmt)
        deleted_result = result.scalars().first()

        if not deleted_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
        
        await self.db.delete(deleted_result)
        await self.db.commit()
        return {
            "message": "Order successfully deleted"
        }