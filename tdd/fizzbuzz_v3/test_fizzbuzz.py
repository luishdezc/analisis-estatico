# -*- coding: utf-8 -*-
# pylint: disable=R0801
# Alan Varela
# 25 Marzo 26

"""
Test Driven Development
"""

import unittest

from . import exercise


class TestFizzbuzz(unittest.TestCase):
    """Test"""

    def test_accepts_number_returns_string(self):
        """
        Test Req1
        """
        resultado = exercise.fizzbuzz(1)
        self.assertEqual(resultado, "1")
        self.assertIsInstance(resultado, str)

    def test_multiples_of_3_returns_fizz(self):
        """
        Test Req2
        """
        resultado = exercise.fizzbuzz(3)
        self.assertEqual(resultado, "Fizz")

    def test_multiples_of_5_returns_buzz(self):
        """
        Test Req3
        """
        resultado = exercise.fizzbuzz(5)
        self.assertEqual(resultado, "Buzz")
