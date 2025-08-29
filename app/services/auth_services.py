from datetime import timedelta
from fastapi import HTTPException, status
from app.repository.user_repository import UserRepository
from app.schema.auth_schema import *
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils import utils
from app.enums.enums import Permission, UserRoleEnum 
    




ROLE_PERMISSIONS = {
    UserRoleEnum.ADMIN.value: [
        Permission.CREATE_USER_CONTROLLER.value,
        Permission.UPDATE_USER_BY_ID_CONTROLLER.value,
        Permission.DELETE_USER_BY_ID_CONTROLLER.value,
        Permission.CREATE_ROLE_CONTROLLER.value,
        Permission.CREATE_PRODUCT_CONTROLLER.value,
        Permission.UPDATE_PRODUCT_BY_ID_CONTROLLER.value,
        Permission.DELETE_PRODUCT_BY_ID_CONTROLLER.value,
        Permission.GET_ALL_ORDER_CONTROLLER.value,
        Permission.UPDATE_ORDER_BY_ID.value
    ],
    UserRoleEnum.MANAGER.value:[
        Permission.CREATE_PRODUCT_CONTROLLER.value,
        Permission.UPDATE_PRODUCT_BY_ID_CONTROLLER.value,
        Permission.GET_ALL_ORDER_CONTROLLER.value,
        Permission.UPDATE_ORDER_BY_ID.value
        
    ],
    UserRoleEnum.CUSTOMER.value:[
        Permission.GET_PRODUCT_ALL_CONTROLLER.value,
        Permission.CREATE_ORDER_CONTROLLER.value,
        Permission.GET_ORDER_BY_ID_CONTROLLER.value

    ]
    
}
class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def auth_service(self, email: EmailStr, password: str):
        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Please provide email and password"
            )
        user = await self.repo.get_user_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if not password == user.password:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Password is incorrect"
            )
        
        user_role = user.role.name if hasattr(user.role, 'name') else user.role
        permissions = ROLE_PERMISSIONS.get(user_role, [])


       

        token_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            "role_id": user.role_id,
            "role": user_role,
            "permissions": permissions
            
        }

        token = utils.create_jwt(data=token_data, expires_delta=timedelta(30))

        return {
            "status_code": 200,
            "error": None,
            "message": "Logged in successfully",
            "data": {
                "access_token": token,
                "user": {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    "role_id": user.role_id,
                    "role": user_role,
                    "permissions":permissions
                   
                }
            }
        }

    async def register_auth(self, payload: RegisterSchema):
        new_user = await self.repo.create_user_repository(payload)
        return new_user