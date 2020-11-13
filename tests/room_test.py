import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Jungle Room", 10)

    def test_room_has_name(self):
        self.assertEqual("Jungle Room", self.room.name)
    
    def test_room_has_max_capacity(self):
        self.assertEqual(10, self.room.max_capacity)