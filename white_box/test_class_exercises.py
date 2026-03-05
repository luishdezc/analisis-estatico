# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest
from io import StringIO
from unittest.mock import patch

from white_box.class_exercises import (
    BankAccount,
    BankingSystem,
    DocumentEditingSystem,
    ElevatorSystem,
    Product,
    ShoppingCart,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
)


# 22
class TestVendingMachine(unittest.TestCase):
    """
    White-box unit test class for the VendingMachine system.
    It validates correct state transitions and invalid operations.
    """

    def setUp(self):
        """
        Creates a new VendingMachine instance before each test
        and verifies that the initial state is "Ready".
        """
        self.machine = VendingMachine()
        self.assertEqual(self.machine.state, "Ready")

    def test_insert_coin_from_ready(self):
        """
        Tests inserting a coin when the machine is in "Ready" state.
        Verifies that the state changes to "Dispensing".
        """
        result = self.machine.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_select_drink_from_dispensing(self):
        """
        Tests selecting a drink after inserting a coin.
        Verifies that the machine returns to "Ready" state.
        """
        self.machine.insert_coin()
        result = self.machine.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(self.machine.state, "Ready")

    def test_insert_coin_when_dispensing(self):
        """
        Tests inserting a coin while already in "Dispensing" state.
        Verifies that the operation is rejected and state remains unchanged.
        """
        self.machine.insert_coin()
        result = self.machine.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_select_drink_when_dispensing(self):
        """
        Tests selecting a drink without inserting a coin first.
        Verifies that the operation is rejected and state remains "Ready".
        """
        self.machine.select_drink()
        result = self.machine.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.machine.state, "Ready")


# 23
class TestTrafficLight(unittest.TestCase):
    """
    White-box unit test class for the TrafficLight system.
    It validates correct state transitions through the full cycle.
    """

    def setUp(self):
        """
        Creates a new TrafficLight instance before each test
        and verifies that the initial state is "Red".
        """
        self.light = TrafficLight()
        self.assertEqual(self.light.state, "Red")

    def test_change_state_cycle(self):
        """
        Tests the complete traffic light cycle:
        Red -> Green -> Yellow -> Red.
        Verifies that each state transition occurs correctly.
        """
        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Green")

        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Yellow")

        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Red")


# 24
class TestUserAuthentication(unittest.TestCase):
    """
    White-box unit test class for the UserAuthentication system.
    It validates correct login/logout transitions and invalid operations.
    """

    def setUp(self):
        """
        Creates a new UserAuthentication instance before each test
        and verifies that the initial state is "Logged Out".
        """
        self.authentication = UserAuthentication()
        self.assertEqual(self.authentication.state, "Logged Out")

    def test_login(self):
        """
        Tests logging in from the "Logged Out" state.
        Verifies that the state changes to "Logged In".
        """
        result = self.authentication.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.authentication.state, "Logged In")

    def test_logout(self):
        """
        Tests logging out from the "Logged In" state.
        Verifies that the state changes back to "Logged Out".
        """
        self.authentication.login()
        result = self.authentication.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.authentication.state, "Logged Out")

    def test_login_invalid(self):
        """
        Tests attempting to log in while already logged in.
        Verifies that the operation is rejected and the state remains unchanged.
        """
        self.authentication.login()
        result = self.authentication.login()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.authentication.state, "Logged In")

    def test_logout_invalid(self):
        """
        Tests attempting to log out while already logged out.
        Verifies that the operation is rejected and the state remains unchanged.
        """
        result = self.authentication.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.authentication.state, "Logged Out")


# 25
class TestDocumentEditingSystem(unittest.TestCase):
    """
    White-box unit test class for the DocumentEditingSystem.
    It validates correct transitions between "Editing" and "Saved"
    states, including invalid operations.
    """

    def setUp(self):
        """
        Creates a new DocumentEditingSystem instance before each test
        and verifies that the initial state is "Editing".
        """
        self.document = DocumentEditingSystem()
        self.assertEqual(self.document.state, "Editing")

    def test_save_document_from_editing(self):
        """
        Tests saving the document while in "Editing" state.
        Verifies that the state changes to "Saved".
        """
        result = self.document.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.document.state, "Saved")

    def test_save_document_invalid(self):
        """
        Tests attempting to save the document when already in "Saved" state.
        Verifies that the operation is rejected and the state remains unchanged.
        """
        self.document.save_document()
        result = self.document.save_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.document.state, "Saved")

    def test_edit_document_from_saved(self):
        """
        Tests resuming editing from the "Saved" state.
        Verifies that the state changes back to "Editing".
        """
        self.document.save_document()
        result = self.document.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.document.state, "Editing")

    def test_edit_document_invalid(self):
        """
        Tests attempting to edit the document while already in "Editing" state.
        Verifies that the operation is rejected and the state remains unchanged.
        """
        result = self.document.edit_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.document.state, "Editing")


# 26
class TestElevatorSystem(unittest.TestCase):
    """
    White-box unit test class for the ElevatorSystem.
    It validates valid and invalid transitions between "Idle",
    "Moving Up", and "Moving Down" states.
    """

    def setUp(self):
        """
        Creates a new ElevatorSystem instance before each test
        and verifies that the initial state is "Idle".
        """
        self.elevator = ElevatorSystem()
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_from_idle(self):
        """
        Tests moving the elevator up from the "Idle" state.
        Verifies that the state changes to "Moving Up".
        """
        result = self.elevator.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_down_from_idle(self):
        """
        Tests moving the elevator down from the "Idle" state.
        Verifies that the state changes to "Moving Down".
        """
        result = self.elevator.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_stop_from_moving_up(self):
        """
        Tests stopping the elevator while moving up.
        Verifies that the state returns to "Idle".
        """
        self.elevator.move_up()
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_from_moving_down(self):
        """
        Tests stopping the elevator while moving down.
        Verifies that the state returns to "Idle".
        """
        self.elevator.move_down()
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_invalid(self):
        """
        Tests attempting to move up while already moving up.
        Verifies that the operation is rejected and state remains unchanged.
        """
        self.elevator.move_up()
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_down_invalid(self):
        """
        Tests attempting to move down while already moving down.
        Verifies that the operation is rejected and state remains unchanged.
        """
        self.elevator.move_down()
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_stop_invalid(self):
        """
        Tests attempting to stop the elevator while in "Idle" state.
        Verifies that the operation is rejected and state remains unchanged.
        """
        result = self.elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")


class TestBankAccount(unittest.TestCase):
    """
    Tests for BankAccount
    """

    def test_init_sets_account_number(self):
        """
        Constructor correctly assigns account_number.
        """
        account = BankAccount("ACC001", 500)
        self.assertEqual(account.account_number, "ACC001")

    def test_init_sets_balance(self):
        """Constructor correctly assigns balance."""
        account = BankAccount("ACC001", 500)
        self.assertEqual(account.balance, 500)

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_account_prints_correctly(self, mock_stdout):
        """
        view_account prints account_number and balance.
        """
        account = BankAccount("ACC001", 500)
        account.view_account()
        output = mock_stdout.getvalue()
        self.assertIn("ACC001", output)
        self.assertIn("500", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_account_zero_balance(self, mock_stdout):
        """
        view_account prints correctly with zero balance
        """
        account = BankAccount("ACC002", 0)
        account.view_account()
        self.assertIn("0", mock_stdout.getvalue())


class TestBankingSystem(unittest.TestCase):
    """
    Tests for BankingSystem
    """

    def setUp(self):
        self.bs = BankingSystem()

    def test_init_state(self):
        """
        Constructor sets users dict and empty logged_in_users set.
        """
        self.assertIn("user123", self.bs.users)
        self.assertIsInstance(self.bs.logged_in_users, set)
        self.assertEqual(len(self.bs.logged_in_users), 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_auth_unknown_user_returns_false(self, mock_stdout):
        """
        Unknown username -> Authentication failed, returns False.
        """
        self.assertFalse(self.bs.authenticate("unknown", "pass123"))
        self.assertIn("Authentication failed.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_auth_wrong_password_returns_false(self, mock_stdout):
        """
        Wrong password -> Authentication failed, returns False.
        """
        self.assertFalse(self.bs.authenticate("user123", "wrong"))
        self.assertIn("Authentication failed.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_auth_valid_credentials_returns_true(self, _mock_stdout):
        """
        Valid credentials -> added to logged_in_users, returns True.
        """
        self.assertTrue(self.bs.authenticate("user123", "pass123"))
        self.assertIn("user123", self.bs.logged_in_users)

    @patch("sys.stdout", new_callable=StringIO)
    def test_auth_already_logged_in_returns_false(self, mock_stdout):
        """
        Already logged in -> prints message, returns False.
        """
        self.bs.logged_in_users.add("user123")
        self.assertFalse(self.bs.authenticate("user123", "pass123"))
        self.assertIn("User already logged in.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_sender_not_authenticated(self, mock_stdout):
        """
        Sender not logged in -> returns False.
        """
        self.assertFalse(self.bs.transfer_money("ghost", "receiver", 100, "regular"))
        self.assertIn("Sender not authenticated.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_invalid_transaction_type(self, mock_stdout):
        """
        Unknown transaction type -> returns False.
        """
        self.bs.logged_in_users.add("user123")
        self.assertFalse(self.bs.transfer_money("user123", "receiver", 100, "instant"))
        self.assertIn("Invalid transaction type.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_regular_sufficient_funds(self, _mock_stdout):
        """
        Regular transfer, funds OK (500 + 2% fee <= 1000) -> True.
        """
        self.bs.logged_in_users.add("user123")
        self.assertTrue(self.bs.transfer_money("user123", "receiver", 500, "regular"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_express_insufficient_funds(self, mock_stdout):
        """
        Express transfer, funds exceeded (1000 + 5% fee > 1000) -> False.
        """
        self.bs.logged_in_users.add("user123")
        self.assertFalse(self.bs.transfer_money("user123", "receiver", 1000, "express"))
        self.assertIn("Insufficient funds.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_scheduled_sufficient_funds(self, _mock_stdout):
        """
        Scheduled transfer, funds OK (500 + 1% fee <= 1000) -> True.
        """
        self.bs.logged_in_users.add("user123")
        self.assertTrue(self.bs.transfer_money("user123", "receiver", 500, "scheduled"))


class TestProduct(unittest.TestCase):
    """
    Tests for Product
    """

    def test_init_sets_name_and_price(self):
        """
        Constructor assigns name and price.
        """
        p = Product("Apple", 1.5)
        self.assertEqual(p.name, "Apple")
        self.assertEqual(p.price, 1.5)

    def test_init_zero_price(self):
        """
        Constructor accepts zero price.
        """
        self.assertEqual(Product("Free", 0).price, 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_product_prints_and_returns_message(self, mock_stdout):
        """
        view_product prints name/price and returns the message string.
        """
        p = Product("Apple", 1.5)
        msg = p.view_product()
        self.assertIn("Apple", mock_stdout.getvalue())
        self.assertIn("1.5", msg)


class TestShoppingCart(unittest.TestCase):
    """
    Tests for ShoppingCart
    """

    def setUp(self):
        self.cart = ShoppingCart()
        self.p1 = Product("Apple", 2.0)
        self.p2 = Product("Banana", 1.0)

    def test_init_empty_items(self):
        """Constructor initializes an empty items list."""
        self.assertEqual(self.cart.items, [])

    def test_add_new_product_appends(self):
        """
        Adding a new product appends it with given quantity.
        """
        self.cart.add_product(self.p1, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_add_existing_product_increments_quantity(self):
        """
        Adding an existing product updates quantity without duplicating.
        """
        self.cart.add_product(self.p1, 2)
        self.cart.add_product(self.p1, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 5)

    def test_remove_product_decrements_quantity(self):
        """
        Removing fewer units than available decrements quantity.
        """
        self.cart.add_product(self.p1, 5)
        self.cart.remove_product(self.p1, 2)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_exact_quantity_removes_item(self):
        """
        Removing exact quantity eliminates the item from the list.
        """
        self.cart.add_product(self.p1, 3)
        self.cart.remove_product(self.p1, 3)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_exceeding_quantity_removes_item(self):
        """
        Removing more than available also eliminates the item.
        """
        self.cart.add_product(self.p1, 2)
        self.cart.remove_product(self.p1, 10)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_not_in_cart_does_nothing(self):
        """
        Removing a product that isn't in the cart leaves it unchanged.
        """
        self.cart.add_product(self.p1, 3)
        self.cart.remove_product(self.p2, 1)
        self.assertEqual(len(self.cart.items), 1)

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_cart_empty_produces_no_output(self, mock_stdout):
        """
        view_cart on empty cart prints nothing.
        """
        self.cart.view_cart()
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_cart_shows_item_details(self, mock_stdout):
        """
        view_cart prints product name and computed price.
        """
        self.cart.add_product(self.p1, 3)
        self.cart.view_cart()
        output = mock_stdout.getvalue()
        self.assertIn("Apple", output)
        self.assertIn("6.0", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_checkout_computes_correct_total(self, mock_stdout):
        """
        checkout sums all items and prints completion message.
        """
        self.cart.add_product(self.p1, 2)
        self.cart.add_product(self.p2, 4)
        self.cart.checkout()
        output = mock_stdout.getvalue()
        self.assertIn("8.0", output)
        self.assertIn("Checkout completed", output)
