import unittest

from project.card.trap_card import TrapCard


class MegicCardTests(unittest.TestCase):
    def setUp(self):
        self.trap_card = TrapCard("Trap")
    def test_init(self):
        self.assertEqual(self.trap_card.name, "Trap")
        self.assertEqual(self.trap_card.damage_points, 120)
        self.assertEqual(self.trap_card.health_points, 5)
    def test_empty_name(self):
        with self.assertRaises(ValueError) as ex:
            self.trap_card.name = ""
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))


    def test_under_zero_damage_points_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.trap_card.damage_points -= 200
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))


    def test_under_zero_health_points_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.trap_card.health_points -= 200
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))