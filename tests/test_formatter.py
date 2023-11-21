from unittest.mock import Mock
import unittest
from lib.phase3_part1 import TaskFormatter

def test_initalisation_task_formatter():
        test_task = Mock()
        test_formatter = TaskFormatter(test_task)
        assert test_formatter.task == test_task
        
def test_format_incomplete_task():
        # Create a Mock Task instance for an incomplete task
        task_Mock = Mock()
        task_Mock.is_complete.return_value = False
        task_Mock.title = "Test Task"
    
        # Test TaskFormatter format method
        formatter = TaskFormatter(task_Mock)
        result = formatter.format()

        assert result == "- [ ] Test Task"
        
def test_format_complete_task():
    task_Mock = Mock()
    task_Mock.is_complete.return_value = True
    task_Mock.title = "Test Task"

    # Test TaskFormatter format method
    formatter = TaskFormatter(task_Mock)
    result = formatter.format()

    assert result == "- [x] Test Task"
    
def test_format_complete_task_different_title():
    task_Mock = Mock()
    task_Mock.is_complete.return_value = True
    task_Mock.title = "A long task"

    # Test TaskFormatter format method
    formatter = TaskFormatter(task_Mock)
    result = formatter.format()

    assert result == "- [x] A long task"