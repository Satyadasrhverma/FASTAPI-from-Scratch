from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f :
        data = json.load(f)
    return data    

@app.get("/")
def home():
    return{"message" : "heloo how i help you ??"}
@app.get("/view")
def view_all():
    return load_data()

@app.get("/view/{patients_id}")
def view(patients_id: str):
    data = load_data()
    

    if patients_id in data:
        return data[patients_id]
    raise HTTPException(status_code=404 , detail="patient not found")

    