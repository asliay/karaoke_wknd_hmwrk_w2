import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Gavin", 35, 50.00)
        self.guest_2 = Guest("Ailsa", 27, 45.00)
        self.guest_3 = Guest("Stewart", 32, 55.00)
        self.guest_4 = Guest("Karissa", 27, 48.00)
        self.guest_5 = Guest("Isla", 28, 52.00)

        self.room_1 = Room("Jungle Room", 5, 50.00)

    def test_customer_has_name(self):
        self.assertEqual("Gavin", self.guest_1.name)

    def test_customer_has_cash(self):
        self.assertEqual(50.00, self.guest_1.cash)

    def test_guest_pay_for_room(self):
        self.guest_1.guest_pay_for_room(self.room_1)
        self.assertEqual(0, self.guest_1.cash)

    


