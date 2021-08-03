from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name:str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value



    def add_topping(self, topping: Topping):
        if topping.topping_type in self.toppings:
            if not self.toppings[topping.topping_type] + topping.weight > self.__toppings_capacity:
                self.toppings[topping.topping_type] += topping.weight
            else:
                raise ValueError("Not enough space for another topping")
        else:
            self.toppings[topping.topping_type] = topping.weight




    def calculate_total_weight(self):
        total_pizza_weight = 0
        for key, value in self.toppings.items():
            total_pizza_weight += value

        total_pizza_weight += self.__dough.weight
        return total_pizza_weight

# from project.dough import Dough
# from project.pizza import Pizza
# from project.topping import Topping

#
# tomato_topping = Topping("Tomato", 60)
# print(tomato_topping.topping_type)
# print(tomato_topping.weight)
#
# mushrooms_topping = Topping("Mushroom", 75)
# print(mushrooms_topping.topping_type)
# print(mushrooms_topping.weight)
#
# mozzarella_topping = Topping("Mozzarella", 80)
# print(mozzarella_topping.topping_type)
# print(mozzarella_topping.weight)
#
# cheddar_topping = Topping("Cheddar", 150)
#
# pepperoni_topping = Topping("Pepperoni", 120)
#
# white_flour_dough = Dough("White Flour", "Mixing", 200)
# print(white_flour_dough.flour_type)
# print(white_flour_dough.weight)
# print(white_flour_dough.baking_technique)
#
# whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
# print(whole_wheat_dough.weight)
# print(whole_wheat_dough.flour_type)
# print(whole_wheat_dough.baking_technique)
#
# p = Pizza("Margherita", whole_wheat_dough, 2)
#
# p.add_topping(tomato_topping)
# print(p.calculate_total_weight())
#
# p.add_topping(mozzarella_topping)
# print(p.calculate_total_weight())
#
# p.add_topping(mozzarella_topping)





















# from project.topping import Topping
# from project.dough import Dough
#
# class Pizza:
#     def __init__(self, name: str, dough, toppings_capacity: int, toppings = {}):
#         self.name = name
#         self.dough = dough
#         self.toppings_capacity = toppings_capacity
#         self.toppings = {}
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, n):
#         if n == "":
#             raise ValueError("The name cannot be an empty string")
#         self.__name = n
#
#     @property
#     def dough(self):
#         return self.__dough
#     @dough.setter
#     def dough(self, d):
#         if d == None:
#             raise ValueError("You should add dough to the pizza")
#         self.__dough = d
#
#     @property
#     def toppings_capacity(self):
#         return self.__toppings_capacity
#     @toppings_capacity.setter
#     def toppings_capacity(self, capacity):
#         if capacity <= 0:
#             raise ValueError("The topping's capacity cannot be less or equal to zero")
#         self.__toppings_capacity = capacity
#
#     def add_topping(self, topping: Topping):
#         if self.toppings_capacity <= len(self.toppings.keys()):
#             raise ValueError("Not enough space for another topping")
#         if topping.topping_type in self.toppings:
#             self.toppings[topping.topping_type] += topping.weight
#             return
#         self.toppings[topping.topping_type] = topping.weight
#
#     def calculate_total_weight(self):
#         total_weight = self.dough.weight
#         for _, topping_weight in self.toppings.items():
#             total_weight += topping_weight
#
#         return total_weight