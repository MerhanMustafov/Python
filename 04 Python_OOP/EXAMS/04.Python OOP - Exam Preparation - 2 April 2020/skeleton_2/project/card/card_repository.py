class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        is_present = [c for c in self.cards if c.name == card.name]
        if is_present:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        card_name = self.find(card)
        self.cards.remove(card_name)
        self.count -= 1
        return

    def find(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card
