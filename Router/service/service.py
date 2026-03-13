def add(a:int , b : int):
    return {"operation" : "addition" , "result" : a + b}

def subtract(a : int , b: int):
    return {"opertation" : "subtract" , "result" : a-b}

def multiply(a:float, b:float):
    return {"operttion" : "multiplication" , "result" : a*b}
    
def divide(a: int, b: int):

    if b == 0:
        return {"error": "Division by zero not allowed"}

    return {"operation": "division", "result": a / b}
