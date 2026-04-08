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

    def test_three_numbers_returns_sum(self):
        """
        Ensures that three comma-separated numbers return their sum.
        """
        resultado = exercise.add("1,2,3")
        self.assertEqual(resultado, 6)

    def test_many_numbers_returns_sum(self):
        """
        Ensures that multiple comma-separated numbers return their sum.
        """
        resultado = exercise.add("1,2,3,4,5")
        self.assertEqual(resultado, 15)

    def test_newline_as_separator_returns_sum(self):
        """
        Ensures that newline characters can be used as separators.
        """
        resultado = exercise.add("1,2\n3")
        self.assertEqual(resultado, 6)

    def test_only_newlines_as_separators(self):
        """
        Ensures that only newline-separated numbers return the correct sum.
        """
        resultado = exercise.add("1\n2\n3")
        self.assertEqual(resultado, 6)
