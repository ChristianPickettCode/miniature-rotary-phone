from typing import Dict
from todo import Todo

class TodoController:
    def __init__(self):
        self.todos: Dict[int, Todo] = {}

    def create_todo(self, todo: Todo) -> Todo:
        self.todos[todo.id] = todo
        return todo

    def get_todo(self, todo_id: int) -> Todo:
        return self.todos.get(todo_id)

    def update_todo(self, todo_id: int, todo: Todo) -> Todo:
        if todo_id in self.todos:
            self.todos[todo_id] = todo
            return todo
        return None

    def delete_todo(self, todo_id: int) -> bool:
        if todo_id in self.todos:
            del self.todos[todo_id]
            return True
        return False
