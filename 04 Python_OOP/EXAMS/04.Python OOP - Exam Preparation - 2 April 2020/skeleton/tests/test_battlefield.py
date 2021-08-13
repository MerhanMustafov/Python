import unittest

from project.battle_field import BattleField
from project.player.beginner import Beginner


class BattleFieldTests(unittest.TestCase):
    def test_fight_exception(self):
        attacker = Beginner("Pesho")
        enemy = Beginner("Gosho")

        BattleField.fight(attacker, enemy)
        self.assertEqual(attacker.health, 90)
        self.assertEqual(enemy.health, 90)