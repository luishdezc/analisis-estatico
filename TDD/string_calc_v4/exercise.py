# -*- coding: utf-8 -*-
# pylint: disable=R0801

"""
Test Driven Development
"""


def add(numbers: str) -> int:
    """
    Parses a string of comma or newline-separated numbers and returns their
    sum, raising an error for trailing separators.
    """
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    if numbers.endswith(","):
        raise ValueError("Number expected but EOF found")
    parts = numbers.split(",")
    return sum(int(p) for p in parts)
