"""
Validation module for task management system.

This module contains functions to validate user input for task details
such as title, description, and due date.
"""

from datetime import datetime
import re


def validate_task_title(title):
    """
    Validate the task title.
    
    Args:
        title (str): The title to validate
        
    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not isinstance(title, str):
        return False, "Title must be a string."
    
    title = title.strip()
    
    if len(title) == 0:
        return False, "Title cannot be empty."
    
    if len(title) < 3:
        return False, "Title must be at least 3 characters long."
    
    if len(title) > 100:
        return False, "Title cannot exceed 100 characters."
    
    return True, None


def validate_task_description(description):
    """
    Validate the task description.
    
    Args:
        description (str): The description to validate
        
    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not isinstance(description, str):
        return False, "Description must be a string."
    
    description = description.strip()
    
    if len(description) == 0:
        return False, "Description cannot be empty."
    
    if len(description) < 5:
        return False, "Description must be at least 5 characters long."
    
    if len(description) > 500:
        return False, "Description cannot exceed 500 characters."
    
    return True, None


def validate_due_date(due_date):
    """
    Validate the due date.
    
    Args:
        due_date (str): The due date to validate in format YYYY-MM-DD
        
    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not isinstance(due_date, str):
        return False, "Due date must be a string."
    
    due_date = due_date.strip()
    
    # Check date format
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(date_pattern, due_date):
        return False, "Due date must be in YYYY-MM-DD format."
    
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        current_date = datetime.now()
        
        if due_date_obj.date() < current_date.date():
            return False, "Due date cannot be in the past."
        
        return True, None
    except ValueError:
        return False, "Invalid date. Please ensure the date is valid (e.g., 2024-06-26)."
