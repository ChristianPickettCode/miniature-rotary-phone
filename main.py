from fastapi import FastAPI
from todo_controller import TodoController
from todo import Todo

app = FastAPI()
controller = TodoController()

@app.post("/todos/")
async def create_todo(todo: Todo):
    return controller.create_todo(todo)

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    return controller.get_todo(todo_id)

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    return controller.update_todo(todo_id, todo)

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    return controller.delete_todo(todo_id)
