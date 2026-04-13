# -*- coding: utf-8 -*-
"""
Kata 6: Banking kata
"""

from clock import Clock
from statement_printer import StatementPrinter
from transaction import Transaction
from transaction_repository import TransactionRepository


class Account:
    """
    Simple bank account with deposit, withdraw, and statement printing.

    Delegates storage to ``TransactionRepository``, presentation to
    ``StatementPrinter``, and date retrieval to ``Clock``.

    Args:
        repository (TransactionRepository): Transaction storage.
        printer (StatementPrinter): Statement output handler.
        clock (Clock): Current date provider.

    Example::

        account = Account(
            TransactionRepository(),
            StatementPrinter(),
            Clock(),
        )
        account.deposit(1000)
        account.withdraw(100)
        account.printStatement()
    """

    def __init__(
        self,
        repository: TransactionRepository,
        printer: StatementPrinter,
        clock: Clock,
    ) -> None:
        """
        Initialize the account with injected dependencies.

        Args:
            repository (TransactionRepository): Transaction storage.
            printer (StatementPrinter): Statement output handler.
            clock (Clock): Current date provider.
        """
        self._repository = repository
        self._printer = printer
        self._clock = clock
        self._balance: int = 0

    def deposit(self, amount: int) -> None:
        """
        Record a deposit into the account.

        Args:
            amount (int): Amount to deposit. Must be a positive integer.

        Raises:
            ValueError: If amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("El monto del depósito debe ser positivo.")
        self._balance += amount
        self._repository.save(
            Transaction(
                date=self._clock.today(),
                amount=amount,
                balance=self._balance,
            )
        )

    def withdraw(self, amount: int) -> None:
        """
        Record a withdrawal from the account.

        Args:
            amount (int): Amount to withdraw. Must be a positive integer.

        Raises:
            ValueError: If amount is less than or equal to zero.
            ValueError: If the balance is insufficient to cover the withdrawal.
        """
        if amount <= 0:
            raise ValueError("El monto del retiro debe ser positivo.")
        if amount > self._balance:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self._balance -= amount
        self._repository.save(
            Transaction(
                date=self._clock.today(),
                amount=-amount,
                balance=self._balance,
            )
        )

    def print_statement(self) -> None:
        """
        Print the account statement to the console.

        Retrieves all transactions from the repository and passes them
        to the printer for tabular display.
        """
        self._printer.print(self._repository.all())
