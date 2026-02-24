# -*- coding: utf-8 -*-
# pylint: disable=missing-function-docstring

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


class TestWhiteBox1(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBox2(unittest.TestCase):
    """
    White-box unittest class.
    """

    # 1
    def test_check_number_status_positive(self):
        self.assertEqual(check_number_status(1), "Positive")

    def test_check_number_status_negative(self):
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_status_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    # 2
    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Abcdef1!"))

    def test_validate_password_invalid_length(self):
        self.assertFalse(validate_password("Ab1!"))

    def test_validate_password_missing_uppercase(self):
        self.assertFalse(validate_password("abcdef1!"))

    def test_validate_password_missing_lowercase(self):
        self.assertFalse(validate_password("ABCDEF1!"))

    def test_validate_password_missing_digit(self):
        self.assertFalse(validate_password("ABCDEFG!"))

    def test_validate_password_missing_special_character(self):
        self.assertFalse(validate_password("ABCDEF12"))

    # 3
    def test_calculate_total_discount_no_discount(self):
        self.assertEqual(calculate_total_discount(99.9), 0)

    def test_calculate_total_discount_ten_percent_1(self):
        self.assertEqual(calculate_total_discount(100), 10)

    def test_calculate_total_discount_ten_percent_2(self):
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_twenty_percent(self):
        self.assertEqual(calculate_total_discount(500.1), 100.02000000000001)


class TestWhiteBox3(unittest.TestCase):
    """
    White-box unittest class.
    """

    # 4
    def test_calculate_order_total_all_ranges(self):
        items = [
            {"quantity": 5, "price": 10},
            {"quantity": 6, "price": 10},
            {"quantity": 10, "price": 10},
            {"quantity": 11, "price": 10},
        ]
        total = calculate_order_total(items)
        expected = (5 * 10) + (0.95 * 6 * 10) + (0.95 * 10 * 10) + (0.9 * 11 * 10)
        self.assertEqual(total, expected)

    # 5
    def test_calculate_items_shipping_cost_standard_1(self):
        items = [{"weight": 3}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_2(self):
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_3(self):
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_4(self):
        items = [{"weight": 11}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_1(self):
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_2(self):
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_3(self):
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_4(self):
        items = [{"weight": 11}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_invalid_method(self):
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 1}], "fast")

    # 6
    def test_validate_login_success(self):
        self.assertEqual(
            validate_login("user1", "password"),
            "Login Successful",
        )

    def test_validate_login_fail_1(self):
        self.assertEqual(
            validate_login("user1", "passwor"),
            "Login Failed",
        )

    def test_validate_login_fail_2(self):
        self.assertEqual(
            validate_login("user", "password"),
            "Login Failed",
        )


class TestWhiteBox4(unittest.TestCase):
    """
    White-box unittest class.
    """

    # 7
    def test_verify_age_eligible_1(self):
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_eligible_2(self):
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_not_eligible_1(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_not_eligible_2(self):
        self.assertEqual(verify_age(66), "Not Eligible")

    # 8
    def test_categorize_product_all_categories(self):
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")
        self.assertEqual(categorize_product(1), "Category D")

    # 9
    def test_validate_email_valid(self):
        self.assertEqual(
            validate_email("test@email.com"),
            "Valid Email",
        )

    def test_validate_email_invalid_length(self):
        self.assertEqual(
            validate_email("a@.c"),
            "Invalid Email",
        )

    def test_validate_email_without_at(self):
        self.assertEqual(
            validate_email("test.com"),
            "Invalid Email",
        )

    def test_validate_email_without_dot(self):
        self.assertEqual(
            validate_email("test@com"),
            "Invalid Email",
        )

    # 10
    def test_celsius_to_fahrenheit_valid_1(self):
        self.assertEqual(celsius_to_fahrenheit(-100), -148)

    def test_celsius_to_fahrenheit_valid_2(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_invalid_1(self):
        self.assertEqual(
            celsius_to_fahrenheit(-101),
            "Invalid Temperature",
        )

    def test_celsius_to_fahrenheit_invalid_2(self):
        self.assertEqual(
            celsius_to_fahrenheit(101),
            "Invalid Temperature",
        )

    # 11
    def test_validate_credit_card_valid(self):
        self.assertEqual(
            validate_credit_card("1234567890123"),
            "Valid Card",
        )

    def test_validate_credit_card_invalid(self):
        self.assertEqual(
            validate_credit_card("1234567890abc"),
            "Invalid Card",
        )


class TestWhiteBox5(unittest.TestCase):
    """
    White-box unittest class.
    """

    # 12
    def test_validate_date_valid(self):
        self.assertEqual(
            validate_date(2026, 2, 23),
            "Valid Date",
        )

    def test_validate_date_invalid_1(self):
        self.assertEqual(
            validate_date(1800, 12, 20),
            "Invalid Date",
        )

    def test_validate_date_invalid_2(self):
        self.assertEqual(
            validate_date(2020, 13, 20),
            "Invalid Date",
        )

    def test_validate_date_invalid_3(self):
        self.assertEqual(
            validate_date(2020, 12, 40),
            "Invalid Date",
        )

    # 13
    def test_check_flight_eligibility_by_age(self):
        self.assertEqual(
            check_flight_eligibility(18, False),
            "Eligible to Book",
        )

    def test_check_flight_eligibility_by_frequent_flyer(self):
        self.assertEqual(
            check_flight_eligibility(16, True),
            "Eligible to Book",
        )

    def test_check_flight_eligibility_not_eligible(self):
        self.assertEqual(
            check_flight_eligibility(16, False),
            "Not Eligible to Book",
        )

    # 14
    def test_validate_url_valid_http(self):
        self.assertEqual(
            validate_url("http://example.com"),
            "Valid URL",
        )

    def test_validate_url_valid_https(self):
        self.assertEqual(
            validate_url("https://example.com"),
            "Valid URL",
        )

    def test_validate_url_invalid(self):
        self.assertEqual(
            validate_url("ftp://example.com"),
            "Invalid URL",
        )

    # 15
    def test_calculate_quantity_discount(self):
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(calculate_quantity_discount(0), "10% Discount")

    # 16
    def test_check_file_size(self):
        self.assertEqual(
            check_file_size(0),
            "Valid File Size",
        )
        self.assertEqual(
            check_file_size(1048576),
            "Valid File Size",
        )
        self.assertEqual(
            check_file_size(1048577),
            "Invalid File Size",
        )
        self.assertEqual(
            check_file_size(-1),
            "Invalid File Size",
        )


class TestWhiteBox6(unittest.TestCase):
    """
    White-box unittest class.
    """

    # 17
    def test_check_loan_eligibility_all_paths(self):
        self.assertEqual(
            check_loan_eligibility(29999.99, 800),
            "Not Eligible",
        )
        self.assertEqual(
            check_loan_eligibility(30000, 701),
            "Standard Loan",
        )
        self.assertEqual(
            check_loan_eligibility(60000, 750),
            "Standard Loan",
        )
        self.assertEqual(
            check_loan_eligibility(30000, 700),
            "Secured Loan",
        )
        self.assertEqual(
            check_loan_eligibility(60000, 700),
            "Secured Loan",
        )
        self.assertEqual(
            check_loan_eligibility(70000, 751),
            "Premium Loan",
        )

    # 18
    def test_calculate_shipping_cost(self):
        self.assertEqual(
            calculate_shipping_cost(1, 10, 10, 10),
            5,
        )
        self.assertEqual(
            calculate_shipping_cost(5, 11, 30, 30),
            10,
        )
        self.assertEqual(
            calculate_shipping_cost(10, 50, 50, 50),
            20,
        )

    # 19
    def test_grade_quiz(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(3, 5), "Fail")

    # 20
    def test_authenticate_user(self):
        self.assertEqual(
            authenticate_user("admin", "admin123"),
            "Admin",
        )
        self.assertEqual(
            authenticate_user("usuario1", "password1"),
            "User",
        )
        self.assertEqual(
            authenticate_user("usuario1", "admin123"),
            "User",
        )
        self.assertEqual(
            authenticate_user("user1", "pass"),
            "Invalid",
        )
        self.assertEqual(
            authenticate_user("usr", "password1"),
            "Invalid",
        )
        self.assertEqual(
            authenticate_user("usr", "pass"),
            "Invalid",
        )

    # 21
    def test_get_weather_advisory(self):
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )
        self.assertEqual(
            get_weather_advisory(-1, 50),
            "Low Temperature. Bundle Up!",
        )
        self.assertEqual(
            get_weather_advisory(20, 50),
            "No Specific Advisory",
        )
