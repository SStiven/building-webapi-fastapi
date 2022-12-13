from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }

class TodoList(BaseModel):
    todos: List[Todo]

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }