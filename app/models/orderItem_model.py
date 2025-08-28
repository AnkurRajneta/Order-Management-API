from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.config.database import Base
from app.enums.enums import TableName
from sqlalchemy.orm import relationship

class OrderItemModel(Base):
    __tablename__ = TableName.ORDERITEMS
    id = Column(Integer, primary_key= True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, nullable= False)
    price = Column(Integer, nullable= False)

    orders = relationship("OrderModel",back_populates="orderitems")

    product = relationship("ProductModel", back_populates="orderitems")