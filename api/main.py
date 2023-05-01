import uvicorn
from fastapi import FastAPI

from router.todo import router as todo_router

app = FastAPI()

app.include_router(todo_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
