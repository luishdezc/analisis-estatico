# -*- coding: utf-8 -*-
# pylint: disable=R0801

"""
Test Driven Development
"""


def fizzbuzz(a: int):
    """
    Returns "Fizz" if the number is divisible by 3, otherwise returns the number as a string.
    """
    if a % 3 == 0:
        return "Fizz"
    return str(a)
