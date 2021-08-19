import unittest

from project.baked_food.bread import Bread


class BreadTests(unittest.TestCase):
    def setUp(self):
        self.bread = Bread("Bread", 10)

    def test_init(self):
        self.assertEqual(self.bread.name, "Bread")
        self.assertEqual(self.bread.portion, 200)
        self.assertEqual(self.bread.price, 10)
    def test_name_space_exception(self):
        with self.assertRaises(ValueError) as ex:
            bread_1 = Bread(" ", 1)
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_name_empty_str_exception(self):
        with self.assertRaises(ValueError) as ex:
            bread_1 = Bread("", 1)
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_name_price_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            bread_1 = Bread("Bread", 0)
        self.assertEqual("Price cannot be less than or equal to zero!", str(ex.exception))

    def test_name_price_less_than_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            bread_1 = Bread("Bread", -10)
        self.assertEqual("Price cannot be less than or equal to zero!", str(ex.exception))

    def test_repr_method(self):
        self.assertEqual(self.bread.__repr__(), f" - {self.bread.name}: {self.bread.portion:.2f}g - {self.bread.price:.2f}lv")