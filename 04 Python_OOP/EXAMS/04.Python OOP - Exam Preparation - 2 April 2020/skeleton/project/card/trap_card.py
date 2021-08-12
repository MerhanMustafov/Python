from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name):
        super().__init__(name, 120, 5)

# trap = TrapCard("Magic")
# print(trap.health_points)
# y = Card("Card", 5, 10)
# print(y.name)