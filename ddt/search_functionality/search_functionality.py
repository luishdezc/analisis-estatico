# -*- coding: utf-8 -*-
"""
Kata 4: Search functionality
"""

import csv
import os
import unittest


# pylint: disable=too-few-public-methods
class CitySearch:
    """
    Search cities from a CSV file with case-insensitive partial matching
    """

    def __init__(self, csv_filename):
        """
        Return cities matching text; '*' returns all, <2 chars returns empty list
        """
        base_path = os.path.dirname(__file__)
        csv_path = os.path.join(base_path, csv_filename)

        self.cities = []
        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.cities = [row["city"] for row in reader]

    def search(self, text):
        """
        Return cities matching text; '*' returns all, <2 chars returns empty list
        """
        if text == "*":
            return self.cities

        if len(text) < 2:
            return []

        return [c for c in self.cities if text.lower() in c.lower()]


class TestCitySearch(unittest.TestCase):
    """
    Unit tests for CitySearch using data-driven scenarios
    """

    def setUp(self):
        """
        Initialize search engine and test cases
        """
        self.search_engine = CitySearch("cities.csv")
        self.test_data = [
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "ape", "output": ["Budapest"]},
            {"input": "a", "output": []},
        ]

    def test_search_cities(self):
        """
        Verify search results match expected outputs
        """
        for i in self.test_data:
            with self.subTest(i=i):
                actual = self.search_engine.search(i["input"])
                self.assertEqual(
                    actual, i["output"], f"In: {i['input']}, Out: {actual}"
                )
