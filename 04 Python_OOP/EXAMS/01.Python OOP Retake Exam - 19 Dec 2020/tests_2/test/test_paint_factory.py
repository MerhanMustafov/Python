import unittest
from project.factory.paint_factory import PaintFactory

class PaintFactoryTests(unittest.TestCase):
    def setUp(self):
        self.paint_f = PaintFactory("Name", 50)

    def test_init(self):
        self.assertEqual(self.paint_f.name, "Name")
        self.assertEqual(self.paint_f.capacity, 50)
        self.assertEqual(self.paint_f.ingredients, {})
        self.assertEqual(self.paint_f.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient_when_not_in_exception(self):
        product_type = "black"
        with self.assertRaises(TypeError) as ex:
            self.paint_f.add_ingredient(product_type, 10)
        self.assertEqual(f"Ingredient of type {product_type} not allowed in {self.paint_f.__class__.__name__}", str(ex.exception))

    def test_add_to_ingredient_value_error(self):
        product_type = "white"
        with self.assertRaises(ValueError) as ex:
            self.paint_f.add_ingredient(product_type, 100)
        self.assertEqual("Not enough space in factory", str(ex.exception))


    def test_add_to_ingredient(self):
        product_type = "white"
        self.paint_f.add_ingredient(product_type, 10)
        self.assertEqual(self.paint_f.ingredients, {"white": 10})


    def test_remove_ingredient_exception(self):
        product_type = "black"
        with self.assertRaises(KeyError) as ex:
            self.paint_f.remove_ingredient(product_type, 10)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient(self):
        self.paint_f.ingredients = {"white": 10}
        product_type = "white"
        self.paint_f.remove_ingredient(product_type, 0)
        self.assertEqual(self.paint_f.ingredients, {"white": 10})

    def test_remove_ingredient_exception_value_error(self):
        self.paint_f.ingredients = {"white": 10}
        product_type = "white"
        with self.assertRaises(ValueError) as ex:
            self.paint_f.remove_ingredient(product_type, 11)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_product_property(self):
        self.assertEqual(self.paint_f.products, self.paint_f.ingredients)