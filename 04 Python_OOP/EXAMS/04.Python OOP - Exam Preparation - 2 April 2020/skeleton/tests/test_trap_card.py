import unittest

from project.card.trap_card import TrapCard


class MegicCardTests(unittest.TestCase):
    def test_init(self):
        trap_card = TrapCard("Trap")
        self.assertEqual(trap_card.name, "Trap")