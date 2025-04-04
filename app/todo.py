from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

todo_router = APIRouter()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

todos: List[Todo] = []

@todo_router.get("/", response_model=List[Todo])
def get_all_todos():
    return todos

@todo_router.post("/", response_model=Todo)
def create_todo(todo: Todo):
    if any(t.id == todo.id for t in todos):
        raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    todos.append(todo)
    return todo

@todo_router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@todo_router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": "Todo deleted"}
