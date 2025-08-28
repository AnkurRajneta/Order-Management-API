from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.enums.enums import TableName, Status
from app.config.database import Base

class OrderModel(Base):
    __tablename__ = TableName.ORDERS
    id = Column(Integer,primary_key= True)
    customer_id = Column(Integer, ForeignKey("user.id"))
    total_amount = Column(Integer, nullable= False)
    status = Column(Enum(Status), nullable= False)

    user = relationship("UserModel", back_populates="orders")
    orderitems = relationship("OrderItemModel", back_populates="orders")