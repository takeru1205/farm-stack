from bson import ObjectId
from database.todo import db
from schema.todo import CreateTodo, CreateTodoResponse, Todo


def create_todo(todo: CreateTodo) -> CreateTodoResponse:
    id = db.todos.insert_one(todo.dict())
    return CreateTodoResponse(id=str(id.inserted_id), **todo.dict())


def get_todos() -> list[Todo]:
    todos = list(db.todos.find())
    for idx, todo in enumerate(todos):
        todo["id"] = str(todo["_id"])
        todos[idx] = todo
    return todos


def update_todo(todo_id: str, todo: CreateTodo) -> CreateTodoResponse:
    db.todos.update_one({"_id": ObjectId(todo_id)}, {"$set": todo.dict()})
    return CreateTodoResponse(id=todo_id, **todo.dict())


def delete_todo(todo_id: str):
    db.todos.delete_one({"_id": ObjectId(todo_id)})
    return {"id": todo_id, "message": "Todo deleted successfully"}
