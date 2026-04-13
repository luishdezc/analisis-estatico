# -*- coding: utf-8 -*-
"""
Kata 6: Banking kata
"""

from dataclasses import dataclass


# pylint: disable=too-few-public-methods
@dataclass
class Transaction:
    """
    Represents a single bank transaction.

    Attributes:
        date (str): Transaction date in DD/MM/YYYY format.
        amount (int): Transaction amount. Positive for deposits, negative for withdrawals.
        balance (int): Resulting balance after the transaction is applied.
    """

    date: str
    amount: int
    balance: int
