from app.repository.product_repository import ProductRepository
from app.schema.products_schema import CreateProduct, UpdateProduct
from sqlalchemy.ext.asyncio import AsyncSession


class ProductService:
    def __init__(self, db:AsyncSession):
        self.repo = ProductRepository(db)

    async def create_product_service(self,payload:CreateProduct):
        return await self.repo.create_product_repository(payload)
    
    async def get_all_product_service(self):
        return await self.repo.get_all_product_repository()
    
    async def get_product_by_id_service(self, id:int):
        return await self.repo.get_product_by_id_repository(id)
    
    async def update_product_by_id_service(self, id:int, payload:UpdateProduct):
        return await self.repo.update_product_by_id_repository(id, payload)
    
    async def delete_product_by_id_service(self, id:int):
        return await self.repo.delete_product_by_id_repository(id)

