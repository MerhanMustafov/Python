import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class PlayerRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.player_repo = PlayerRepository()

    def test_init(self):
        self.assertEqual(self.player_repo.count, 0)
        self.assertEqual(self.player_repo.players, [])

    def test_add_method(self):
        player = Beginner("Gojo")
        self.player_repo.add(player)
        self.assertEqual(len(self.player_repo.players), 1)
        self.assertEqual(self.player_repo.count, 1)

    def test_add_method_when_exception(self):
        player = Beginner("Gojo")
        self.player_repo.add(player)
        with self.assertRaises(ValueError) as ex:
            self.player_repo.add(player)
        self.assertEqual(f"Player {player.username} already exists!", str(ex.exception))

    def test_find_method(self):
        player = Beginner("Gojo")
        self.player_repo.add(player)
        username = "Gojo"
        expected = self.player_repo.players[0]
        actual = self.player_repo.find(username)
        self.assertEqual(actual, expected)

    def test_remove_str_empty(self):
        player = ""
        with self.assertRaises(ValueError) as ex:
            self.player_repo.remove(player)
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_remove(self):
        player = Beginner("Gojo")
        self.player_repo.add(player)
        player = "Gojo"
        self.player_repo.remove(player)
        self.assertEqual(len(self.player_repo.players), self.player_repo.count)
        self.assertEqual(self.player_repo.count, 0)