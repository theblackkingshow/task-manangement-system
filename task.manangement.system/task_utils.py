"""
Task utilities module for task management system.

This module contains functions for adding tasks, marking tasks as complete,
viewing pending tasks, and calculating progress.
"""

from datetime import datetime
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Global tasks list
tasks = []


def add_task(title, description, due_date, task_list=None):
    """
    Add a new task to the task list after validating input.
    
    Args:
        title (str): The task title
        description (str): The task description
        due_date (str): The task due date in YYYY-MM-DD format
        task_list (list): Optional task list to add to
        
    Returns:
        tuple: (success: bool, message: str, task: dict or None)
    """
    if task_list is None:
        task_list = tasks
    
    # Validate title
    is_valid, error_msg = validate_task_title(title)
    if not is_valid:
        return False, f"Title validation failed: {error_msg}", None
    
    # Validate description
    is_valid, error_msg = validate_task_description(description)
    if not is_valid:
        return False, f"Description validation failed: {error_msg}", None
    
    # Validate due date
    is_valid, error_msg = validate_due_date(due_date)
    if not is_valid:
        return False, f"Due date validation failed: {error_msg}", None
    
    # Create task dictionary
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    
    task_list.append(task)
    return True, f"Task '{task['title']}' added successfully!", task


def mark_task_as_complete(index, task_list=None):
    """
    Mark a task as complete.
    
    Args:
        index (int): The index of the task to mark as complete
        task_list (list): Optional task list
        
    Returns:
        tuple: (success: bool, message: str)
    """
    if task_list is None:
        task_list = tasks
    
    if not isinstance(index, int) or index < 0 or index >= len(task_list):
        return False, "Invalid task index."
    
    if task_list[index]["completed"]:
        return False, "Task is already completed."
    
    task_list[index]["completed"] = True
    return True, f"Task '{task_list[index]['title']}' marked as complete!"


def view_pending_tasks(task_list=None):
    """
    View all pending (incomplete) tasks.
    
    Args:
        task_list (list): Optional task list
        
    Returns:
        list: List of pending tasks
    """
    if task_list is None:
        task_list = tasks
    
    pending_tasks = [task for task in task_list if not task["completed"]]
    return pending_tasks


def calculate_progress(task_list=None):
    """
    Calculate the progress of task completion.
    
    Args:
        task_list (list): Optional task list
        
    Returns:
        dict: Dictionary containing progress information
    """
    if task_list is None:
        task_list = tasks
    
    if len(task_list) == 0:
        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0.0
        }
    
    completed_count = sum(1 for task in task_list if task["completed"])
    pending_count = len(task_list) - completed_count
    completion_percentage = (completed_count / len(task_list)) * 100
    
    return {
        "total_tasks": len(task_list),
        "completed_tasks": completed_count,
        "pending_tasks": pending_count,
        "completion_percentage": round(completion_percentage, 2)
    }
