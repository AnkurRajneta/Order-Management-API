from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.enums.enums import TableName, UserRoleEnum


class RoleModel(Base):
    __tablename__ = TableName.ROLE
    id = Column(Integer, primary_key= True)
    name = Column(Enum(UserRoleEnum), nullable = False)

    permission = relationship("PermissionModel", back_populates="role")
    user = relationship("UserModel", back_populates="role")