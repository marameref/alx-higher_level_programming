#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
from subprocess import call
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Checks for correct output during many edge cases.
    """
    def test_simple(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-219, -89, -832, -300]), -89)
        self.assertEqual(max_integer([-219, -89, 832, -300]), 832)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one_item(self):
        self.assertEqual(max_integer([42]), 42)

    def test_wrong_tpye(self):
        with self.assertRaises(TypeError):
            max_integer(None)
            max_integer("bell pepper")
            max_integer([1, 2, 3, "cat"])
            max_integer([1, 2, (8, 3), 4])
            max_integer([1, 2, 3.7, 4])

    def test_style(self):
        try:
            self.assertEqual(call(["pep8", "6-max_integer.py"]), 0)
        except FileNotFoundError:
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
