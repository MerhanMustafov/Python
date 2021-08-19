import unittest

from project.drink.water import Water


class TeaTests(unittest.TestCase):
    def setUp(self):
        self.water = Water("Natural", 50, "Devin")

    def test_init(self):
        self.assertEqual(self.water.name, "Natural")
        self.assertEqual(self.water.portion, 50)
        self.assertEqual(self.water.price, 1.50)
        self.assertEqual(self.water.brand, "Devin")
    def test_name_space_exception(self):
        with self.assertRaises(ValueError) as ex:
            water = Water(" ", 200, "Devin")
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_name_empty_str_exception(self):
        with self.assertRaises(ValueError) as ex:
            water = Water("", 200, "Devin")
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_portion_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            water = Water("Natural", 0, "Devin")
        self.assertEqual("Portion cannot be less than or equal to zero!", str(ex.exception))

    def test_portion_less_than_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            water = Water("Natural", -1, "Devin")
        self.assertEqual("Portion cannot be less than or equal to zero!", str(ex.exception))

    def test_brand_space_exception(self):
        with self.assertRaises(ValueError) as ex:
            water = Water("Natural", 200, " ")
        self.assertEqual("Brand cannot be empty string or white space!", str(ex.exception))

    def test_brand_empty_str_exception(self):
        with self.assertRaises(ValueError) as ex:
            water = Water("Natural", 200, "")
        self.assertEqual("Brand cannot be empty string or white space!", str(ex.exception))


    def test_repr_method(self):
        self.assertEqual(self.water.__repr__(), f" - {self.water.name} {self.water.brand} - {self.water.portion:.2f}ml - {self.water.price:.2f}lv")