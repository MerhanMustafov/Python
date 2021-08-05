from project.product import Product


class Food(Product):
    quantity = 15
    def __init__(self, name):
        super().__init__(name, Food.quantity)

    def __repr__(self):
        return f"{self.name}: {self.quantity}"
