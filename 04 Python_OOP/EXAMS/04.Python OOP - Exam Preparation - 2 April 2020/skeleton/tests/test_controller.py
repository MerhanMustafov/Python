import unittest

from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.beginner import Beginner


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_init(self):
        self.assertEqual(self.controller.card_repository.cards, [])
        self.assertEqual(self.controller.player_repository.players, [])

    def test_add_player(self):

        type = "Advanced"
        username = "Pesho"
        massage = self.controller.add_player(type, username)
        self.assertEqual(len(self.controller.player_repository.players), 1)
        self.assertEqual(massage, f"Successfully added player of type {type} with username: {username}")

    def test_add_card(self):

        type = "MagicCard"
        name = "Pesho"
        massage = self.controller.add_card(type, name)
        self.assertEqual(len(self.controller.card_repository.cards), 1)
        self.assertEqual(massage, f"Successfully added card of type {type}Card with name: {name}")

    def test_add_player_card(self):
        player = Beginner("Pesho")
        card = MagicCard("Magic")
        self.controller.player_repository.players.append(player)
        for el in self.controller.player_repository.players:
            if el.username == "Pesho":
                el.card_repository.cards.append(card)
        username = "Pesho"
        card_name = "Magic"
        massage = self.controller.add_player_card(username, card_name)
        self.assertEqual(massage, f"Successfully added card: {card_name} to user: {username}")
        for el in self.controller.player_repository.players:
            if el.username == "Pesho":
                self.assertEqual(len(el.card_repository.cards), 2)

