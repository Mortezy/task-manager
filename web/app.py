from flask import Flask, request, Response
from core.task_class import Task
import json

app = Flask(__name__)

# tasks = [Task("task1"), Task("task2"), Task("task3")]
tasks = []


@app.route("/tasks", methods=["GET"])
def get_list():
    list = []
    json_str = {"task list": list}
    for i, obj in enumerate(tasks):
        task = {}
        task["id"] = i
        task["task"] = obj.to_dict()
        list.append(task)
    if len(tasks) == 0:
        json_str["task list"] = "NO TASK FOUND!"
    else:
        json_str["task list"] = list

    json_str = json.dumps(json_str, sort_keys=False)
    return Response(json_str, mimetype="application/json")


@app.route("/tasks", methods=["POST"])
def add_task():
    if not "title" in request.args:
        return "'title' is required!", 400

    new_task = Task(request.args["title"])
    tasks.append(new_task)
    return "New task is added successfuly!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
