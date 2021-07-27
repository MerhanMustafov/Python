from List import IntegerList
import unittest

class TestIntegerList(unittest.TestCase):



    def test_intiger_list_add_when_int_should_add_it(self):
        integer_list = IntegerList()
        integer_list = integer_list.add(1)
        self.assertEqual([1], integer_list)

    def test_intiger_list_add_when_str_expected_exception(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add("as")

    def test_intiger_list_remove_when_valid_index_expected_to_remove_and_return_it(self):
        value_to_be_rmoved = 3
        integer_list = IntegerList(1, 2, value_to_be_rmoved, 4)
        result = integer_list.remove_index(2)
        self.assertEqual(value_to_be_rmoved, result)
        self.assertEqual([1, 2, 4], integer_list.get_data())

    def test_intiger_list_remove_index_when_invalid_negative_index_expected_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = -4
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)
    def test_intiger_list_remove_index_when_invalid_positive_index_expected_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)
    def test_intiger_list_init__when_integers_expect_to_creat_it(self):
        IntegerList(1, 2, 3)

    def test_intiger_list_init__when_not_only_integers_expect_exception(self):
        with self.assertRaises(Exception):
            IntegerList(1, 2, "as")

    def test_intiger_list_get_when_valid_index_expected_to_return_it(self):
        pass
    def test_intiger_list_get_when_invalid_negative_index_expected_exception(self):
        pass
    def test_intiger_list_get_when_invalid_positive_index_expected_exception(self):
        pass

    def test_intiger_list_insert_when_invalid_positive_index_expected_exception(self):
        pass


    def test_intiger_list_insert_when_valid_index_and_value_expected_to_insert_it(self):
        pass
    def test_intiger_list_insert_when_invalid_negative_index_expected_exception(self):
        pass
    def test_intiger_list_insert__when_invalid_positive_index_expected_exception(self):
        pass


    def test_intiger_list_insert__when_value_is_str_expected_exception(self):
        pass

    def test_intiger_list_get_biggest__when_invalid_positive_index_expected_to_return_the_biggest(self):
        pass