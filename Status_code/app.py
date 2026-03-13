from fastapi import HTTPException

students = ["Rahul", 'Virat']


def view():
    return students

def get_student(index:int):
    if index >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
        
    return {"student" : students[index]}
    
def add_student(name:str):
    students.append(name)

    return{
        "message" : "succesfull",
        "total_std" : len(students),
        "students" : students
    }
