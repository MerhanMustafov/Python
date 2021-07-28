from List import IntegerList
import unittest

class IntegerListTests(unittest.TestCase):

    def setUp(self):
        self.list = IntegerList([])

    def test_add(self):
        self.assertEqual(self.list.add(1), [1])
    def test_when_is_not_int_exception(self):
        self.assertRaises(ValueError, self.list.add, "mm")
    def test_remove_by_index(self):
        self.list.add(42)
        el = self.list.remove_index(0)
        self.assertEqual(el, 42)
    def test_remove_by_index_raises_indexerror(self):
        self.assertRaises(IndexError, self.list.remove_index, 0)
    def test_init_take_only_ints(self):
        list = IntegerList("merho", 42, "ohrem")
        self.assertEqual(list.get_data(), [42])

    def test_get(self):
        self.list.add(42)
        self.assertEqual(self.list.get(0), 42)

    def test_get_taises_index_error(self):
        self.assertRaises(IndexError, self.list.get, 0)

    def test_insert(self):
        self.assertRaises(IndexError, self.list.insert, 0, 42)
        self.list.add(1)
        self.assertRaises(ValueError, self.list.insert, 0, "baba")
        self.list.insert(0, 42)
        self.assertEqual(self.list.get_data(), [42, 1])

    def test_get_biggest(self):
        self.list.add(42)
        self.list.add(43)
        self.assertEqual(self.list.get_biggest(), 43)
    def test_get_index(self):
        self.list.add(42)
        self.assertEqual(self.list.get_index(42), 0)
if __name__ == "__main__":
    unittest.main()

    # def test_intiger_list_add_when_str_expected_exception(self):
    #     integer_list = IntegerList()
    #     with self.assertRaises(ValueError):
    #         integer_list.add("as")
    #
    # def test_intiger_list_remove_when_valid_index_expected_to_remove_and_return_it(self):
    #     value_to_be_rmoved = 3
    #     integer_list = IntegerList(1, 2, value_to_be_rmoved, 4)
    #     result = integer_list.remove_index(2)
    #     self.assertEqual(value_to_be_rmoved, result)
    #     self.assertEqual([1, 2, 4], integer_list.get_data())
    #
    # def test_intiger_list_remove_index_when_invalid_negative_index_expected_exception(self):
    #     integer_list = IntegerList(1, 2, 3)
    #     index = -4
    #     with self.assertRaises(IndexError):
    #         integer_list.remove_index(index)
    # def test_intiger_list_remove_index_when_invalid_positive_index_expected_exception(self):
    #     integer_list = IntegerList(1, 2, 3)
    #     index = 3
    #     with self.assertRaises(IndexError):
    #         integer_list.remove_index(index)
    # def test_intiger_list_init__when_integers_expect_to_creat_it(self):
    #     IntegerList(1, 2, 3)
    #
    # def test_intiger_list_init__when_not_only_integers_expect_exception(self):
    #     with self.assertRaises(Exception):
    #         IntegerList(1, 2, "as")
    #
    # def test_intiger_list_get_when_valid_index_expected_to_return_it(self):
    #     pass
    # def test_intiger_list_get_when_invalid_negative_index_expected_exception(self):
    #     pass
    # def test_intiger_list_get_when_invalid_positive_index_expected_exception(self):
    #     pass
    #
    # def test_intiger_list_insert_when_invalid_positive_index_expected_exception(self):
    #     pass
    #
    #
    # def test_intiger_list_insert_when_valid_index_and_value_expected_to_insert_it(self):
    #     pass
    # def test_intiger_list_insert_when_invalid_negative_index_expected_exception(self):
    #     pass
    # def test_intiger_list_insert__when_invalid_positive_index_expected_exception(self):
    #     pass
    #
    #
    # def test_intiger_list_insert__when_value_is_str_expected_exception(self):
    #     pass
    #
    # def test_intiger_list_get_biggest__when_invalid_positive_index_expected_to_return_the_biggest(self):
    #     pass