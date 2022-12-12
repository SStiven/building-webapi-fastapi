from fastapi import FastAPI
from todo import todo_router
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
	return { "message": "Hello"}

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)