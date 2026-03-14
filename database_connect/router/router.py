from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session

import database 
import crude 

router = APIRouter()

def get_db():
    db = database.Session()

    try :
        yield db
    finally:
        db.close()    
@router.get("/student")
def view_stud(db:Session = Depends(get_db)):
    return crude.get_stud(db)

@router.post("/students")
def add_stud(name:str , db:Session = Depends(get_db)):
    return crude.create_stud(db , name)