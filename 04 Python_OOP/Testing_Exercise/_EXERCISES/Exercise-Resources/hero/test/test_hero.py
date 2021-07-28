from project.hero import Hero

import unittest

class HeroTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        """def __init__(self, username: str, level: int, health: float, damage: float):"""
        self.hero = Hero("John", 2, 10.0, 5.0)
        self.enemy_hero = Hero("Mike", 2, 10.0, 5.0)
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def test_initialization(self):
        self.assertEqual(self.hero.username, "John")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 10.0)
        self.assertEqual(self.hero.damage, 5.0)
    def test_you_can_not_fight_yourself(self):
        enemy_hero = Hero("John", 2, 10.0, 5.0)
        with self.assertRaises(Exception):
            self.hero.battle(enemy_hero)
    def test_when_health_equal_or_under_0(self):
        self.enemy_hero.health = 0
        with self.assertRaises(Exception) as exc:
            self.enemy_hero.health = -1
            str(exc.exception)



    def test_when_both_health_is_0(self):
        with self.assertRaises(ValueError):
            self.enemy_hero.health = 0
            self.hero.health = 0










if __name__ == "__main__":
    unittest.main()