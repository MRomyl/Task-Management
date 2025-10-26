from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # Validate inputs
    if not validate_task_title(title):
        print("Invalid task title. Task not added.")
        return
    if not validate_task_description(description):
        print("Invalid task description. Task not added.")
        return
    if not validate_due_date(due_date):
        print("Invalid due date. Use format YYYY-MM-DD. Task not added.")
        return

    # Add task
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return
    for idx, task in enumerate(pending, start=1):
        print(f"{idx}. {task['title']} (Due: {task['due_date']}) - {task['description']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        return 0
    completed = sum(t["completed"] for t in tasks)
    progress = (completed / total) * 100
    return progress
