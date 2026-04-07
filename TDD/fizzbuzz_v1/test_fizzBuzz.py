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
    """
    Test
    """

    def test_accepts_number_returns_string(self):
        """
        Test Req1
        """
        resultado = exercise.fizzbuzz(1)
        self.assertEqual(resultado, "1")
        self.assertIsInstance(resultado, str)
