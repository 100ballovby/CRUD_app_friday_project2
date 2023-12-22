import requests as r
from models import ToDo


def fill_todo(db):
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = r.get(url)
    todos = response.json()
    for todo in todos:
        todo_instance = ToDo(
            title=todo['title'],
            user_id=todo['userId'],
            completed=todo['completed']
        )
        db.session.add(todo_instance)
    db.session.commit()




