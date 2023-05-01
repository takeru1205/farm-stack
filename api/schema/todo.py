from typing import Union

from pydantic import BaseModel


class BaseTodo(BaseModel):
    title: str
    description: Union[str, None] = None
    completed: bool = False


class Todo(BaseTodo):
    id: str


class CreateTodo(BaseTodo):
    pass


class CreateTodoResponse(CreateTodo):
    id: str


class DeleteTodoResponse:
    id: str
    message: str
