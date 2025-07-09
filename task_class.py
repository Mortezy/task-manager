from datetime import date
from enum import Enum


class Status(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    CANCELED = 3


class Task:

    def __init__(self, title, todo_date=date.today()):
        self.title = title
        self.todo_date = todo_date
        self.status: Status = Status.TODO

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return str(self)
