from sqlalchemy.orm import Session
from app.models import Student
from app.schemas import StudentCreate, StudentUpdate

def create_student(db: Session, x: StudentCreate):
    student = Student(**x.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def search_students(db: Session, q: str):
    return db.query(Student).filter(
        (Student.name.ilike(f"%{q}%")) |
        (Student.email.ilike(f"%{q}%")) |
        (Student.course.ilike(f"%{q}%"))
    ).all()

def update_student(db: Session, student_id: int, x: StudentUpdate):
    student = get_student(db, student_id)
    if not student:
        return None

    for key, value in x.model_dump(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    if not student:
        return False

    db.delete(student)
    db.commit()
    return True
