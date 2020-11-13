import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Gavin", 35, 50.00)
        self.guest_2 = Guest("Ailsa", 27, 45.00)
        self.guest_3 = Guest("Stewart", 32, 55.00)
        self.guest_4 = Guest("Karissa", 27, 48.00)
        self.guest_5 = Guest("Isla", 28, 52.00)

        self.room_1 = Room("Jungle Room", 5, 50.00)
        self.drink_1 = Drink("Cocktail Pitcher", 12.00)

    def test_customer_has_name(self):
        self.assertEqual("Gavin", self.guest_1.name)

    def test_customer_has_cash(self):
        self.assertEqual(50.00, self.guest_1.wallet)

    def test_bill_starts_at_0(self):
        self.assertEqual(0, self.guest_1.bill)

    def test_remove_cash(self):
        self.guest_1.remove_cash(25)
        self.assertEqual(25, self.guest_1.wallet)
    
    def test_add_to_bill(self):
        self.guest_1.add_to_bill(12)
        self.assertEqual(12, self.guest_1.bill)

    def test_buy_drink(self):
        self.guest_2.buy_drink(self.drink_1)
        self.assertEqual(33, self.guest_2.wallet)


