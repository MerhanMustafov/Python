from project.product import Product


class Drink(Product):
    quantity = 10
    def __init__(self, name):
        super().__init__(name, Drink.quantity)

    def __repr__(self):
        return f"{self.name}: {self.quantity}"
