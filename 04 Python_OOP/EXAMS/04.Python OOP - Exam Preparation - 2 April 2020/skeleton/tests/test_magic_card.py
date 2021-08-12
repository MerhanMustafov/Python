import unittest

from project.card.magic_card import MagicCard


class MegicCardTests(unittest.TestCase):
    def test_init(self):
        megic_card = MagicCard("Megic")
        self.assertEqual(megic_card.name, "Megic")