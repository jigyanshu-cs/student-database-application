from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.ai.graph import ask_chatbot

router = APIRouter()


@router.post('/chat', response_model=ChatResponse)
def chat(x: ChatRequest):
    try:
        return ChatResponse(response=ask_chatbot(x.message))
    except Exception as e:
        raise HTTPException(500, f'AI service error: {e}')