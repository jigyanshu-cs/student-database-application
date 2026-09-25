from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post('/', response_model=schemas.StudentResponse, status_code=201)
def create_student(
    x: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_student(db, x)
    except IntegrityError:
        db.rollback()
        raise HTTPException(409, 'Email already exists')


@router.get('/', response_model=list[schemas.StudentResponse])
def list_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_students(db, skip, min(limit, 100))


@router.get('/search', response_model=list[schemas.StudentResponse])
def search(
    q: str,
    db: Session = Depends(get_db)
):
    return crud.search_students(db, q)


@router.get('/{student_id}', response_model=schemas.StudentResponse)
def get(
    student_id: int,
    db: Session = Depends(get_db)
):
    x = crud.get_student(db, student_id)

    if not x:
        raise HTTPException(404, 'Student not found')

    return x


@router.put('/{student_id}', response_model=schemas.StudentResponse)
def update(
    student_id: int,
    x: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    try:
        s = crud.update_student(db, student_id, x)

        if not s:
            raise HTTPException(404, 'Student not found')

        return s

    except IntegrityError:
        db.rollback()
        raise HTTPException(409, 'Email already exists')


@router.delete('/{student_id}')
def delete(
    student_id: int,
    db: Session = Depends(get_db)
):
    if not crud.delete_student(db, student_id):
        raise HTTPException(404, 'Student not found')

    return {'message': 'Student deleted successfully'}