from langchain_core.tools import tool
from app.database import SessionLocal
from app import crud
@tool
def find_student(query:str)->str:
    '''Search student records by name, email or course.'''
    db=SessionLocal()
    try:
        rows=crud.search_students(db,query)
        return 'No matching students found.' if not rows else '\n'.join(f'ID={x.id}, Name={x.name}, Email={x.email}, Course={x.course}, Year={x.year}, CGPA={x.cgpa}' for x in rows)
    finally: db.close()
@tool
def get_student_by_id(student_id:int)->str:
    '''Retrieve one student by ID.'''
    db=SessionLocal()
    try:
        x=crud.get_student(db,student_id)
        return 'Student not found.' if not x else f'ID={x.id}, Name={x.name}, Email={x.email}, Course={x.course}, Year={x.year}, CGPA={x.cgpa}'
    finally: db.close()
TOOLS=[find_student,get_student_by_id]
