from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def display_menu():
    print("\nTask Management System")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")


def display_all_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks found.")
        return

    print("\nAll Tasks")
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['title']} (Due: {task['due_date']}) - {status}")


def add_new_task(tasks):
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    success, message, _ = add_task(title, description, due_date, tasks)
    if success:
        print("Task added successfully!")
    else:
        print(message)


def mark_task_complete_menu(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available to mark as complete.")
        return

    display_all_tasks(tasks)
    choice = input("Enter task number to mark as complete: ").strip()
    try:
        task_index = int(choice) - 1
    except ValueError:
        print("Invalid task number.")
        return

    success, message = mark_task_as_complete(task_index, tasks)
    if success:
        print("Task marked as complete!")
    else:
        print(message)


def view_pending_tasks_menu(tasks):
    pending = view_pending_tasks(tasks)
    if len(pending) == 0:
        print("\nNo pending tasks.")
        return

    print("\nPending Tasks")
    for idx, task in enumerate(pending, 1):
        print(f"{idx}. {task['title']} (Due: {task['due_date']})")


def view_progress_menu(tasks):
    progress = calculate_progress(tasks)
    print("\nProgress")
    print(f"Total tasks: {progress['total_tasks']}")
    print(f"Completed tasks: {progress['completed_tasks']}")
    print(f"Pending tasks: {progress['pending_tasks']}")
    print(f"Completion percentage: {progress['completion_percentage']}%")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_new_task(tasks)
        elif choice == "2":
            mark_task_complete_menu(tasks)
        elif choice == "3":
            view_pending_tasks_menu(tasks)
        elif choice == "4":
            view_progress_menu(tasks)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
