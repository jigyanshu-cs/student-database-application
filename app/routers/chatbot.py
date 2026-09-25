from fastapi import APIRouter,Depends,HTTPException
from app.schemas import ChatRequest,ChatResponse
from app.auth import get_current_user
from app.ai.graph import ask_chatbot
router=APIRouter()
@router.post('/chat',response_model=ChatResponse)
def chat(x:ChatRequest,u=Depends(get_current_user)):
    try:return ChatResponse(response=ask_chatbot(x.message))
    except Exception as e: raise HTTPException(500,f'AI service error: {e}')
