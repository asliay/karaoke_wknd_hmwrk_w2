import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Jungle Room", 5)
        self.guest = Guest("Gavin", 50.00)

    def test_room_has_name(self):
        self.assertEqual("Jungle Room", self.room.name)
    
    def test_room_has_max_capacity(self):
        self.assertEqual(5, self.room.max_capacity)

    def test_guests_start_at_0(self):
        self.assertEqual(0, self.room.guest_count())

    def test_add_guests_to_room(self):
        self.room.add_guests(self.guest)
        self.assertEqual(1, self.room.guest_count())