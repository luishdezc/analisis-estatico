# -*- coding: utf-8 -*-
# pylint: disable=protected-access
# pylint: disable=import-outside-toplevel
"""
Kata 6: Banking kata
"""

import sys
import unittest
from unittest.mock import MagicMock, patch

from account import Account
from clock import Clock
from statement_printer import StatementPrinter
from transaction_repository import TransactionRepository

from ddt import data, ddt, unpack  # pylint: disable=no-name-in-module

sys.path.insert(0, ".")


def make_account(today: str = "01/04/2014") -> Account:
    """
    Build an ``Account`` instance with test-ready dependencies.

    Uses a mocked ``Clock`` returning the given date, a real in-memory
    repository, and a real ``StatementPrinter``.

    Args:
        today (str): Fixed date the mocked clock will return.

    Returns:
        Account: Instance ready for use in tests.
    """
    clock = MagicMock(spec=Clock)
    clock.today.return_value = today
    return Account(
        repository=TransactionRepository(),
        printer=StatementPrinter(),
        clock=clock,
    )


@ddt
class TestDeposit(unittest.TestCase):
    """
    Unit tests for the deposit operation
    """

    @data(
        (500, 500),
        (1000, 1000),
        (1, 1),
        (999999, 999999),
    )
    @unpack
    def test_deposit_updates_balance(self, amount: int, expected_balance: int) -> None:
        """
        Verify that a deposit correctly updates the balance.

        Args:
            amount (int): Amount to deposit.
            expected_balance (int): Expected balance after the deposit.
        """
        account = make_account()
        account.deposit(amount)
        self.assertEqual(account._balance, expected_balance)

    @data(
        (200, 300, 500),
        (1000, 500, 1500),
        (50, 50, 100),
    )
    @unpack
    def test_multiple_deposits_accumulate(
        self, first: int, second: int, expected: int
    ) -> None:
        """
        Verify that multiple deposits accumulate the balance correctly.

        Args:
            first (int): First deposited amount.
            second (int): Second deposited amount.
            expected (int): Expected total balance.
        """
        account = make_account()
        account.deposit(first)
        account.deposit(second)
        self.assertEqual(account._balance, expected)

    @data(
        (500, 1, "01/04/2014", 500),
    )
    @unpack
    def test_deposit_stores_transaction(
        self, amount: int, expected_count: int, date: str, expected_balance: int
    ) -> None:
        """
        Verify that a deposit stores exactly one transaction with correct data.

        Args:
            amount (int): Amount to deposit.
            expected_count (int): Expected number of stored transactions.
            date (str): Expected date on the transaction.
            expected_balance (int): Expected balance on the transaction.
        """
        account = make_account(today=date)
        account.deposit(amount)
        transactions = account._repository.all()
        self.assertEqual(len(transactions), expected_count)
        self.assertEqual(transactions[0].amount, amount)
        self.assertEqual(transactions[0].date, date)
        self.assertEqual(transactions[0].balance, expected_balance)


@ddt
class TestWithdraw(unittest.TestCase):
    """
    Unit tests for the withdrawal operation
    """

    @data(
        (1000, 100, 900),
        (1000, 500, 500),
        (1000, 1000, 0),
    )
    @unpack
    def test_withdraw_updates_balance(
        self, initial: int, withdraw: int, expected: int
    ) -> None:
        """
        Verify that a withdrawal correctly reduces the balance.

        Args:
            initial (int): Starting balance after an initial deposit.
            withdraw (int): Amount to withdraw.
            expected (int): Expected balance after the withdrawal.
        """
        account = make_account()
        account.deposit(initial)
        account.withdraw(withdraw)
        self.assertEqual(account._balance, expected)

    @data(
        (1000, 100, -100),
        (500, 200, -200),
    )
    @unpack
    def test_withdraw_stores_negative_amount(
        self, initial: int, withdraw: int, expected_amount: int
    ) -> None:
        """
        Verify that a withdrawal is stored as a negative amount.

        Args:
            initial (int): Starting balance.
            withdraw (int): Amount to withdraw.
            expected_amount (int): Expected amount value on the transaction.
        """
        account = make_account()
        account.deposit(initial)
        account.withdraw(withdraw)
        last_tx = account._repository.all()[0]
        self.assertEqual(last_tx.amount, expected_amount)

    @data(
        (1000, 100, 500, 400),
        (2000, 1000, 500, 500),
    )
    @unpack
    def test_multiple_withdrawals(
        self, initial: int, w1: int, w2: int, expected: int
    ) -> None:
        """
        Verify that multiple withdrawals reduce the balance cumulatively.

        Args:
            initial (int): Initial deposit amount.
            w1 (int): First withdrawal amount.
            w2 (int): Second withdrawal amount.
            expected (int): Expected final balance.
        """
        account = make_account()
        account.deposit(initial)
        account.withdraw(w1)
        account.withdraw(w2)
        self.assertEqual(account._balance, expected)


class TestPrintStatement(unittest.TestCase):
    """
    Integration tests for ``printStatement`` using a mocked ``print``.

    Verifies that the statement is printed in the correct order
    (most recent first) and with the expected format.
    """

    def test_print_statement_shows_header(self) -> None:
        """Verify that the header appears as the first line of the statement."""
        account = make_account()
        account.deposit(1000)
        with patch("builtins.print") as mock_print:
            account.print_statement()
        first_call = mock_print.call_args_list[0]
        self.assertIn("DATE", first_call.args[0])
        self.assertIn("AMOUNT", first_call.args[0])
        self.assertIn("BALANCE", first_call.args[0])

    def test_print_statement_full_scenario(self) -> None:
        """
        Verify the full kata scenario: deposit 1000, withdraw 100, deposit 500.

        Lines must appear from most recent to oldest.
        """
        clock = MagicMock(spec=Clock)
        dates = ["01/04/2014", "02/04/2014", "10/04/2014"]
        clock.today.side_effect = dates

        account = Account(
            repository=TransactionRepository(),
            printer=StatementPrinter(),
            clock=clock,
        )
        account.deposit(1000)
        account.withdraw(100)
        account.deposit(500)

        with patch("builtins.print") as mock_print:
            account.print_statement()

        calls = [c.args[0] for c in mock_print.call_args_list]

        self.assertIn("DATE", calls[0])

        self.assertIn("10/04/2014", calls[1])
        self.assertIn("500.00", calls[1])
        self.assertIn("1400.00", calls[1])

        self.assertIn("02/04/2014", calls[2])
        self.assertIn("-100.00", calls[2])
        self.assertIn("900.00", calls[2])

        self.assertIn("01/04/2014", calls[3])
        self.assertIn("1000.00", calls[3])
        self.assertIn("1000.00", calls[3])

    def test_print_statement_empty_account(self) -> None:
        """
        Verify that an account with no transactions only prints the header
        """
        account = make_account()
        with patch("builtins.print") as mock_print:
            account.print_statement()
        self.assertEqual(mock_print.call_count, 1)
        self.assertIn("DATE", mock_print.call_args_list[0].args[0])

    def test_printer_is_called_with_all_transactions(self) -> None:
        """
        Verify that ``StatementPrinter.print`` receives the full transaction list
        """
        mock_printer = MagicMock(spec=StatementPrinter)
        clock = MagicMock(spec=Clock)
        clock.today.return_value = "01/04/2014"

        account = Account(
            repository=TransactionRepository(),
            printer=mock_printer,
            clock=clock,
        )
        account.deposit(1000)
        account.withdraw(100)
        account.print_statement()

        mock_printer.print.assert_called_once()
        transactions_passed = mock_printer.print.call_args[0][0]
        self.assertEqual(len(transactions_passed), 2)


@ddt
class TestInvalidOperations(unittest.TestCase):
    """
    Test invalid deposit and withdraw operations
    """

    @data(0, -1, -500, -999999)
    def test_deposit_raises_on_non_positive_amount(self, amount: int) -> None:
        """
        Verify deposit raises ValueError for non-positive amounts
        """
        account = make_account()
        with self.assertRaises(ValueError):
            account.deposit(amount)

    @data(0, -1, -100)
    def test_withdraw_raises_on_non_positive_amount(self, amount: int) -> None:
        """
        Verify withdraw raises ValueError for non-positive amounts
        """
        account = make_account()
        account.deposit(1000)
        with self.assertRaises(ValueError):
            account.withdraw(amount)

    @data(
        (500, 501),
        (0, 1),
        (100, 200),
    )
    @unpack
    def test_withdraw_raises_when_insufficient_funds(
        self, deposit: int, withdraw: int
    ) -> None:
        """
        Verify withdraw raises ValueError when funds are insufficient
        """
        account = make_account()
        if deposit > 0:
            account.deposit(deposit)
        with self.assertRaises(ValueError):
            account.withdraw(withdraw)


@ddt
class TestStatementPrinter(unittest.TestCase):
    """
    Test statement printer formatting and output
    """

    @data(
        (1000, "1000.00"),
        (-100, "-100.00"),
        (500, "500.00"),
        (0, "0.00"),
    )
    @unpack
    def test_format_amount(self, amount: int, expected: str) -> None:
        """
        Verify amount formatting returns correct decimal string
        """
        result = StatementPrinter._format_amount(amount)
        self.assertEqual(result, expected)

    def test_printer_outputs_correct_lines(self) -> None:
        """
        Verify printer outputs header and all transaction lines
        """
        from transaction import Transaction

        printer = StatementPrinter()
        transactions = [
            Transaction(date="10/04/2014", amount=500, balance=1400),
            Transaction(date="02/04/2014", amount=-100, balance=900),
            Transaction(date="01/04/2014", amount=1000, balance=1000),
        ]
        with patch("builtins.print") as mock_print:
            printer.print(transactions)

        self.assertEqual(mock_print.call_count, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
