from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session

import database, models, crud
from auth import hash_pass , verify_pass

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

@router.post("/login")
def login(usermame:str, password:str, db:Session = Depends(get_db)):
    user = crud.get_user(db, usermame)

   
    if not user:
        raise HTTPException(status_code=404, detail="user npt founf")
    if not verify_pass(password , user.password):
        raise HTTPException(status_code= 401, detail="incoorect pass")
    return {"message" : "login succesfull"}



