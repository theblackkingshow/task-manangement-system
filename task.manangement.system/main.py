"""
Main script for the Task Management System.

This script provides a menu-based interface for users to interact with
the task management system.
"""

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("TASK MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. View all pending tasks")
    print("4. View all tasks")
    print("5. View progress")
    print("6. Exit")
    print("="*50)


def display_all_tasks(tasks):
    """
    Display all tasks with their status.
    
    Args:
        tasks (list): The list of tasks
    """
    if len(tasks) == 0:
        print("\nNo tasks found.")
        return
    
    print("\n" + "-"*80)
    print(f"{'#':<3} {'Title':<20} {'Due Date':<12} {'Status':<12}")
    print("-"*80)
    
    for idx, task in enumerate(tasks, 1):
        status = "✓ Completed" if task["completed"] else "⊘ Pending"
        print(f"{idx:<3} {task['title']:<20} {task['due_date']:<12} {status:<12}")
    
    print("-"*80)


def add_new_task(tasks):
    """
    Prompt user to add a new task.
    
    Args:
        tasks (list): The list of tasks
    """
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    
    success, message, _ = add_task(tasks, title, description, due_date)
    
    if success:
        print(f"\n✓ {message}")
    else:
        print(f"\n✗ Error: {message}")


def mark_task_complete(tasks):
    """
    Prompt user to mark a task as complete.
    
    Args:
        tasks (list): The list of tasks
    """
    if len(tasks) == 0:
        print("\nNo tasks available to mark as complete.")
        return
    
    print("\n--- Mark Task as Complete ---")
    display_all_tasks(tasks)
    
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        task_index = task_num - 1
        
        success, message = mark_task_as_complete(tasks, task_index)
        
        if success:
            print(f"\n✓ {message}")
        else:
            print(f"\n✗ Error: {message}")
    except ValueError:
        print("\n✗ Error: Please enter a valid task number.")


def view_pending(tasks):
    """
    Display all pending tasks.
    
    Args:
        tasks (list): The list of tasks
    """
    pending = view_pending_tasks(tasks)
    
    if len(pending) == 0:
        print("\n🎉 Great! All tasks are completed!")
        return
    
    print("\n" + "-"*80)
    print(f"PENDING TASKS ({len(pending)})")
    print("-"*80)
    print(f"{'#':<3} {'Title':<20} {'Description':<35} {'Due Date':<12}")
    print("-"*80)
    
    for idx, task in enumerate(pending, 1):
        desc = task['description'][:32] + "..." if len(task['description']) > 32 else task['description']
        print(f"{idx:<3} {task['title']:<20} {desc:<35} {task['due_date']:<12}")
    
    print("-"*80)


def view_progress(tasks):
    """
    Display task progress.
    
    Args:
        tasks (list): The list of tasks
    """
    progress = calculate_progress(tasks)
    
    print("\n" + "="*50)
    print("PROGRESS REPORT")
    print("="*50)
    print(f"Total Tasks:        {progress['total_tasks']}")
    print(f"Completed Tasks:    {progress['completed_tasks']}")
    print(f"Pending Tasks:      {progress['pending_tasks']}")
    print(f"Completion Rate:    {progress['completion_percentage']}%")
    
    # Visual progress bar
    if progress['total_tasks'] > 0:
        filled = int(progress['completion_percentage'] / 5)
        bar = "█" * filled + "░" * (20 - filled)
        print(f"Progress:           [{bar}] {progress['completion_percentage']}%")
    
    print("="*50)


def main():
    """Main function to run the task management system."""
    tasks = []
    
    print("\n🎯 Welcome to the Task Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_new_task(tasks)
        elif choice == "2":
            mark_task_complete(tasks)
        elif choice == "3":
            view_pending(tasks)
        elif choice == "4":
            display_all_tasks(tasks)
        elif choice == "5":
            view_progress(tasks)
        elif choice == "6":
            print("\n👋 Thank you for using the Task Management System! Goodbye!")
            break
        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
