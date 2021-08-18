import unittest

import bread as bread

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water


class BakeryTests(unittest.TestCase):
    def setUp(self):
        self.bakery = Bakery("Bakery")

    def test_init(self):
        self.assertEqual(self.bakery.name, "Bakery")
        self.assertEqual(self.bakery.food_menu, [])
        self.assertEqual(self.bakery.drinks_menu, [])
        self.assertEqual(self.bakery.tables_repository, [])
        self.assertEqual(self.bakery.total_income, 0)

    def test_name_empty_string_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.bakery.name = ""

        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_name_space_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.bakery.name = " "

        self.assertEqual("Name cannot be empty string or white space!", str(ex.exception))

    def test_add_food_type_bread(self):
        food_type = "Bread"
        name = "Name"
        price = 2
        actual = self.bakery.add_food(food_type, name, price)
        bread = Bread(name, price)
        self.assertEqual(len(self.bakery.food_menu), 1)
        self.assertEqual(actual, f"Added {name} ({food_type}) to the food menu")

    def test_add_food_type_cake(self):
        food_type = "Cake"
        name = "Name"
        price = 2
        actual = self.bakery.add_food(food_type, name, price)
        cake = Cake(name, price)
        self.assertEqual(len(self.bakery.food_menu), 1)
        self.assertEqual(actual, f"Added {name} ({food_type}) to the food menu")

    def test_add_food_when_in_exception(self):
        food_type = "Cake"
        name = "Name"
        price = 2
        cake = Cake(name, price)
        self.bakery.food_menu.append(cake)
        with self.assertRaises(Exception) as ex:
            self.bakery.add_food(food_type, name, price)
        self.assertEqual(f"{food_type} {name} is already in the menu!", str(ex.exception))

    def test_add_drink_type_tea(self):
        drink_type = "Tea"
        name = "Tea"
        portion = 200
        brand = "Ahmad"
        actual = self.bakery.add_drink(drink_type, name, portion, brand)
        tea = Tea(name, portion, brand)
        self.assertEqual(len(self.bakery.drinks_menu), 1)
        self.assertEqual(actual, f"Added {name} ({brand}) to the drink menu")

    def test_add_drink_type_water(self):
        drink_type = "Water"
        name = "Water"
        portion = 200
        brand = "Devin"
        actual = self.bakery.add_drink(drink_type, name, portion, brand)
        water = Water(name, portion, brand)
        self.assertEqual(len(self.bakery.drinks_menu), 1)
        self.assertEqual(actual, f"Added {name} ({brand}) to the drink menu")


