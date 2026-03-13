from fastapi import HTTPException

def verify (api_key:str):
    if api_key != "1234":
        raise HTTPException(status_code=401, detail= "invalid")
    
    return api_key