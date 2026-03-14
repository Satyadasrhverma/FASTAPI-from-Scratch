from sqlalchemy.orm import Session
from models import Student

def create_stud(db:Session, name:str):
    student = Student(name=name)

    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_stud(db:Session):
    return db.query(Student).all()
