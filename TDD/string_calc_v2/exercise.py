# -*- coding: utf-8 -*-
# pylint: disable=R0801

"""
Test Driven Development
"""


def add(numbers: str) -> int:
    """
    Return the sum of integers in a comma-separated string.
    """
    if numbers == "":
        return 0
    parts = numbers.split(",")
    return sum(int(p) for p in parts)
