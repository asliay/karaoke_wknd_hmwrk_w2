import unittest

from classes.drink import Drink
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Cocktail Pitcher", 12.00)

    def test_drink_has_name(self):
        self.assertEqual("Cocktail Pitcher", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(12.00, self.drink.price)