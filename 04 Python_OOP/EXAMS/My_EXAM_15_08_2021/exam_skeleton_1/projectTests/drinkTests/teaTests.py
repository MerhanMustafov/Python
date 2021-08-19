import unittest

from project.drink.tea import Tea


class TeaTests(unittest.TestCase):
    def setUp(self):
        self.tea = Tea("Black", 50, "Ahmad")

    def test_init(self):
        self.assertEqual(self.tea.name, "Black")
        self.assertEqual(self.tea.portion, 50)
        self.assertEqual(self.tea.price, 2.50)
        self.assertEqual(self.tea.brand, "Ahmad")
    def test_name_space_exception(self):
        with self.assertRaises(ValueError) as ex:
            tea_1 = Tea(" ", 50, "Ahmad")
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_name_empty_str_exception(self):
        with self.assertRaises(ValueError) as ex:
            tea_1 = Tea("", 50, "Ahmad")
        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_portion_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            tea_1 = Tea("Black", 0, "Ahmad")
        self.assertEqual("Portion cannot be less than or equal to zero!", str(ex.exception))

    def test_portion_less_than_0_exception(self):
        with self.assertRaises(ValueError) as ex:
            tea_1 = Tea("Black", -1, "Ahmad")
        self.assertEqual("Portion cannot be less than or equal to zero!", str(ex.exception))

    def test_brand_space_exception(self):
        with self.assertRaises(ValueError) as ex:
            tea_1 = Tea("Black", 50, " ")
        self.assertEqual("Brand cannot be empty string or white space!", str(ex.exception))

    def test_brand_empty_str_exception(self):
        with self.assertRaises(ValueError) as ex:
            tea_1 = Tea("Black", 50, "")
        self.assertEqual("Brand cannot be empty string or white space!", str(ex.exception))


    def test_repr_method(self):
        self.assertEqual(self.tea.__repr__(), f" - {self.tea.name} {self.tea.brand} - {self.tea.portion:.2f}ml - {self.tea.price:.2f}lv")