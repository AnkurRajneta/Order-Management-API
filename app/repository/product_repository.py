from app.models.products_model import ProductModel
from app.schema.products_schema import CreateProduct, UpdateProduct
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.enums.enums import Category, Stock
from fastapi import HTTPException,status

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product_repository(self, payload:CreateProduct):
        new_product = ProductModel(name = payload.name,
                                   category = payload.category,
                                   price = payload.price,
                                   stock = payload.stock)
        
        self.db.add(new_product)
        await self.db.commit()
        await self.db.refresh(new_product)
        return new_product
    

    async def get_all_product_repository(self):
        stmt = select(ProductModel)
        result = await self.db.execute(stmt)
        return result.scalars().all()
    

    async def get_product_by_id_repository(self, id:int):
        stmt = select(ProductModel).where(ProductModel.id == id)
        result = await self.db.execute(stmt)
        return result.scalars().first()
    

    async def update_product_by_id_repository(self, id:int, payload:UpdateProduct):
        stmt = select(ProductModel).where(ProductModel.id ==id)
        result = await self.db.execute(stmt)
        updated_result = result.scalars().first()

        if not updated_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found" )
        
        updated_result.name = payload.name
        updated_result.category = payload.category
        updated_result.price = payload.price
        updated_result.stock = payload.stock

        await self.db.commit()
        await self.db.refresh(updated_result)
        return updated_result
    

    async def delete_product_by_id_repository(self, id:int):
        stmt = select(ProductModel).where(ProductModel.id == id)
        result = await self.db.execute(stmt)
        deleted_result = result.scalars().first()

        if not deleted_result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Product not found")
        
        await self.db.delete(deleted_result)
        await self.db.commit()
        return {"message": "Product deleted successfully"}
