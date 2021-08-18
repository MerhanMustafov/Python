import unittest

from project.baked_food.baked_food import BakedFood


class BakedFoodTests(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError) as ex:
            baked_food = BakedFood("BakedFood", 100, 50)
        self.assertEqual("Can't instantiate abstract class BakedFood with abstract methods __init__", str(ex.exception))