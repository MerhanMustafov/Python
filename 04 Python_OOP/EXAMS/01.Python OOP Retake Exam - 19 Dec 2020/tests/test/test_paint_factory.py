import unittest

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):
    def setUp(self):
        self.paint_f = PaintFactory("Art", 100)
        self.paint_f.ingredients = {}

    def test_init(self):
        self.assertEqual(self.paint_f.name, "Art")
        self.assertEqual(self.paint_f.capacity, 100)
        self.assertEqual(self.paint_f.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.paint_f.ingredients, {})

    def test_add_ingredient_product_not_in_exception(self):
        product = "black"
        with self.assertRaises(TypeError) as ex:
            self.paint_f.add_ingredient(product, 2)
        self.assertEqual(f"Ingredient of type {product} not allowed in PaintFactory", str(ex.exception))

    def test_can_not_add_exception(self):
        product = "white"
        with self.assertRaises(ValueError) as ex:
            self.paint_f.add_ingredient(product, 101)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_can_add(self):
        product = "white"
        self.paint_f.add_ingredient(product, 2)
        self.assertEqual(self.paint_f.ingredients, {"white": 2})

    def test_remove_ingredient_when_not_in_exception(self):
        product_type = "black"
        with self.assertRaises(KeyError) as ex:
            self.paint_f.remove_ingredient(product_type, 2)
        self.assertEqual(f"'No such ingredient in the factory'", str(ex.exception))
    def test_remove_ingredient_when_in(self):
        product_type = "black"
        self.paint_f.ingredients = {"black": 2}
        self.paint_f.remove_ingredient(product_type, 1)
        self.assertEqual(self.paint_f.ingredients, {"black": 1})

    def test_remove_ingredient_when_in_but_less_than_zero_exception(self):
        product_type = "black"
        self.paint_f.ingredients = {"black": 2}
        with self.assertRaises(ValueError) as ex:
            self.paint_f.remove_ingredient(product_type, 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))
    # def test_product_property(self):
    #     self.paint_f.ingredients = {"black": 2}
    #     self.assertEqual(self.paint_f.products, {"black": 2})

if __name__ == "__main__":
    unittest.main()