import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Closing Time", "Semisonic", "Alt Rock")
        self.song_2 = Song("Romeo and Juliet", "Dire Straits", "Rock")
        self.song_3 = Song("Thank You For the Music", "ABBA", "Pop")
        self.song_4 = Song("I Miss You", "Blink-182", "Pop-Punk")
        song_catalogue = [self.song_1, self.song_2, self.song_3, self.song_4]
        
        self.room_1 = Room("Jungle Room", 5, 50.00, song_catalogue)
        self.room_2 = Room("Disco Room", 10, 100.00, song_catalogue)
        self.room_3 = Room("Outer Space Room", 3, 30.00, song_catalogue)

        self.guest_1 = Guest("Gavin", 35, "Closing Time", 50.00)
        self.guest_2 = Guest("Ailsa", 27, "Romeo and Juliet", 45.00)
        self.guest_3 = Guest("Stewart", 32, "Don't Think Twice, It's Alright", 55.00)
        self.guest_4 = Guest("Karissa", 27, "Super Trouper", 48.00)
        self.guest_5 = Guest("Isla", 28, "Oops! I Did it Again", 52.00)
        self.guest_6 = Guest("Kirsty", 16, "What's My Age Again?", 25.00)

        self.drink_1 = Drink("Cocktail Pitcher", 12.00)
        self.drink_2 = Drink("Punk IPA", 5.00)

    def test_room_has_name(self):
        self.assertEqual("Jungle Room", self.room_1.name)
    
    def test_room_has_max_capacity(self):
        self.assertEqual(5, self.room_1.max_capacity)

    def test_guest_list_starts_empty(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_song_queue_starts_empty(self):
        self.assertEqual(0, self.room_1.song_count())

    def test_check_in_guest(self):
        self.room_3.check_in_guest(self.guest_1)
        self.room_3.check_in_guest(self.guest_2)
        self.room_3.check_in_guest(self.guest_3)
        too_full = self.room_3.check_in_guest(self.guest_4)
        too_young = self.room_1.check_in_guest(self.guest_6)
        self.assertEqual("Sorry! This room is full!", too_full)
        self.assertEqual(3, self.room_3.guest_count())
        self.assertEqual("Sorry! You have to be at least 18 to come in.", too_young)

    def test_check_in_group(self):
        group_1 = [
            self.guest_1, 
            self.guest_2, 
            self.guest_3, 
            self.guest_4, 
            self.guest_5
            ]

        self.room_1.check_in_group(group_1)
        self.assertEqual(5, self.room_1.guest_count())

    def test_capacity_reached(self):
        self.room_3.check_in_guest(self.guest_1)
        self.room_3.check_in_guest(self.guest_2)
        self.room_3.check_in_guest(self.guest_3)
        self.room_3.check_in_guest(self.guest_4)
        self.assertEqual("Sorry! This room is full!", self.room_3.capacity_reached())
    

    def test_charge_guest_for_room_share(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.room_1.check_in_guest(self.guest_5)

        self.guest_1.order_drink(self.drink_2)
        self.guest_2.order_drink(self.drink_2)
        self.guest_3.order_drink(self.drink_2)
        self.guest_4.order_drink(self.drink_2)
        self.room_1.charge_for_room_share(self.guest_1)
        self.room_1.charge_for_room_share(self.guest_2)
        self.room_1.charge_for_room_share(self.guest_3)
        self.assertEqual(35, self.guest_1.wallet)
        self.assertEqual(30, self.guest_2.wallet)
        self.assertEqual(40, self.guest_3.wallet)
        

    def test_check_out_guests(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.guest_1.order_drink(self.drink_2)
        self.room_1.check_out_guests(self.guest_1)
        self.room_1.check_out_guests(self.guest_2)
        self.assertEqual(20, self.guest_1.wallet)
        self.assertEqual(20, self.guest_2.wallet)
        self.assertEqual(0, self.room_1.guest_count())

    