import unittest

from project.player.advanced import Advanced


class AdvancedTests(unittest.TestCase):
    def setUp(self):
        self.advanced = Advanced("Seto")
    def test_init(self):
        self.assertEqual(self.advanced.username, "Seto")
        self.assertEqual(self.advanced.health, 250)

    def test_health_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.health -= 251
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))
    def test_empty_username(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))
