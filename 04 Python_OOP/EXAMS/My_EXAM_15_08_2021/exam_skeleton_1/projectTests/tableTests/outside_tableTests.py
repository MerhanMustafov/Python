import unittest

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.outside_table import OutsideTable


class InsideTableTests(unittest.TestCase):
    def setUp(self):
        self.outside_table = OutsideTable(51, 3)

    def test_init(self):
        self.assertEqual(self.outside_table.table_number, 51)
        self.assertEqual(self.outside_table.capacity, 3)

        self.assertEqual(self.outside_table.food_orders, [])
        self.assertEqual(self.outside_table.drink_orders, [])
        self.assertEqual(self.outside_table.number_of_people, 0)
        self.assertEqual(self.outside_table.is_reserved, False)

    def test_table_number_less_than_1_exception(self):
        with self.assertRaises(ValueError) as ex:
            outsise_table_two = OutsideTable(50, 3)
        self.assertEqual("Outside table's number must be between 51 and 100 inclusive!", str(ex.exception))

    def test_table_number_more_than_50_exception(self):
        with self.assertRaises(ValueError) as ex:
            outsise_table_two = OutsideTable(101, 3)
        self.assertEqual("Outside table's number must be between 51 and 100 inclusive!", str(ex.exception))

    def test_reserve_method(self):
        number_of_people = 3
        self.outside_table.reserve(number_of_people)
        self.assertEqual(self.outside_table.number_of_people, 3)
        self.assertEqual(self.outside_table.is_reserved, True)

    def test_reseve_mothod_with_more_peple_than_the_capacity(self):
        number_of_people_1 = 4
        self.outside_table.reserve(number_of_people_1)
        self.assertLessEqual(self.outside_table.number_of_people, self.outside_table.capacity)

    def test_order_food_bread_method(self):
        food = Bread("Bread", 2)
        self.outside_table.order_food(food)
        self.assertEqual(self.outside_table.food_orders, [food])

    def test_order_food_cake_method(self):
        food = Cake("Cake", 2)
        self.outside_table.order_food(food)
        self.assertEqual(self.outside_table.food_orders, [food])

    def test_order_drink_tea_method(self):
        drink = Tea("Black", 50, "Ahmad")
        self.outside_table.order_drink(drink)
        self.assertEqual(self.outside_table.drink_orders, [drink])

    def test_order_drink_water_method(self):
        drink = Water("Natural", 200, "Devin")
        self.outside_table.order_drink(drink)
        self.assertEqual(self.outside_table.drink_orders, [drink])

    def test_get_bill_method(self):
        food = Bread("Bread", 2)
        self.outside_table.order_food(food)
        food = Cake("Cake", 2)
        self.outside_table.order_food(food)

        drink = Tea("Black", 50, "Ahmad")
        self.outside_table.order_drink(drink)
        drink = Water("Natural", 200, "Devin")
        self.outside_table.order_drink(drink)

        actual = self.outside_table.get_bill()
        self.assertEqual(actual, 8.00)

    def test_clear_method(self):
        self.outside_table.reserve(2)
        self.assertEqual(self.outside_table.is_reserved, True)
        self.assertEqual(self.outside_table.number_of_people, 2)

        food = Bread("Bread", 2)
        self.outside_table.order_food(food)
        food = Cake("Cake", 2)
        self.outside_table.order_food(food)

        drink = Tea("Black", 50, "Ahmad")
        self.outside_table.order_drink(drink)
        drink = Water("Natural", 200, "Devin")
        self.outside_table.order_drink(drink)

        self.outside_table.clear()
        self.assertEqual(self.outside_table.food_orders, [])
        self.assertEqual(self.outside_table.drink_orders, [])
        self.assertEqual(self.outside_table.is_reserved, False)
        self.assertEqual(self.outside_table.number_of_people, 0)

    def test_free_table_method(self):
        actual = self.outside_table.free_table_info()
        self.assertEqual(actual, f"Table: {self.outside_table.table_number}\n"
                                 f"Type: {self.outside_table.__class__.__name__}\n"
                                 f"Capacity: {self.outside_table.capacity}")

