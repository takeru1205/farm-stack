import crud.todo as todo_crud
from fastapi import APIRouter
from schema.todo import CreateTodo, CreateTodoResponse, Todo

router = APIRouter()


@router.post("/todos", response_model=CreateTodoResponse)
def create_todo(todo: CreateTodo):
    return todo_crud.create_todo(todo)


@router.get("/todos", response_model=list[Todo])
def read_todos():
    return todo_crud.get_todos()


@router.put("/todos/{todo_id}")
def update_todo(todo_id: str, todo: CreateTodo):
    return todo_crud.update_todo(todo_id, todo)


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    return todo_crud.delete_todo(todo_id)
