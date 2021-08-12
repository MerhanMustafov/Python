import unittest

from project.player.advanced import Advanced


class AdvancedTests(unittest.TestCase):
    def test_init(self):
        advanced = Advanced("Seto")
        self.assertEqual(advanced.username, "Seto")
