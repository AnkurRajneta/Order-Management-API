import jwt
from datetime import datetime, timedelta
from app.config.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM


def create_jwt(data:dict, expires_delta:timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token Expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid Token")
