import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Jungle Room", 5, 50.00)
        self.room_2 = Room("Disco Room", 10, 100.00)
        self.room_3 = Room("Outer Space Room", 3, 30.00)

        self.guest_1 = Guest("Gavin", 35, 50.00)
        self.guest_2 = Guest("Ailsa", 27, 45.00)
        self.guest_3 = Guest("Stewart", 32, 55.00)
        self.guest_4 = Guest("Karissa", 27, 48.00)
        self.guest_5 = Guest("Isla", 28, 52.00)

    def test_room_has_name(self):
        self.assertEqual("Jungle Room", self.room_1.name)
    
    def test_room_has_max_capacity(self):
        self.assertEqual(5, self.room_1.max_capacity)

    def test_guests_start_at_0(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())

    def test_check_in_group(self):
        group_1 = [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5]
        self.room_1.check_in_group(group_1)
        self.assertEqual(5, self.room_1.guest_count())

    def test_charge_guest_for_room_share(self):
        self.room_1.charge_for_room_share(self.guest_1)
        self.assertEqual(40, self.guest_1.wallet)

    def test_check_out_guest(self):
        self.room_2.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room_1.guest_count())

    def test_check_out_group(self):
        group_1 = [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5]
        self.room_1.check_out_group(group_1)
        self.assertEqual(0, self.room_1.guest_count())

    def test_add_song_to_queue(self):
        song_choice = Song("Closing Time", "Semisonic")
        self.room_1.add_song_to_queue(song_choice)
        self.assertEqual(1, len(self.room_1.song_queue))