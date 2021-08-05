# from project.drink import Drink
# from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)
    def find(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                return product
    def remove(self, product_name):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)

    def __repr__(self):
        result = ""
        new_line = "\n"
        for product in self.products:
            if self.products.index(product) == len(self.products)-1:
                result += str(product)
                return result
            result += str(product) + new_line

# food = Food("Banana")
# smooty = Drink("Smooty")
# p_rep = ProductRepository([])
# p_rep.add(food)
# p_rep.add(smooty)
# print(p_rep)


# import unittest
#
# from project.drink import Drink
# from project.food import Food
# from project.product import Product
# # from project.product_repository import ProductRepository
#
#
# class Tests(unittest.TestCase):
#     def setUp(self):
#         self.product = Product('product', 150)
#         self.drink = Drink('drink')
#         self.food = Food('food')
#         self.repo = ProductRepository()
#
#     def test_init_of_product(self):
#         self.assertEqual(self.product.name, 'product')
#         self.assertEqual(self.product.quantity, 150)
#
#     def test_decrease_product(self):
#         self.product.decrease(10)
#         self.assertEqual(self.product.quantity, 140)
#
#     def test_increase_product(self):
#         self.product.increase(10)
#         self.assertEqual(self.product.quantity, 160)
#
#     def test_drink_init(self):
#         self.assertEqual(self.drink.name, 'drink')
#         self.assertEqual(self.drink.quantity, 10)
#         self.assertEqual(self.drink.__class__.__base__.__name__, 'Product')
#
#     def test_decrease_drink(self):
#         self.drink.decrease(10)
#         self.assertEqual(self.drink.quantity, 0)
#
#     def test_increase_drink(self):
#         self.drink.increase(10)
#         self.assertEqual(self.drink.quantity, 20)
#
#     def test_food_init(self):
#         self.assertEqual(self.food.name, 'food')
#         self.assertEqual(self.food.quantity, 15)
#         self.assertEqual(self.food.__class__.__base__.__name__, 'Product')
#
#     def test_decrease_food(self):
#         self.food.decrease(10)
#         self.assertEqual(self.food.quantity, 5)
#
#     def test_increase_food(self):
#         self.food.increase(10)
#         self.assertEqual(self.food.quantity, 25)
#
#     def test_init_repo(self):
#         self.assertEqual(self.repo.products, [])
#
#     def test_repo_add(self):
#         self.repo.add(self.food)
#         self.repo.add(self.drink)
#         self.assertEqual(len(self.repo.products), 2)
#         self.assertEqual(self.repo.products[0], self.food)
#         self.assertEqual(self.repo.products[1], self.drink)
#
#     def test_repo_remove(self):
#         self.repo.products = [self.drink, self.food]
#         self.repo.remove('drink')
#         self.assertEqual(self.repo.products[0], self.food)
#         self.repo.remove('drink')
#         self.assertEqual(self.repo.products[0], self.food)
#
#     def test_repo_repr(self):
#         self.repo.add(self.food)
#         self.repo.add(self.drink)
#         actual = str(self.repo)
#         expected = 'food: 15\ndrink: 10'
#         self.assertEqual(expected, actual)
#
#
# if __name__ == "__main__":
#    unittest.main()
