# 📝 Task Manager (CLI + Web API – Python)

A minimal task manager project written in Python.  
This project includes two interfaces:

- ✅ A simple **CLI version** for command-line task management
- 🌐 A basic **Flask-based web API** for interacting via HTTP

---

## 📁 Project Structure

```

task-manager/
│
├── core/
│   └── task\_class.py       # Task class and Status enum
│
├── cli/
│   └── manage.py           # CLI interface
│
├── web/
│   ├── **init**.py
│   └── app.py              # Flask web API
│
└── README.md

```

---

## 🚀 How to Use

### ▶ CLI Version

Run the CLI interface:

```bash
python -m cli.manage
```

### 📌 CLI Commands

```
add "task title"          → Add a new task
list                      → Show the list of tasks
set_status ID STATUS      → Change status of a task
check_status ID           → Show the current status of a task
help                      → Show help message
exit                      → Exit the program
```

> 💡 Tip: Wrap task titles with spaces in quotes → `add "Buy groceries"`

---

### ▶ Flask Web API Version

Start the Flask server:

```bash
python -m web.app
```

The server will run at: `http://localhost:8000`

---

## 🔗 API Endpoints

### 📤 Get All Tasks

**GET** `/tasks`

Example:

```
GET http://localhost:8000/tasks
```

Response:

```json
{
  "task list": [
    {
      "id": 0,
      "task": {
        "title": "Buy milk",
        "to do date": "2025-07-07",
        "status": "TODO"
      }
    }
  ]
}
```

---

### 📥 Add a New Task

**POST** `/tasks?title=YourTitle`

Query Parameter:

- `title` (required)

Example:

```
POST http://localhost:8000/tasks?title=Read%20book
```

---

## 🎯 Status Options

You can set the task status (CLI) using either number or name:

| Code | Name        |
| ---- | ----------- |
| 0    | TODO        |
| 1    | IN_PROGRESS |
| 2    | DONE        |
| 3    | CANCELED    |

---

## 🛠 Requirements

- Python 3.10+
- Flask (for the web version)

Install Flask if needed:

```bash
pip install flask
```

---

## 📌 Notes

- Tasks are stored in memory (not persistent).
- Both CLI and Web are built to be beginner-friendly.
- Can be extended with:

  - File or database persistence
  - More API endpoints (e.g., update/delete)
  - Task filtering or search

---

## 👨‍💻 Author

💻 [Mortezy](https://github.com/Mortezy)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---
