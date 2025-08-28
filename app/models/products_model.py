from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.enums.enums import TableName, Stock, Category


class ProductModel(Base):
    __tablename__ = TableName.PRODUCT

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    category = Column(Enum(Category), nullable= False)
    price = Column(Integer, nullable= False)
    stock = Column(Enum(Stock), nullable= False)

    orderitems = relationship("OrderItemModel", back_populates="product")