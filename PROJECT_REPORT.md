# Internship Project Report – Student Database Application System

## Abstract
This project implements a modular backend for managing student records and interacting with the database through a natural-language AI chatbot. FastAPI provides REST APIs and automatic Swagger documentation. SQLAlchemy provides database access. Gemini provides natural-language generation, while LangGraph orchestrates the chatbot workflow and database tools. ChromaDB is included as the vector database for semantic project-knowledge retrieval.

## Objectives
1. Build a modular backend.
2. Implement student CRUD operations.
3. Provide documented FastAPI APIs.
4. Integrate Gemini.
5. Build a LangGraph chatbot.
6. Allow the chatbot to interact with student records.
7. Research and use a vector database.
8. Prepare the service for deployment.

## Technologies
Python, FastAPI, SQLAlchemy, SQLite, Pydantic, Gemini API, LangGraph, ChromaDB, Uvicorn, GitHub.

## Modules
- `app/main.py`: application entry point.
- `app/models.py`: database model.
- `app/schemas.py`: API validation schemas.
- `app/crud.py`: database operations.
- `app/routers/students.py`: CRUD API routes.
- `app/routers/chatbot.py`: chatbot API route.
- `app/ai/tools.py`: LangGraph database tools.
- `app/ai/graph.py`: chatbot workflow.
- `app/ai/vector_store.py`: ChromaDB knowledge store.

## Conclusion
The project demonstrates how a modern Python backend can combine REST APIs, persistent student data, generative AI, agentic workflows, and vector search in a modular application.
