from fastapi import APIRouter
from service.service import add, divide,multiply,subtract

viv = APIRouter()

@viv.get("/add")
def add_num(a:int, b:int):
    return add(a,b)

@viv.get("/sub")
def subtract_num(a:int, b:int):

    return subtract(a,b)

@viv.get("/multiply")
def multiply_numbers(a: int, b: int):
    return multiply(a, b)


@viv.get("/divide")
def divide_numbers(a: int, b: int):
    return divide(a, b)