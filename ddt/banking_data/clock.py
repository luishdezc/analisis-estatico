# -*- coding: utf-8 -*-
"""
Kata 6: Banking kata
"""

from datetime import date


# pylint: disable=too-few-public-methods
class Clock:
    """
    Provides the current system date.

    Wraps ``date.today()`` behind a replaceable interface to simplify mocking
    without patching the ``datetime`` module directly.
    """

    def today(self) -> str:
        """
        Return today's date formatted as DD/MM/YYYY.

        Returns:
            str: Today's date as 'DD/MM/YYYY'.
        """
        return date.today().strftime("%d/%m/%Y")
