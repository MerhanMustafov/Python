import unittest

from project.player.beginner import Beginner


class BeginnerTests(unittest.TestCase):
    def test_init(self):
        beginnar = Beginner("Yu-Gi")
        self.assertEqual(beginnar.username, "Yu-Gi")
