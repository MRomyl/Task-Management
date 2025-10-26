# Import functions from task_utils
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # Add a new task
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            add_task(title, description, due_date)

        elif choice == "2":
            # Mark a task as complete
            if not tasks:
                print("No tasks available to mark as complete.")
                continue
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{idx}. {task['title']} [{status}]")
            try:
                index = int(input("Enter the task number to mark as complete: "))
                mark_task_as_complete(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            # View pending tasks
            view_pending_tasks()

        elif choice == "4":
            # View progress
            progress = calculate_progress()
            print(f"Progress: {progress:.2f}% tasks completed.")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
