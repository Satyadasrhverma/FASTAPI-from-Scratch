from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session

import database, models, crud
from auth import hash_pass , verify_pass, create_access_token

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
def login(username: str, password: str, db: Session = Depends(get_db)):

    user = crud.get_user(db, username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_pass(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_access_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }