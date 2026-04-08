# -*- coding: utf-8 -*-
# pylint: disable=R0801

"""
Test Driven Development
"""


def add(numbers: str) -> int:
    """
    Returns the sum of comma-separated integers in the input string,
    or 0 if the string is empty.
    """
    if numbers == "":
        return 0
    parts = numbers.split(",")
    return sum(int(p) for p in parts)
