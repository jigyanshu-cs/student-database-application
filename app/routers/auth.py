from fastapi import APIRouter,HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import authenticate,create_access_token
from app.schemas import LoginRequest,TokenResponse
router=APIRouter()
@router.post('/login',response_model=TokenResponse)
def login(form:OAuth2PasswordRequestForm=Depends()):
    user=authenticate(form.username,form.password)
    if not user: raise HTTPException(401,'Incorrect email or password')
    return {'access_token':create_access_token({'sub':user['email'],'role':user['role']}),'token_type':'bearer'}
@router.post('/login-json',response_model=TokenResponse)
def login_json(data:LoginRequest):
    user=authenticate(data.email,data.password)
    if not user: raise HTTPException(401,'Incorrect email or password')
    return {'access_token':create_access_token({'sub':user['email'],'role':user['role']}),'token_type':'bearer'}
