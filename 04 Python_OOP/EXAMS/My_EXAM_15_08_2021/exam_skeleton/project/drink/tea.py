from project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 2.50, brand)

# tea = Tea("Black", 250, "Tea")
# print(tea.price)
