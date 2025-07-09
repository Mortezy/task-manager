from task_class import *
from typing import List
import shlex

tasks: List[Task] = [Task("test1"), Task("test2"), Task("test3")]


def add(title):
    tasks.append(Task(title))


def list():
    print("Task List:")
    if len(tasks) == 0:
        print("NO TASK FOUND!")
    for i, task in enumerate(tasks):
        print(f"ID: {i}\tTitle: {task}")


def check_status(id: str):
    if not id.isdigit():
        print("Invalid arrguments!")
    elif int(id) >= len(tasks):
        print("ID not found!")
    else:
        print(f"Task status with ID = {id} is: {tasks[int(id)].status.name}")


def set_status(id: str, status: str):
    if (
        not id.isdigit()
        or (status.isdigit() and not int(status) in Status)
        or (not status.isdigit() and not hasattr(Status, status))
    ):
        print("Invalid arrguments!")
    elif int(id) >= len(tasks):
        print("ID not found!")
    else:
        tasks[int(id)].status = Status(int(status))
        print(f"Task status with ID = {id} is set to: {tasks[int(id)].status.name}")


def help():
    print(
        """
Available Commands:

add "task title"          → Add a new task
list                      → Show the list of tasks
set_status ID STATUS      → Change status of a task
check_status ID           → Show the current status of a task
help                      → Show this help message
exit                      → Exit the program

Notes:
- STATUS can be:
    0 or TODO
    1 or IN_PROGRESS
    2 or DONE
    3 or CANCELED
- If your task title has spaces, use quotation marks:
    Example: add "Buy groceries"
"""
    )


def process_cmd(command_string: str):
    cmd = shlex.split(command_string)
    match (cmd[0]):
        case "add":
            if len(cmd) == 2:
                add(cmd[1])
            elif len(cmd) > 2:
                print("Too many arrguments!")
            else:
                print("Not enough arrguments!")
        case "list":
            if len(cmd) == 1:
                list()
            elif len(cmd) > 1:
                print("Too many arrguments!")
            # else:
            #     print("Not enough arrguments!")
        case "set_status":
            if len(cmd) == 3:
                set_status(cmd[1], cmd[2])
            elif len(cmd) > 3:
                print("Too many arrguments!")
            else:
                print("Not enough arrguments!")
        case "check_status":
            if len(cmd) == 2:
                check_status(cmd[1])
            elif len(cmd) > 2:
                print("Too many arrguments!")
            else:
                print("Not enough arrguments!")
        case "help":
            help()
        case _:
            print(f"Unknown command '{cmd[0]}'!")


print("Enter your command (or 'exit')")
while True:
    command = input(">> ")
    if command == "exit":
        break
    else:
        process_cmd(command)
