from passlib.context import CryptContext
from jose import JWTError , jwt # install library pytho jose crypthography
#cryptconetxt is a container used to manage different hasing algo , which used schemas

from datetime import datetime ,timedelta, timezone




secret_key = "vivaan123"
algorithm = "HS256"
acess_token_expire_minutes = 30



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