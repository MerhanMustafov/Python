from Test_Cat import Cat
import unittest

class CatTests(unittest.TestCase):
    name = "Kitty"
    def setUp(self):
        self.cat = Cat(self.name)
    def test_when_cat_eat_expect_size_to_be_increased_by_one(self):
        """Cat's size is increased after eating"""
        self.cat.eat()
        self.assertEqual(1, self.cat.size)
    def test_when_cat_eat_expect_fed_to_be_True(self):
        """Cat is fed after eating"""
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_sleep_when_fed_expect__not_to_be_sleepy(self):
        """Cat cannot eat if already fed, raises an error"""
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_cat_eat_when_fed_expect__exception(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep_when_not_fed_expect__exception(self):
        """Cat is not sleepy after sleeping"""
        with self.assertRaises(Exception):
            self.cat.sleep()

if __name__ == "__main__":
    unittest.main()
