```markdown
# 📝 Task Manager (CLI – Python)

A minimal, terminal-based task manager written in Python.  
Manage your daily tasks from the command line: add, list, and update task status — fast and simple.

---

## 📁 Project Structure
```

task_manager/
│
├── manage.py # Main CLI interface
├── task_class.py # Task class and Status enum

````

---

## 🚀 How to Use

### ▶ Run the App

```bash
python manage.py
````

### 📌 Available Commands

```
add "task title"          → Add a new task
list                      → Show the list of tasks
set_status ID STATUS      → Change status of a task
check_status ID           → Show the current status of a task
help                      → Show help message
exit                      → Exit the program
```

> 💡 Tip: If your task title contains spaces, wrap it in quotes
> Example: `add "Buy groceries"`

---

## 🎯 Status Options

You can set the task status using either number or name:

| Code | Name        |
| ---- | ----------- |
| 0    | TODO        |
| 1    | IN_PROGRESS |
| 2    | DONE        |
| 3    | CANCELED    |

---

## 🛠 Requirements

Just Python 3.10+
No external libraries needed.

---

## 📌 Notes

- This is a beginner-friendly CLI project designed to practice:

  - Classes and enums
  - Command parsing
  - Lists and loops
  - Basic user interaction

- Tasks are **not** yet saved to disk.
  (Can be extended with JSON or SQLite support later.)

---

## 🧑‍💻 Author

Created with ❤️ by [Mortezy](https://github.com/Mortezy) – as part of my learning journey.
Feel free to use, fork, or suggest improvements!

```

---
```
