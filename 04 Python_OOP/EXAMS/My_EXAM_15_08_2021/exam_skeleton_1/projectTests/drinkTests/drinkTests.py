import unittest

from project.drink.drink import Drink


class DrinkTests(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError) as ex:
            baked_food = Drink("Drink", 200, 5, "Coke")
        self.assertEqual("Can't instantiate abstract class Drink with abstract methods __init__", str(ex.exception))