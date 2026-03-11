# the main HTTP mehtod are 1.GET , 2.POST , 3.PUT , 4.DELETE
from fastapi import FastAPI

app = FastAPI()

students = ["rahul", "vishal"]

@app.get("/students")
def students ():
    return {"students" : students}

@app.post("/studenst")
def add_student(name:str):
    students.append(name)
    return {"Message" : "students added"}


@app.put("/students/{index}")
def update_student(index:int, name:str):
    students[index] = name
    return {"message":"Student updated"}

@app.delete("/students/{index}")
def delete_student(index:int):
    students.pop(index)
    return {"message":"Student deleted"}