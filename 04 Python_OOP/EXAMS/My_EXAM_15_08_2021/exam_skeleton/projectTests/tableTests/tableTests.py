import unittest

from project.table.table import Table


class TableTests(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError) as ex:
            table = Table(1, 3)
        self.assertEqual("Can't instantiate abstract class Table with abstract methods __init__", str(ex.exception))
