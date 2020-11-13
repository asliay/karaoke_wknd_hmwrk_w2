import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Gavin", 50)

    def test_customer_has_name(self):
        self.assertEqual("Gavin", self.guest.name)

    def test_customer_has_cash(self):
        self.assertEqual(50, self.guest.cash)