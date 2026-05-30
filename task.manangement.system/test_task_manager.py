"""
Test script for the Task Management System.

This script demonstrates and tests all functionality of the task management system,
including valid and invalid input scenarios.
"""

import sys
from datetime import datetime, timedelta

# Import the functions from the task_manager package
from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)


def print_test_case(test_num, description):
    """Print a formatted test case header."""
    print(f"\n[TEST {test_num}] {description}")
    print("-" * 60)


def test_valid_inputs():
    """Test the system with valid inputs."""
    print_section("TESTING VALID INPUTS")
    tasks = []
    
    # Test Case 1: Add a valid task
    print_test_case(1, "Add a valid task")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    success, message, task = add_task(
        tasks,
        "Buy Groceries",
        "Shop at Market Basket for food and household items",
        tomorrow
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    assert success is True, f"Expected valid task to be added: {message}"
    assert task is not None, "Expected task object to be returned for valid input"
    if task:
        print(f"Task created: {task}")
    
    # Test Case 2: Add another valid task
    print_test_case(2, "Add another valid task with different due date")
    future_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    success, message, task = add_task(
        tasks,
        "Complete Project",
        "Finish the Python task management system project",
        future_date
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    assert success is True, f"Expected second valid task to be added: {message}"
    
    # Test Case 3: View pending tasks
    print_test_case(3, "View pending tasks")
    pending = view_pending_tasks(tasks)
    print(f"Number of pending tasks: {len(pending)}")
    assert len(pending) == 2, "Expected two pending tasks after adding valid tasks"
    for idx, task in enumerate(pending, 1):
        print(f"  {idx}. {task['title']} (Due: {task['due_date']})")
    
    # Test Case 4: Mark a task as complete
    print_test_case(4, "Mark first task as complete")
    success, message = mark_task_as_complete(tasks, 0)
    print(f"Result: {message}")
    print(f"Success: {success}")
    assert success is True, f"Expected task to be marked complete: {message}"
    
    # Test Case 5: View updated pending tasks
    print_test_case(5, "View pending tasks after marking one as complete")
    pending = view_pending_tasks(tasks)
    print(f"Number of pending tasks: {len(pending)}")
    assert len(pending) == 1, "Expected one pending task after marking a task complete"
    for idx, task in enumerate(pending, 1):
        print(f"  {idx}. {task['title']} (Due: {task['due_date']})")
    
    # Test Case 6: Calculate progress
    print_test_case(6, "Calculate progress")
    progress = calculate_progress(tasks)
    print(f"Total tasks: {progress['total_tasks']}")
    print(f"Completed tasks: {progress['completed_tasks']}")
    print(f"Pending tasks: {progress['pending_tasks']}")
    print(f"Completion percentage: {progress['completion_percentage']}%")
    assert progress['total_tasks'] == 2, "Expected total tasks count to be 2"
    assert progress['completed_tasks'] == 1, "Expected 1 completed task"
    assert progress['pending_tasks'] == 1, "Expected 1 pending task"
    assert progress['completion_percentage'] == 50.0, "Expected completion percentage to be 50%"
    
    return tasks


def test_invalid_inputs():
    """Test the system with invalid inputs."""
    print_section("TESTING INVALID INPUTS")
    tasks = []
    
    # Test Case 7: Title too short
    print_test_case(7, "Add task with title too short (less than 3 characters)")
    success, message, task = add_task(
        tasks,
        "AB",
        "This is a valid description for testing",
        "2025-07-01"
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (title too short)")
    assert success is False, "Expected invalid title input to fail"
    
    # Test Case 8: Empty title
    print_test_case(8, "Add task with empty title")
    success, message, task = add_task(
        tasks,
        "",
        "This is a valid description for testing",
        "2025-07-01"
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (empty title)")
    assert success is False, "Expected empty title input to fail validation"
    
    # Test Case 9: Title too long
    print_test_case(9, "Add task with title exceeding 100 characters")
    long_title = "A" * 101
    success, message, task = add_task(
        tasks,
        long_title,
        "This is a valid description for testing",
        "2025-07-01"
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (title too long)")
    assert success is False, "Expected overly long title input to fail validation"
    
    # Test Case 10: Description too short
    print_test_case(10, "Add task with description too short (less than 5 characters)")
    success, message, task = add_task(
        tasks,
        "Valid Title",
        "Test",
        "2025-07-01"
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (description too short)")
    assert success is False, "Expected too-short description input to fail validation"
    
    # Test Case 11: Empty description
    print_test_case(11, "Add task with empty description")
    success, message, task = add_task(
        tasks,
        "Valid Title",
        "",
        "2025-07-01"
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (empty description)")
    assert success is False, "Expected empty description input to fail validation"
    
    # Test Case 12: Invalid date format
    print_test_case(12, "Add task with invalid date format (not YYYY-MM-DD)")
    success, message, task = add_task(
        tasks,
        "Valid Title",
        "This is a valid description for testing",
        "06-07-2025"
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (invalid date format)")
    assert success is False, "Expected invalid date format input to fail validation"
    
    # Test Case 13: Past due date
    print_test_case(13, "Add task with past due date")
    past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    success, message, task = add_task(
        tasks,
        "Valid Title",
        "This is a valid description for testing",
        past_date
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (past due date)")
    assert success is False, "Expected past due date input to fail validation"
    
    # Test Case 14: Mark invalid task index as complete
    print_test_case(14, "Add one valid task and attempt to mark invalid index as complete")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    add_task(
        tasks,
        "Valid Task",
        "This is a valid description for testing",
        tomorrow
    )
    success, message = mark_task_as_complete(tasks, 99)
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (invalid task index)")
    assert success is False, "Expected invalid task index to fail"
    
    # Test Case 15: Try to mark already completed task
    print_test_case(15, "Mark task as complete and try to mark it again")
    mark_task_as_complete(tasks, 0)
    success, message = mark_task_as_complete(tasks, 0)
    print(f"Result: {message}")
    print(f"Success: {success}")
    print(f"Expected: False (already completed)")
    assert success is False, "Expected already completed task to fail when marking complete again"


def test_edge_cases():
    """Test edge cases."""
    print_section("TESTING EDGE CASES")
    tasks = []
    
    # Test Case 16: Empty task list progress
    print_test_case(16, "Calculate progress on empty task list")
    progress = calculate_progress(tasks)
    print(f"Progress on empty list: {progress}")
    print(f"Expected: All zeros")
    assert progress == {
        'total_tasks': 0,
        'completed_tasks': 0,
        'pending_tasks': 0,
        'completion_percentage': 0.0
    }, "Expected progress summary to be all zeros for an empty task list"
    
    # Test Case 17: View pending on empty list
    print_test_case(17, "View pending tasks on empty list")
    pending = view_pending_tasks(tasks)
    print(f"Pending tasks: {pending}")
    print(f"Expected: Empty list")
    assert pending == [], "Expected no pending tasks on an empty task list"
    
    # Test Case 18: Add task with whitespace
    print_test_case(18, "Add task with leading/trailing whitespace")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    success, message, task = add_task(
        tasks,
        "  Task with spaces  ",
        "  Description with spaces  ",
        f"  {tomorrow}  "
    )
    print(f"Result: {message}")
    print(f"Success: {success}")
    assert success is True, "Expected valid whitespace-trimmed task to be added successfully"
    if task:
        print(f"Task title after trim: '{task['title']}'")
        print(f"Task description after trim: '{task['description']}'")
        assert task['title'] == 'Task with spaces', "Expected task title to be trimmed"
        assert task['description'] == 'Description with spaces', "Expected task description to be trimmed"
    
    # Test Case 19: All tasks completed progress
    print_test_case(19, "Calculate progress when all tasks are completed")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    add_task(tasks, "Task 1", "Description 1 for testing purposes", tomorrow)
    add_task(tasks, "Task 2", "Description 2 for testing purposes", tomorrow)
    mark_task_as_complete(tasks, 0)
    mark_task_as_complete(tasks, 1)
    progress = calculate_progress(tasks)
    print(f"Progress: {progress}")
    print(f"Expected: 100% completion")
    assert progress['completion_percentage'] == 100.0, "Expected completion percentage to be 100% when all tasks are completed"


def main():
    """Run all tests."""
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "  TASK MANAGEMENT SYSTEM - COMPREHENSIVE TEST SUITE".center(58) + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    
    try:
        # Run test suites
        test_valid_inputs()
        test_invalid_inputs()
        test_edge_cases()
        
        # Final summary
        print_section("TEST SUITE COMPLETED SUCCESSFULLY")
        print("\n✓ All test cases executed successfully!")
        print("✓ The task management system is working correctly.")
        print("✓ Validation functions are properly handling invalid inputs.")
        print("✓ Progress calculation is accurate.")
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
