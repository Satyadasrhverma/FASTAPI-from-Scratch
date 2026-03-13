from fastapi import HTTPException

def validate(title:str):
    if len(title) <3:
        raise HTTPException(status_code=400, detail="task must be 3 charachter")
    return title