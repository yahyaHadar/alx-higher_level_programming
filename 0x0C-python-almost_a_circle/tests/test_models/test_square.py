#!/usr/bin/python3
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """TestSquare_instantiation."""

    def test_is_base(self):
        """test_is_base."""
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """test_is_rectangle."""
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        """test_no_args."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """test_one_arg."""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_size_private(self):
        """test_size_private."""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """test_size_getter."""
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        """test_size_setter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """test_width_getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        """test_height_getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        """test_x_getter."""
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """test_y_getter."""
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """TestSquare_size."""

    def test_None_size(self):
        """test_None_size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        """test_str_size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_negative_size(self):
        """test_negative_size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        """test_zero_size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """TestSquare_x."""

    def test_None_x(self):
        """test_None_x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        """test_str_x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_negative_x(self):
        """test_negative_x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
    """TestSquare_y."""

    def test_None_y(self):
        """test_None_y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        """test_str_y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        """test_float_y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complex_y(self):
        """test_complex_y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_negative_y(self):
        """test_negative_y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquare_order_of_initialization(unittest.TestCase):
    """TestSquare_order_of_initialization."""

    def test_size_before_x(self):
        """test_size_before_x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        """test_size_before_y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        """test_x_before_y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """TestSquare_area."""

    def test_area_small(self):
        """test_area_small."""
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        """test_area_large."""
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        """test_area_changed_attributes."""
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_one_arg(self):
        """test_area_one_arg."""
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_update_args(unittest.TestCase):
    """TestSquare_update_args."""

    def test_update_args_zero(self):
        """test_update_args_zero."""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        """test_update_args_one."""
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_four(self):
        """test_update_args_four."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_None_id(self):
        """test_update_args_None_id."""
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        """test_update_args_None_id_and_more."""
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        """test_update_args_twice."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        """test_update_args_invalid_size_type."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_invalid_x(self):
        """test_update_args_invalid_x."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_before_y(self):
        """test_update_args_x_before_y."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """TestSquare_update_kwargs."""

    def test_update_kwargs_one(self):
        """test_update_kwargs_one."""
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        """test_update_kwargs_two."""
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_four(self):
        """test_update_kwargs_four."""
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        """test_update_kwargs_width_setter."""
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_twice(self):
        """test_update_kwargs_twice."""
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_y_negative(self):
        """test_update_kwargs_y_negative."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_kwargs_wrong_keys(self):
        """test_update_kwargs_wrong_keys."""
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        """test_update_kwargs_some_wrong_keys."""
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        """test_to_dictionary_output."""
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """test_to_dictionary_no_object_changes."""
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        """test_to_dictionary_arg."""
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
