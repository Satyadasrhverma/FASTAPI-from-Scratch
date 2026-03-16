from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session

import database, models
from auth import hash_pass

router = APIRouter()

def get_db():
    db = database.sessionloacal()

    try :
        yield db
    finally:
        db.close()    

@router.post("/register")
def register(username:str, password : str, db:Session = Depends(get_db)):
     hased = hash_pass(password)

     user = models.stud(
         username = username,
         password = hased
     )        

     db.add(user)
     db.commit()

     return{"messages" : "user_created"}

