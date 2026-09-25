from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    course = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    cgpa = Column(Float, nullable=True)
    phone = Column(String(20), nullable=True)
