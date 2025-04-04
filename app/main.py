from fastapi import FastAPI
from app.todo import todo_router

app = FastAPI(title="Simple TODO App")

app.include_router(todo_router, prefix="/todos")
