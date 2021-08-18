import unittest

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable


class InsideTableTests(unittest.TestCase):
    def setUp(self):
        self.inside_table = InsideTable(1, 3)

    def test_init(self):
        self.assertEqual(self.inside_table.table_number, 1)
        self.assertEqual(self.inside_table.capacity, 3)

        self.assertEqual(self.inside_table.food_orders, [])
        self.assertEqual(self.inside_table.drink_orders, [])
        self.assertEqual(self.inside_table.number_of_people, 0)
        self.assertEqual(self.inside_table.is_reserved, False)

    def test_table_number_less_than_1_exception(self):
        with self.assertRaises(ValueError) as ex:
            inside_table_two = InsideTable(0, 3)
        self.assertEqual("Inside table's number must be between 1 and 50 inclusive!", str(ex.exception))

    def test_table_number_more_than_50_exception(self):
        with self.assertRaises(ValueError) as ex:
            inside_table_two = InsideTable(51, 3)
        self.assertEqual("Inside table's number must be between 1 and 50 inclusive!", str(ex.exception))

    def test_reserve_method(self):
        number_of_people = 3
        self.inside_table.reserve(number_of_people)
        self.assertEqual(self.inside_table.number_of_people, 3)
        self.assertEqual(self.inside_table.is_reserved, True)

    def test_reseve_mothod_with_more_peple_than_the_capacity(self):
        number_of_people_1 = 4
        self.inside_table.reserve(number_of_people_1)
        self.assertLessEqual(self.inside_table.number_of_people, self.inside_table.capacity)

    def test_order_food_bread_method(self):
        food = Bread("Bread", 2)
        self.inside_table.order_food(food)
        self.assertEqual(self.inside_table.food_orders, [food])

    def test_order_food_cake_method(self):
        food = Cake("Cake", 2)
        self.inside_table.order_food(food)
        self.assertEqual(self.inside_table.food_orders, [food])


    def test_order_drink_tea_method(self):
        drink = Tea("Black", 50, "Ahmad")
        self.inside_table.order_drink(drink)
        self.assertEqual(self.inside_table.drink_orders, [drink])

    def test_order_drink_water_method(self):
        drink = Water("Natural", 200, "Devin")
        self.inside_table.order_drink(drink)
        self.assertEqual(self.inside_table.drink_orders, [drink])

    def test_get_bill_method(self):
        food = Bread("Bread", 2)
        self.inside_table.order_food(food)
        food = Cake("Cake", 2)
        self.inside_table.order_food(food)

        drink = Tea("Black", 50, "Ahmad")
        self.inside_table.order_drink(drink)
        drink = Water("Natural", 200, "Devin")
        self.inside_table.order_drink(drink)

        actual = self.inside_table.get_bill()
        self.assertEqual(actual, 8.00)

    def test_clear_method(self):
        self.inside_table.reserve(2)
        self.assertEqual(self.inside_table.is_reserved, True)
        self.assertEqual(self.inside_table.number_of_people, 2)

        food = Bread("Bread", 2)
        self.inside_table.order_food(food)
        food = Cake("Cake", 2)
        self.inside_table.order_food(food)

        drink = Tea("Black", 50, "Ahmad")
        self.inside_table.order_drink(drink)
        drink = Water("Natural", 200, "Devin")
        self.inside_table.order_drink(drink)

        self.inside_table.clear()
        self.assertEqual(self.inside_table.food_orders, [])
        self.assertEqual(self.inside_table.drink_orders, [])
        self.assertEqual(self.inside_table.is_reserved, False)
        self.assertEqual(self.inside_table.number_of_people, 0)

    def test_free_table_method(self):
        actual = self.inside_table.free_table_info()
        self.assertEqual(actual, f"Table: {self.inside_table.table_number}\n"
                                f"Type: {self.inside_table.__class__.__name__}\n"
                                f"Capacity: {self.inside_table.capacity}")

