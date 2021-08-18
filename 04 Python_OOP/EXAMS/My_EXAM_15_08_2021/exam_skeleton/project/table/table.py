from abc import ABC, abstractmethod



class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False



    def reserve(self, number_of_people):
        if self.capacity >= number_of_people:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food):  # OBJ
        self.food_orders.append(baked_food)

    def order_drink(self, drink):  # OBJ
        self.drink_orders.append(drink)

    def get_bill(self):
        result = 0
        for food in self.food_orders:
            result += food.price

        for drink in self.drink_orders:
            result += drink.price

        return result

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                    f"Type: {self.__class__.__name__}\n" \
                    f"Capacity: {self.capacity}"



