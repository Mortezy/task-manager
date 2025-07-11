from datetime import date
from enum import Enum
import json


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

    def to_dict(self):
        return {
            "title": self.title,
            "to do date": self.todo_date.isoformat(),
            "status": self.status.name,
        }

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return str(self)
