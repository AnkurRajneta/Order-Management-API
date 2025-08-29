from fastapi import Depends, HTTPException, status
from app.enums.enums import Permission
from app.middleware.auth_middleware import get_current_user

def require_permission(permission:Permission):
    async def dependency(current_user = Depends(get_current_user)):
        user_permissions = current_user.get("permissions",[])
        print(user_permissions)
        print("Checking Permission:",permission.value, "in", user_permissions)
        if permission.value not in user_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action."
            )
        
    return dependency
