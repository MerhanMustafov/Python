import unittest

from project.card.magic_card import MagicCard


class MegicCardTests(unittest.TestCase):
    def setUp(self):
        self.megic_card = MagicCard("Megic")
    def test_init(self):
        self.assertEqual(self.megic_card.name, "Megic")
        self.assertEqual(self.megic_card.damage_points, 5)
        self.assertEqual(self.megic_card.health_points, 80)

    def test_empty_name(self):
        with self.assertRaises(ValueError) as ex:
            self.megic_card.name = ""
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))


    def test_under_zero_damage_points_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.megic_card.damage_points -= 200
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))


    def test_under_zero_health_points_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.megic_card.health_points -= 200
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))