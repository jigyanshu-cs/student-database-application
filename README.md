# Student Database Application System – Submission Edition

Full-stack internship project using **FastAPI, PostgreSQL, JWT authentication, Gemini, LangGraph, ChromaDB, React and Docker**.

## Requirements covered
- Modular backend architecture
- Student CRUD APIs
- Swagger/OpenAPI at `/docs`
- PostgreSQL persistence
- JWT login/authentication
- Gemini API integration
- LangGraph agent with student database tools
- ChromaDB vector database
- React frontend
- Docker Compose deployment
- Render deployment configuration

## Quick start
1. Copy `.env.example` to `.env`.
2. Add your Gemini API key.
3. Change the JWT secret and admin password.
4. Run `docker compose up --build`.

Frontend: `http://localhost:3000`  
Backend: `http://localhost:8000`  
Swagger: `http://localhost:8000/docs`

Demo credentials come from `.env` (`ADMIN_EMAIL` / `ADMIN_PASSWORD`). Change them before submission.

## Architecture
```text
React Frontend -> FastAPI -> JWT Auth -> PostgreSQL
                         |
                         -> LangGraph -> Gemini
                                      -> DB tools -> PostgreSQL
                                      -> ChromaDB project knowledge
```

## Vector database research
ChromaDB was selected for this internship demonstration because it is lightweight, persistent and easy to run locally. Alternatives considered: PostgreSQL + pgvector, Qdrant, Pinecone and Weaviate. A production choice should consider scale, filtering, cost and hosting.

## Deployment
`Dockerfile`, `docker-compose.yml` and `render.yaml` are included. Set secrets through deployment environment variables; never commit `.env` or API keys.

## GitHub checklist
Upload source, README, report, Docker files and screenshots. Do not upload secrets, database files or `chroma_data`.

## Viva topics
Be ready to explain FastAPI routing, Pydantic validation, SQLAlchemy ORM, PostgreSQL, JWT, LangGraph state/tool calling, Gemini, vector databases, ChromaDB, Docker and environment variables.
