# a fastapi system for Todos creating and management
# check Python version: must be 3.11.9
# to run this code, use command 'fastapi dev fastapi_todos.py'

from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()

class Todos(BaseModel):
    id: int
    name: str
    description: str
    date: datetime.date

# type hint for a list of Todos
todos:list[Todos] = []

@app.post("/todos/")
def create_todo(todo: Todos):
    todos.append(todo)
    return {"message": "Todo created successfully"}

@app.get("/todos/")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Such todo was not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    todos[:] = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted successfully"}
