from lib.phase3_part3 import *
import unittest
from unittest import mock

class TestDiary(unittest.TestCase):
    def test_diary_read(self):
        diary = Diary("Test contents")
        self.assertEqual(diary.read(), "Test contents")

class TestSecretDiary(unittest.TestCase):
    def test_secret_diary_locked_read(self):
        diary = Diary("Test contents")
        secret_diary = SecretDiary(diary)

        with self.assertRaises(Exception):
            secret_diary.read()

    def test_secret_diary_unlocked_read(self):
        diary = Diary("Test contents")
        secret_diary = SecretDiary(diary)
        secret_diary.unlock()

        self.assertEqual(secret_diary.read(), "Test contents")

    def test_secret_diary_lock(self):
        diary = Diary("Test contents")
        secret_diary = SecretDiary(diary)
        secret_diary.unlock()

        secret_diary.lock()
        with self.assertRaises(Exception):
            secret_diary.read()

    def test_secret_diary_unlock(self):
        diary = Diary("Test contents")
        secret_diary = SecretDiary(diary)
        secret_diary.unlock()

        secret_diary.lock()
        secret_diary.unlock()
        self.assertEqual(secret_diary.read(), "Test contents")

if __name__ == "__main__":
    unittest.main()