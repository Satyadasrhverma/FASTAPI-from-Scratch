from fastapi import FastAPI , Depends
from dependencies.auth import verify
from dependencies.validation import validate
from service.service import get_task, create_task

app = FastAPI()

@app.get("/tasks")
def view_task(api_key :str = Depends(verify)):
    return get_task()


@app.get("/add")
def add_tasks(title :str = Depends(validate), api_key : str = Depends(verify)):
    return create_task(title)#http://127.0.0.1:8000/add?title=fastapi&api_key=1234