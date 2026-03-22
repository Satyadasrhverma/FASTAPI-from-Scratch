from passlib.context import CryptContext
from jose import JWTError , jwt # install library pytho jose crypthography
#cryptconetxt is a container used to manage different hasing algo , which used schemas
from fastapi import HTTPException, Depends
from datetime import datetime ,timedelta, timezone
from fastapi.security import OAuth2PasswordBearer




secret_key = "vivaan123"
algorithm = "HS256"
acess_token_expire_minutes = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


def hash_pass(password:str):
    return pwd_context.hash(password)

def verify_pass(plain , hased):
    return pwd_context.verify(plain, hased)

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=acess_token_expire_minutes)

    to_encode.update({"exp" : expire})

    token = jwt.encode(to_encode, secret_key,algorithm=algorithm)

    return token


def get_current_user(token:str = Depends(oauth2_scheme)):
    try :
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])

        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="invalid")
        return username
    
    except JWTError:
        raise HTTPException(status_code=401, detail="token is none")
