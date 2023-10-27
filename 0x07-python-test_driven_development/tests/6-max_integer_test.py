#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for the max_integer function"""

    def test_max_integer(self):
        """test_max_integer."""
        self.assertEqual(max_integer([8, -3, 14, 2]), 14)

    def test_empty_list(self):
        """test_empty_list."""
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        """test_repeated_number."""
        self.assertEqual(max_integer([777, 777, 777]), 777)

    def test_max_at_beginning(self):
        """test_max_at_beginning."""
        self.assertEqual(max_integer([9, 7, 5, 3, 1]), 9)

    def test_number(self):
        """test_number."""
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_neg_numbers(self):
        """test_neg_numbers."""
        self.assertEqual(max_integer([-20, -15, -10, -5]), -5)

    def test_float_numbers(self):
        """test_float_numbers."""
        self.assertEqual(max_integer([8.5, 9.2, 7.8, 7.7]), 9.2)

    def test_max_operated_integer(self):
        """test_max_operated_integer."""
        self.assertEqual(max_integer([-5, 3 * 6, 18, -2]), 18)

    def test_zero_number(self):
        """test_zero_number."""
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
        """test_big_list."""
        self.assertEqual(max_integer([
            1000, 999, 998, 997, 996, 995, 994, 993, 992, 991,
            990, 989, 988, 987, 986, 985, 984, 983, 982, 981,
            980, 979, 978, 977, 976, 975, 974, 973, 972, 971,
            970, 969, 968, 967, 966, 965, 964, 963, 962, 961]), 1000)

    def test_list_with_loop(self):
        """test_list_with_loop."""
        my_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer([i * 3 for i in my_list]), 30)

    def test_one_number_in_a_list(self):
        """test_one_number_in_a_list."""
        self.assertEqual(max_integer([7]), 7)

    def test_string_number_in_a_list(self):
        """test_string_number_in_a_list."""
        with self.assertRaises(TypeError):
            max_integer([0, '12'])

    def test_tuple_in_a_list(self):
        """test_tuple_in_a_list."""
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        """test_dictionary."""
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})


if __name__ == '__main__':
    unittest.main()
