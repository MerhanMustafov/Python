import unittest

from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple


class RoomTests(unittest.TestCase):
    def setUp(self):
        self.room = Room("Name", 100, 2)
        self.young_couple = YoungCouple("Johnsons", 150, 205)

    def test_init(self):
        self.assertEqual(self.room.family_name, "Name")
        self.assertEqual(self.room.budget, 100)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_expenses_negative_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses -= 1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_expenses_positive(self):
        self.room.expenses += 2
        self.assertEqual(self.room.expenses, 2)

    def test_calculate_expenses(self):
        actual = self.young_couple.expenses
        self.assertEqual(actual, 222)

if __name__ == "__main__":
    unittest.main()
