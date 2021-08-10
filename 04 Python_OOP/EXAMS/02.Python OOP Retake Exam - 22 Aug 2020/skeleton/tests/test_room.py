import unittest

from project.people.child import Child
from project.rooms.room import Room

class RoomTests(unittest.TestCase):
    def setUp(self):
        self.room = Room("Petrovi", 3000, 3)

    def test_init(self):
        self.assertEqual(self.room.family_name, "Petrovi")
        self.assertEqual(self.room.budget, 3000)
        self.assertEqual(self.room.members_count, 3)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)
    def test_negative_expanses(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))
    def test_expenses_positive(self):
        self.room.expenses = 5
        self.assertEqual(self.room.expenses, 5)

    def test_calculate_expenses(self):

        ch = Child(5, 4, 1)
        self.room.calculate_expenses([ch])
        self.assertEqual(self.room.expenses, 300)

if __name__ == "__main__":
    unittest.main()