from sqlalchemy.orm import Session
import models

def get_user(db:Session, username:str):
    return db.query(models.stud).filter(
        models.stud.username == username).first()
    