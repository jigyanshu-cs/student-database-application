from app.database import Base,engine,SessionLocal
from app.models import Student
from app.ai.vector_store import seed_project_knowledge
Base.metadata.create_all(bind=engine)
db=SessionLocal()
if db.query(Student).count()==0:
    db.add_all([Student(name='Aarav Sharma',email='aarav@example.com',course='BTech CSE',year=2,cgpa=8.4,phone='9876543210'),Student(name='Priya Verma',email='priya@example.com',course='BTech CSE',year=3,cgpa=9.1,phone='9876543211'),Student(name='Rahul Kumar',email='rahul@example.com',course='BCA',year=2,cgpa=7.8,phone='9876543212')]);db.commit()
db.close();seed_project_knowledge();print('Initialized.')
