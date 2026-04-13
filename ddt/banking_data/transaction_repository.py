# -*- coding: utf-8 -*-
"""
Kata 6: Banking kata
"""

from typing import List

from transaction import Transaction


class TransactionRepository:
    """
    In-memory repository for bank transactions.

    Stores each recorded transaction and returns them in reverse
    chronological order for statement generation.
    """

    def __init__(self) -> None:
        """Initialize the repository with an empty transaction list"""
        self._transactions: List[Transaction] = []

    def save(self, transaction: Transaction) -> None:
        """
        Store a new transaction in the repository.

        Args:
            transaction (Transaction): The transaction to store.
        """
        self._transactions.append(transaction)

    def all(self) -> List[Transaction]:
        """
        Return all stored transactions in reverse chronological order.

        Returns:
            List[Transaction]: Transactions from most recent to oldest.
        """
        return list(reversed(self._transactions))
