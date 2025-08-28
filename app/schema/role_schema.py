from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.enums.enums import UserRoleEnum


class CreateRole(BaseModel):
    name :UserRoleEnum

    class Config:
        from_attributes = True


class UpdateRole(BaseModel):
    name: Optional[UserRoleEnum]

    class Config:
        from_attributes = True


class RoleOut(BaseModel):
    id: int
    name: UserRoleEnum

    class Config:
        from_attributes = True
