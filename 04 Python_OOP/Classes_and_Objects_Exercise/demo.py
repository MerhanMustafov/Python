# class Example:
#     x = ["aaaaaa"]
#     def __init__(self):
#         pass
#
# example = Example()
# example_2 = Example
# example.x.append("bbbbbbbbbbbb")
# print(example.x)
# print(example_2.x)
# example.x = "bbbbb"
# print(example.x)
# print(example_2.x)
# print(example.x)



# def ingredient_in(self, ingredients, ingredient):
#     for key, value in self.ingredients.items():
#         if key == ingredient:
#             return True
#     return False
# class PizzaDelivery:
#     ordered = False
#     def __init__(self, name, price: float, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#
#     def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
#         # if self.ordered:
#         #     return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         # if ingredient in self.ingredients and not self.ordered:
#         #     self.ingredients[ingredient] += quantity
#         #     self.price += price_per_ingredient * quantity
#         # elif ingredient not in self.ingredients and not self.ordered:
#         #     self.ingredients[ingredient] = quantity
#         #     self.price += price_per_ingredient * quantity
#         # if self.ordered:
#         #     return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient_in(self, self.ingredients, ingredient) and not PizzaDelivery.ordered:
#             self.ingredients[ingredient] += quantity
#             self.price += price_per_ingredient*quantity
#         elif not ingredient_in(self, self.ingredients, ingredient) and not PizzaDelivery.ordered:
#             self.ingredients[ingredient] = quantity
#             self.price += price_per_ingredient*quantity
#         if PizzaDelivery.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#     def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
#         # if self.ordered:
#         #     return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         # if ingredient not in self.ingredients and not self.ordered:
#         #     return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#         # elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
#         #     return f"Please check again the desired quantity of {ingredient}!"
#         # else:
#         #     self.ingredients[ingredient] -= quantity
#         #     self.price -= price_per_ingredient * quantity
#         if ingredient_in(self, self.ingredients, ingredient):
#             if not quantity > self.ingredients[ingredient]:
#                 self.ingredients[ingredient] -= quantity
#                 self.price -= price_per_ingredient * quantity
#             else:
#                 return f"Please check again the desired quantity of {ingredient}!"
#         elif not ingredient_in(self, self.ingredients, ingredient):
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#
#     def make_order(self):
        # self.ordered = True
        #
        # ingredients_and_quantity = {f'{ingred}: {quantity}'for ingred, quantity in self.ingredients.items()}
        #
        # return f"You've ordered pizza {self.name} " \
        #     f"prepared with {', '.join(ingredients_and_quantity)}" \
        #     f" and the price will be {self.price}lv."
        # PizzaDelivery.ordered = True
        # str_ingtedients = []
        # for k, v in self.ingredients.items():
        #     str_ingtedients.append(f'{k}: {v}')
        # return f"You've ordered pizza {self.name} prepared with {', '.join(str_ingtedients)} and the price will be {self.price}lv."
# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))

# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         self.assertEqual(t.name, 'Margarita')
#         self.assertEqual(t.price, 12)
#         self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1})
#         self.assertEqual(t.ordered, False)
#
#     def test_add_extra_with_available_ingredient_should_increase_the_quantity(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         t.add_extra('cheese', 1, 2)
#         self.assertEqual(t.ingredients, {'cheese': 3, 'tomatoes': 1})
#         self.assertEqual(t.price, 14)
#
#     def test_add_extra_with_new_ingredient_should_add_the_quantity(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         t.add_extra('mozzarella', 1, 2.5)
#         self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1, 'mozzarella': 1})
#         self.assertEqual(t.price, 14.5)
#
#     def test_remove_ingredients_not_included_in_pizza_should_return_message(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         message = t.remove_ingredient('bacon', 1, 5)
#         self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1})
#         self.assertEqual(message, 'Wrong ingredient selected! We do not use bacon in Margarita!')
#
#     def test_remove_ingredients_with_quantity_higher_than_what_we_have_should_return_message(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         message = t.remove_ingredient('tomatoes', 2, 2)
#         self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1})
#         self.assertEqual(message, 'Please check again the desired quantity of tomatoes!')
#
#     def test_remove_ingredients_with_quantity_equal_to_what_we_have_should_remove_the_ingredient(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         t.remove_ingredient('tomatoes', 1, 2)
#         self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 0})
#         self.assertEqual(t.price, 10)
#
#     def test_pizza_ordered(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         result = t.make_order()
#         self.assertEqual(t.ordered, True)
#         self.assertEqual(result,
#                          "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.")
#
#     def test_add_extra_after_pizza_is_ordered_should_return_message(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         order = t.make_order()
#         result = t.add_extra('mozzarella', 1, 2)
#         self.assertEqual(order,
#                          "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.")
#         self.assertEqual(result, "Pizza Margarita already prepared, and we can't make any changes!")
#
#     def test_remove_ingredient_after_pizza_is_ordered_should_return_message(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
#         order = t.make_order()
#         result = t.remove_ingredient('mozzarella', 1, 2)
#         self.assertEqual(order,
#                          "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.")
#         self.assertEqual(result, "Pizza Margarita already prepared, and we can't make any changes!")
#
#
# if __name__ == "__main__":
#     unittest.main()
# class Account:
#     def __init__(self, id, name, balance = 0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return  self.balance
#         return f"Amount exceeded balance"
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"
#
# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())
# print("*"*20)
# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())




# class Vet:
#     animals = []
#     space = 5
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def register_animal(self, animal_name):
#         if len(Vet.animals) < self.space:
#             self.animals.append(animal_name)
#             Vet.animals.append(animal_name)
#             return f"{animal_name} registered in the clinic"
#         return "Not enough space"
#     def unregister_animal(self, animal_name):
#         if animal_name in Vet.animals:
#             self.animals.remove(animal_name)
#             Vet.animals.remove(animal_name)
#             return f"{animal_name} unregistered successfully"
#         return f"{animal_name} not in the clinic"
#     def info(self):
#         return f"{self.name} has {len(self.animals)} animals. {self.space - len(Vet.animals)} space left in clinic"
#
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())
