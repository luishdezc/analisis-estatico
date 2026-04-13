# -*- coding: utf-8 -*-
"""
Kata 6: Banking kata
"""

from typing import List

from transaction import Transaction


# pylint: disable=too-few-public-methods
class StatementPrinter:
    """
    Prints the bank account statement to the console.

    Handles only the presentation layer: receives a list of transactions
    and prints them in DATE | AMOUNT | BALANCE format.
    """

    HEADER = "DATE       | AMOUNT  | BALANCE"

    def print(self, transactions: List[Transaction]) -> None:
        """
        Print the header followed by each transaction line.

        Args:
            transactions (List[Transaction]): Transactions ordered most recent first.
        """
        print(self.HEADER)
        for transaction in transactions:
            amount_str = self._format_amount(transaction.amount)
            balance_str = self._format_amount(transaction.balance)
            print(f"{transaction.date} | {amount_str} | {balance_str}")

    @staticmethod
    def _format_amount(amount: int) -> str:
        """
        Format an integer amount as a two-decimal string.

        Args:
            amount (int): Amount to format (may be negative).

        Returns:
            str: Amount as 'NNNN.00' or '-NNNN.00' if negative.
        """
        return f"{amount:.2f}"
