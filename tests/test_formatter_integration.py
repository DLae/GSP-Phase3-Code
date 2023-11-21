from unittest.mock import Mock
from lib.phase3_part1 import TaskFormatter, Task

def test_initalisation_task_formatter():
        test_task = Task("Anything")
        test_formatter = TaskFormatter(test_task)
        assert test_formatter.task == test_task
        
def test_format_incomplete_task():
        # Create a Mock Task instance for an incomplete task
        task_Mock = Task("Anything")
    
        # Test TaskFormatter format method
        formatter = TaskFormatter(task_Mock)
        result = formatter.format()

        assert result == "- [ ] Anything"
        
def test_format_complete_task():
    task_Mock = Task("Anything")
    task_Mock.mark_complete()

    # Test TaskFormatter format method
    formatter = TaskFormatter(task_Mock)
    result = formatter.format()

    assert result == "- [x] Anything"
    