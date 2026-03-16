from sqlalchemy import Column, Integer , String, ForeignKey
from database import Base


class stud(Base):
    __tablename__ = "stud"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class notes(Base):
    __tablename__ = "notes" 

    id = Column(Integer, primary_key=True)
    content = Column(String)   

    user_id = Column(String, ForeignKey("stud.id"))