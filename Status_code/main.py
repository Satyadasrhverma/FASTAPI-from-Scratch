from fastapi import FastAPI, status
from app import view,get_student,add_student

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Welcome"}

@app.get("/students", status_code=status.HTTP_200_OK)
def show_students():
    return view()

@app.get("/students/{index}", status_code=status.HTTP_200_OK)
def show_student(index: int):
    return get_student(index)

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(name: str):
    return add_student(name)