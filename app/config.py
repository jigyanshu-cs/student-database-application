import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL=os.getenv('DATABASE_URL','sqlite:///./students.db')
GEMINI_API_KEY=os.getenv('GEMINI_API_KEY','')
GEMINI_MODEL=os.getenv('GEMINI_MODEL','gemini-2.5-flash')
CHROMA_PATH=os.getenv('CHROMA_PATH','./chroma_data')
