from fastapi import FastAPI
#install using pip , pip install FASTAPI uvicorn

app = FastAPI() # BAckend server

@app.get("/")
def home():
    return {'message' : "heloo vivaan"}

@app.get('/students')
def students():
    students_list = ["Rahul", "Amit", "Neha", "Riya"]
    return {"students": students_list}