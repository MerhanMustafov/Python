from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name, price):
        super().__init__(name, 200, price)

# bread = Bread("Name", 300)
# print(bread.portion)
# baked_food = BakedFood("name", 20, 30)
