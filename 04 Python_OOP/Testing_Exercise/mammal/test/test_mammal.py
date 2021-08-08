
import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("bob", "dog", "bau_bau")


    def test_init_creates_all_attributes(self):
        self.assertEqual(self.mammal.name, 'bob')
        self.assertEqual(self.mammal.type, 'dog')
        self.assertEqual(self.mammal.sound, 'bau_bau')


    def test_make_sound(self):
        makes_sound = self.mammal.make_sound()
        self.assertEqual(makes_sound, f"bob makes bau_bau")

    def test_get_kingdom(self):
        get_kingdom = self.mammal.get_kingdom()
        self.assertEqual(get_kingdom, "animals")

    def test_info(self):
        info = self.mammal.info()
        self.assertEqual(info, f"bob is of type dog")

    def test_kingdom(self):
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")