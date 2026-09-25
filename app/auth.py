import os
from datetime import datetime,timedelta,timezone
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY=os.getenv('JWT_SECRET_KEY','change-this-secret')
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/api/auth/login')
def authenticate(email,password):
    if email==os.getenv('ADMIN_EMAIL','admin@example.com') and password==os.getenv('ADMIN_PASSWORD','ChangeMe123!'):
        return {'email':email,'role':'admin'}
    return None
def create_access_token(data):
    p=data.copy(); p['exp']=datetime.now(timezone.utc)+timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES','60')))
    return jwt.encode(p,SECRET_KEY,algorithm='HS256')
def get_current_user(token:str=Depends(oauth2_scheme)):
    err=HTTPException(status_code=401,detail='Invalid or expired token',headers={'WWW-Authenticate':'Bearer'})
    try:
        p=jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
        if not p.get('sub'): raise err
        return {'email':p['sub'],'role':p.get('role','user')}
    except JWTError: raise err
