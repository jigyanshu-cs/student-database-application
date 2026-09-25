from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base,engine
from app.routers import students,chatbot,auth
Base.metadata.create_all(bind=engine)
app=FastAPI(title='Student Database Application System',version='2.0.0',description='FastAPI + PostgreSQL + Gemini + LangGraph + ChromaDB')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.include_router(auth.router,prefix='/api/auth',tags=['Authentication'])
app.include_router(students.router,prefix='/api/students',tags=['Students'])
app.include_router(chatbot.router,prefix='/api/chatbot',tags=['AI Chatbot'])
@app.get('/')
def root(): return {'message':'Student Database Backend is running','docs':'/docs'}
@app.get('/health')
def health(): return {'status':'healthy'}
