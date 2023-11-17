from lib.phase3_part1 import *
import unittest

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

if __name__ == '__main__':
    unittest.main()