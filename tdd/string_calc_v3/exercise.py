# -*- coding: utf-8 -*-
# pylint: disable=R0801

"""
Test Driven Development
"""


def add(numbers: str) -> int:
    """
    Return the sum of integers in a string, using commas or newlines as separators.
    """
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    return sum(int(p) for p in parts)
