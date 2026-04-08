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
        """Ensures that multiple comma-separated numbers return their sum."""
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
        Ensures that newline-separated numbers return the correct sum.
        """
        resultado = exercise.add("1\n2\n3")
        self.assertEqual(resultado, 6)

    def test_trailing_comma_raises_exception(self):
        """
        Ensures that a trailing comma raises an exception.
        """
        with self.assertRaises(Exception):
            exercise.add("1,2,")

    def test_valid_input_without_trailing_comma_does_not_raise(self):
        """
        Ensures that valid input does not raise an exception.
        """
        try:
            exercise.add("1,2")
        except ValueError:
            self.fail("add() raised ValueError with valid input")

    def test_custom_single_char_delimiter_semicolon(self):
        """
        Ensures that a custom single-character delimiter (;) is supported.
        """
        resultado = exercise.add("//;\n1;3")
        self.assertEqual(resultado, 4)

    def test_custom_single_char_delimiter_pipe(self):
        """
        Ensures that a custom single-character delimiter (|) is supported.
        """
        resultado = exercise.add("//|\n1|2|3")
        self.assertEqual(resultado, 6)

    def test_custom_multi_char_delimiter(self):
        """
        Ensures that a custom multi-character delimiter is supported.
        """
        resultado = exercise.add("//sep\n2sep5")
        self.assertEqual(resultado, 7)

    def test_custom_delimiter_mixed_with_comma_raises_format_error(self):
        """
        Ensures that mixing delimiters raises a ValueError with the correct message.
        """
        with self.assertRaises(ValueError) as context:
            exercise.add("//|\n1|2,3")
        expected_message = "'|' expected but ',' found at position 3."
        self.assertEqual(str(context.exception), expected_message)

    def test_single_negative_number_raises_exception(self):
        """
        Ensures that a single negative number raises a ValueError.
        """
        with self.assertRaises(ValueError):
            exercise.add("1,-2")

    def test_single_negative_error_message_contains_negative(self):
        """
        Ensures that the error message includes the negative number.
        """
        try:
            exercise.add("1,-2")
        except ValueError as e:
            self.assertIn("-2", str(e))

    def test_multiple_negatives_raises_exception(self):
        """
        Ensures that multiple negative numbers raise a ValueError.
        """
        with self.assertRaises(ValueError):
            exercise.add("2,-4,-9")

    def test_multiple_negatives_error_message_contains_all_negatives(self):
        """
        Ensures that the error message includes all negative numbers.
        """
        try:
            exercise.add("2,-4,-9")
        except ValueError as e:
            self.assertIn("-4", str(e))
            self.assertIn("-9", str(e))
