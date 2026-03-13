tasks = []
def get_task():
    return {
        "total_task" : len(tasks),
        "tasks" : tasks
    }

def create_task(title:str):
    task = {
        "id" : len(tasks) + 1,
        "title" : title
    }

    tasks.append(task)

    return {
        "message" :"task created",
        "task" : task
    }