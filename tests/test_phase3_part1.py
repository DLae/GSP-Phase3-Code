from unittest.mock import Mock
import unittest
from lib.phase3_part1 import Track, MusicLibrary
from lib.phase3_part1 import Task, TaskList, TaskFormatter

class TestTrack(unittest.TestCase):
    def test_track_creation(self):
        track = Track("Song Title", "Artist Name")
        self.assertEqual(track.title, "Song Title")
        self.assertEqual(track.artist, "Artist Name")

    def test_track_matches(self):
        track = Track("Song Title", "Artist Name")
        self.assertTrue(track.matches("Song Title"))
        self.assertTrue(track.matches("Artist Name"))
        self.assertFalse(track.matches("Unknown"))

class TestMusicLibrary(unittest.TestCase):
    def test_music_library_creation(self):
        library = MusicLibrary()
        self.assertEqual(len(library.tracks), 0)

    def test_add_track_to_library(self):
        library = MusicLibrary()
        track = Track("Song Title", "Artist Name")
        library.add(track)
        self.assertEqual(len(library.tracks), 1)
        self.assertEqual(library.tracks[0], track)

    def test_search_in_library(self):
        library = MusicLibrary()
        track1 = Track("Song Title 1", "Artist Name")
        track2 = Track("Song Title 1", "Another Artist")
        library.add(track1)
        library.add(track2)

        results = library.search("Song Title 1")
        self.assertEqual(len(results), 2)
        self.assertIn(track1, results)
        self.assertIn(track2, results)

        results = library.search("Another Artist")
        self.assertEqual(len(results), 1)
        self.assertIn(track2, results)
        self.assertNotIn(track1, results)

def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]

def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True


def test_constructs():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

def test_can_be_marked_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.is_complete() == True


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False



class TestTaskFormatter(unittest.TestCase):
    def test_initalisation_task_formatter():
        test_task = Mock()
        test_formatter = TaskFormatter(test_task)
        assert test_formatter.task == test_task  

    def test_format_incomplete_task(self):
        # Create a Mock Task instance for an incomplete task
        task_Mock = Mock(spec=Task)
        task_Mock.is_complete.return_value = False
        task_Mock.title = "Incomplete Task"

        # Test TaskFormatter format method
        formatter = TaskFormatter(task_Mock)
        result = formatter.format()

        # Assert the expected format for an incomplete task
        self.assertEqual(result, "- [ ] Incomplete Task")

    def test_format_complete_task(self):
        # Create a Mock Task instance for a complete task
        task_Mock = Mock(spec=Task)
        task_Mock.is_complete.return_value = True
        task_Mock.title = "Complete Task"

        # Test TaskFormatter format method
        formatter = TaskFormatter(task_Mock)
        result = formatter.format()

        # Assert the expected format for a complete task
        self.assertEqual(result, "- [x] Complete Task")

    def test_format_empty_task_title(self):
        # Create a Mock Task instance with an empty title
        task_Mock = Mock(spec=Task)
        task_Mock.is_complete.return_value = False
        task_Mock.title = ""

        # Test TaskFormatter format method
        formatter = TaskFormatter(task_Mock)
        result = formatter.format()

        # Assert the expected format for a task with an empty title
        self.assertEqual(result, "- [ ] ")

    def test_format_integration(self):
        # Create a real Task instance for an incomplete task
        task = Task("Real Incomplete Task")

        # Create a TaskFormatter instance
        formatter = TaskFormatter(task)

        # Test TaskFormatter format method
        result = formatter.format()

        # Assert the expected format for an incomplete task
        self.assertEqual(result, "- [ ] Real Incomplete Task")


if __name__ == '__main__':
    unittest.main()