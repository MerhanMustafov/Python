import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class PlayerRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.card_repo = CardRepository()

    def test_init(self):
        self.assertEqual(self.card_repo.count, 0)
        self.assertEqual(self.card_repo.cards, [])

    def test_add_method(self):
        card = MagicCard("Magic")
        self.card_repo.add(card)
        self.assertEqual(len(self.card_repo.cards), 1)
        self.assertEqual(self.card_repo.count, 1)

    def test_add_method_when_exception(self):
        card = MagicCard("Magic")
        self.card_repo.add(card)
        with self.assertRaises(ValueError) as ex:
            self.card_repo.add(card)
        self.assertEqual(f"Card {card.name} already exists!", str(ex.exception))

    def test_find_method(self):
        card = MagicCard("Magic")
        self.card_repo.add(card)
        name = "Magic"
        expected = self.card_repo.cards[0]
        actual = self.card_repo.find(name)
        self.assertEqual(actual, expected)

    def test_remove_str_empty(self):
        card = ""
        with self.assertRaises(ValueError) as ex:
            self.card_repo.remove(card)
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_remove(self):
        card = MagicCard("Magic")
        self.card_repo.add(card)
        c = "Gojo"
        self.card_repo.remove(c)
        self.assertEqual(len(self.card_repo.cards), self.card_repo.count)
        self.assertEqual(self.card_repo.count, 0)