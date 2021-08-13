import unittest

from project.player.beginner import Beginner


class BeginnerTests(unittest.TestCase):
    def setUp(self):
        self.beginnar = Beginner("Yu-Gi")
    def test_init(self):
        self.assertEqual(self.beginnar.username, "Yu-Gi")
        self.assertEqual(self.beginnar.health, 50)
    def test_health_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.beginnar.health -= 51
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))
    def test_empty_username(self):
        with self.assertRaises(ValueError) as ex:
            self.beginnar.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))