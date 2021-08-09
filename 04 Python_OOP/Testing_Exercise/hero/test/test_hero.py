import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Pesho", 5, 97, 3)

    def test_init(self):
        self.assertEqual(self.hero.username, "Pesho")
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 97)
        self.assertEqual(self.hero.damage, 3)

    def test_battle_when_enemy_and_hero_are_with_same_names__exception__(self):
        enemy_hero = Hero("Pesho", 4, 90, 10)
        with self.assertRaises(Exception) as e:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(e.exception))
    def test_battle_when_hero_health_is_under_or_0(self):
        enemy_hero = Hero("Jiji", 4, 90, 10)
        self.hero.health = 0
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_battle_when_enemy_health_is_under_or_0(self):
        enemy_hero = Hero("Jiji", 4, 90, 10)
        enemy_hero.health = 0
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(e.exception))

    def test_damage(self):
        enemy_hero = Hero("Jiji", 4, 90, 10)
        player_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level
        self.hero.battle(enemy_hero)
        self.assertEqual(player_damage, 15)
        self.assertEqual(enemy_hero_damage, 40)

    def test_health(self):
        enemy_hero = Hero("Jiji", 4, 90, 10)
        player_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level
        self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.health, 57)
        self.assertEqual(enemy_hero.health, 80)
    def test_draw(self):
        enemy_hero = Hero("Jiji", 4, 90, 10)
        self.hero.damage = 100
        enemy_hero.damage = 100
        player_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level
        self.assertEqual(self.hero.battle(enemy_hero), "Draw")

    def test_you_win(self):
        enemy_hero = Hero("Jiji", 4, 90, 10)
        self.hero.damage = 100
        player_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level
        self.assertEqual(self.hero.battle(enemy_hero), "You win")
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.health, 62)
        self.assertEqual(self.hero.damage, 105)

    def test_you_lose(self):
        enemy_hero = Hero("Jiji", 4, 90, 10)

        self.assertEqual(self.hero.battle(enemy_hero), "You lose")
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 57)
        self.assertEqual(self.hero.damage, 3)

    def test_str_method(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\n"
                        f"Health: {self.hero.health}\n"
                        f"Damage: {self.hero.damage}\n", str(self.hero))