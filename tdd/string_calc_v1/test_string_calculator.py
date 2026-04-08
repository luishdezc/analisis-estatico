# -*- coding: utf-8 -*-
# pylint: disable=R0801

"""
Test Driven Development
"""

import unittest

from . import exercise


class TestStringCalculator(unittest.TestCase):
    """
    Test
    """

    def test_empty_string_returns_zero(self):
        """
        Ensures that an empty string returns 0.
        """
        resultado = exercise.add("")
        self.assertEqual(resultado, 0)

    def test_single_number_returns_itself(self):
        """
        Ensures that a single number returns its integer value.
        """
        resultado = exercise.add("1")
        self.assertEqual(resultado, 1)

    def test_two_numbers_returns_sum(self):
        """
        Ensures that two comma-separated numbers return their sum.
        """
        resultado = exercise.add("1,2")
        self.assertEqual(resultado, 3)

    def test_return_type_is_int(self):
        """
        Ensures that the result is of type int.
        """
        resultado = exercise.add("1")
        self.assertIsInstance(resultado, int)
