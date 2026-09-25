from pydantic import BaseModel,EmailStr,Field
class StudentBase(BaseModel):
    name:str=Field(...,min_length=2,max_length=100); email:EmailStr; course:str=Field(...,min_length=2,max_length=100)
    year:int=Field(...,ge=1,le=6); cgpa:float|None=Field(None,ge=0,le=10); phone:str|None=Field(None,max_length=20)
class StudentCreate(StudentBase): pass
class StudentUpdate(BaseModel):
    name:str|None=None; email:EmailStr|None=None; course:str|None=None; year:int|None=Field(None,ge=1,le=6); cgpa:float|None=Field(None,ge=0,le=10); phone:str|None=None
class StudentResponse(StudentBase):
    id:int
    class Config: from_attributes=True
class ChatRequest(BaseModel): message:str=Field(...,min_length=1,max_length=2000)
class ChatResponse(BaseModel): response:str
class LoginRequest(BaseModel): email:EmailStr; password:str
class TokenResponse(BaseModel): access_token:str; token_type:str
