from passlib.context import CryptContext
#cryptconetxt is a container used to manage different hasing algo , which used schemas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


def hash_pass(password:str):
    return pwd_context.hash(password)

def verify_pass(plain , hased):
    return pwd_context.verify(plain, hased)