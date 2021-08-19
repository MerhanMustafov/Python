import unittest

from project.baked_food.cake import Cake


class CakeTests(unittest.TestCase):
    def setUp(self):
        self.cake = Cake("Cake", 10)

    def test_init(self):
        self.assertEqual(self.cake.name, "Cake")
        self.assertEqual(self.cake.portion, 245)
        self.assertEqual(self.cake.price, 10)
    def test_name_space_exception(self):
        with self.assertRaises(ValueError) as ex:
            cake_1 = Cake(" ", 1)
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_name_empty_str_exception(self):
        with self.assertRaises(ValueError) as ex:
            cake_1 = Cake("", 1)
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_name_price_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            cake_1 = Cake("Cake", 0)
        self.assertEqual("Price cannot be less than or equal to zero!", str(ex.exception))

    def test_name_price_less_than_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            cake_1 = Cake("Cake", -10)
        self.assertEqual("Price cannot be less than or equal to zero!", str(ex.exception))

    def test_repr_method(self):
        self.assertEqual(self.cake.__repr__(), f" - {self.cake.name}: {self.cake.portion:.2f}g - {self.cake.price:.2f}lv")