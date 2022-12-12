from fastapi import APIRouter, Path
from model import Todo, TodoList

todo_router = APIRouter()

#todo_list = TodoList(todos=[Todo(id = 1, item ="finish this book"), Todo(id = 2, item = "second todo")])
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.post("/todos")
async def add_todo(todos: TodoList) -> dict:
    todo_list.extends(todos)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

@todo_router.get("/todo/{id}")
async def get_single_todo(id: int = Path(..., title = "The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == id:
            print(f"id: {id}")
            return {"todo": todo}
    
    return {"message": "Todo with supplied ID doesn't exist."}