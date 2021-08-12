
class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        for c in self.cards:
            if c.name == card.name:
                raise ValueError(f"Card {c.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        self.cards.remove(self.find(card))
        self.count -= 1

    def find(self, name: str):
        for c in self.cards:
            if c.name == name:
                return c
