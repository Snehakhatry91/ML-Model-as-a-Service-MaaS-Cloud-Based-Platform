from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY="CHANGE_THIS_SECRET_KEY"
ALGORITHM="HS256"
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def create_token(data:dict):
    data=data.copy()
    data["exp"]=datetime.utcnow()+timedelta(hours=5)
    return jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
