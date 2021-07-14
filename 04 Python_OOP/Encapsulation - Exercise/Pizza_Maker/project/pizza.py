from project.topping import Topping
from project.dough import Dough

class Pizza:
    def __init__(self, name: str, dough, toppings_capacity: int, toppings = {}):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        if n == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = n

    @property
    def dough(self):
        return self.__dough
    @dough.setter
    def dough(self, d):
        if d == None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = d

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity
    @toppings_capacity.setter
    def toppings_capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = capacity

    def add_topping(self, topping: Topping):
        if self.toppings_capacity <= len(self.toppings.keys()):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
            return
        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight
        for _, topping_weight in self.toppings.items():
            total_weight += topping_weight

        return total_weight