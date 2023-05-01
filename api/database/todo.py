# ./api/database/todo.py

from pymongo import MongoClient

HOST = "mongo_db"
PORT = 27017
USERNAME = "root"
PASSWORD = "password"
DATABASE = "todo_db"

client = MongoClient(HOST, PORT, username=USERNAME, password=PASSWORD)
db = client[DATABASE]


def make_todos():
    for i in range(10):
        db.todos.insert_one(
            {
                "title": f"Todo {i}",
                "description": f"Todo {i} description",
                "completed": False,
            }
        )


if __name__ == "__main__":
    make_todos()
