# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
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
