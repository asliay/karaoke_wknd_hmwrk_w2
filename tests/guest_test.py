import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Gavin", 35, "Closing Time", 50.00)
        self.guest_2 = Guest("Ailsa", 27, "Romeo and Juliet", 45.00)
        self.guest_3 = Guest("Stewart", 32, "Just Dropped In (To See What Condition My Condition Was In)", 55.00)
        self.guest_4 = Guest("Karissa", 27, "Super Trouper", 48.00)
        self.guest_5 = Guest("Isla", 28, "Oops! I Did it Again", 52.00)
        self.guest_6 = Guest("Kirsty", 16, "What's My Age Again?", 25.00)


        self.song_1 = Song("Closing Time", "Semisonic", "Alt Rock")
        self.song_2 = Song("Romeo and Juliet", "Dire Straits", "Rock")
        self.song_3 = Song("Thank You For the Music", "ABBA", "Pop")
        room_songs = {self.song_1, self.song_2, self.song_3}
        
        self.room_1 = Room("Jungle Room", 5, 50.00, room_songs)
        
        self.drink_1 = Drink("Cocktail Pitcher", 12.00)
        self.drink_2 = Drink("Punk IPA", 5.00)

    def test_customer_has_name(self):
        self.assertEqual("Gavin", self.guest_1.name)

    def test_customer_has_favourite_song(self):
        self.assertEqual("Closing Time", self.guest_1.favourite_song)

    def test_customer_has_cash(self):
        self.assertEqual(50.00, self.guest_1.wallet)

    def test_tab_starts_at_0(self):
        self.assertEqual(0, self.guest_1.drink_tab)

    def test_remove_cash(self):
        self.guest_1.remove_cash(25)
        self.assertEqual(25, self.guest_1.wallet)
    
    def test_add_to_tab(self):
        self.guest_1.add_to_tab(12)
        self.assertEqual(12, self.guest_1.drink_tab)

    def test_order_drink(self):
        self.guest_2.order_drink(self.drink_1)
        self.guest_2.order_drink(self.drink_2)
        self.guest_6.order_drink(self.drink_2)
        self.assertEqual(17, self.guest_2.drink_tab)

    def test_settle_drink_tab(self):
        self.guest_2.order_drink(self.drink_1)
        self.guest_2.order_drink(self.drink_2)
        self.guest_2.settle_drink_tab()
        self.assertEqual(28, self.guest_2.wallet)

    

    


