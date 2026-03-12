import json
from pydantic import BaseModel


class Medicine(BaseModel):
    name : str
    stock_quantity : int
    price: float


def load_data():
    try:
        with open("medicine.json" , "r") as f :
            data = json.load(f)
            return data
    except Exception as e:
        print ("erroe loading data" , e)
def save_data(data):
     with open("medicine.json" , "w") as f :
         json.dump(data , f , indent=5)