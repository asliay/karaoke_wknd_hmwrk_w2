import unittest

from classes.song import Song
from classes.guest import Guest
from classes.room import Room
from classes.drink import Drink

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Closing Time", "Semisonic")

    def test_song_has_name(self):
        self.assertEqual("Closing Time", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Semisonic", self.song.artist)
