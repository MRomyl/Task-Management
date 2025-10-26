from datetime import datetime

def validate_task_title(title):
    """
    Validate that the task title is not empty and is a string.
    Returns True if valid, False otherwise.
    """
    if isinstance(title, str) and title.strip():
        return True
    return False

def validate_task_description(description):
    """
    Validate that the description is not empty and is a string.
    Returns True if valid, False otherwise.
    """
    if isinstance(description, str) and description.strip():
        return True
    return False

def validate_due_date(due_date):
    """
    Validate that the due date is in the format YYYY-MM-DD and is a valid date.
    Returns True if valid, False otherwise.
    """
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
