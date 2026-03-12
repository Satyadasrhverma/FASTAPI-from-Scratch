#PYDANTIC model is represent the ideal schemas for the data, that the user insert and seach data with coreect data types


from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from app import Medicine , load_data, save_data
app = FastAPI()

@app.get("/")
def home():
    return {"message" : "hlooo worker"}

@app.get("/all")
def get_medicine():
    return load_data

@app.post("/add/{med_id}")
def add_medicine(med_id : str, med : Medicine):
    data = load_data()

    if med_id in data:
        raise HTTPException(status_code=404, detail= "id alreaddy exist")
    
    new_med = med.model_dump()

    data[med_id] = new_med

    save_data(data)

    return {
        
        "message": "Medicine added successfully",
        "medicine_id": med_id,
        "data": new_med
    }
    

