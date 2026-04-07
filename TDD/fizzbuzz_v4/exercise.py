# -*- coding: utf-8 -*-
# pylint: disable=R0801

"""
Test Driven Development
"""


def fizzbuzz(a: int):
    """
    Returns "FizzBuzz" if divisible by 3 and 5, "Fizz" if divisible by 3,
    "Buzz" if divisible by 5, otherwise returns the number as a string.
    """
    if a % 3 == 0 and a % 5 == 0:
        return "FizzBuzz"
    if a % 3 == 0:
        return "Fizz"
    if a % 5 == 0:
        return "Buzz"
    return str(a)
