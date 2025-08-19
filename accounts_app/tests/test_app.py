import unittest
from unittest.mock import patch
from datetime import date

import app  # assuming app.py is in the same directory or importable


class TestAppFunctions(unittest.TestCase):
    @patch(
        "app.ACCOUNTS",
        [
            {"id": 1, "name": "Alpha", "home_state": "NY"},
            {"id": 3, "name": "Gamma", "home_state": "CA"},
        ],
    )
    def test_get_account_name(self):
        self.assertEqual(app.get_account_name(1), "Alpha")
        self.assertEqual(app.get_account_name(3), "CA")  # special case
        self.assertEqual(app.get_account_name(99), 0)  # not found

    @patch(
        "app.MONTHLY_RATES",
        [
            {"effective_date": date(2022, 1, 1), "multiplier": 1.0},
            {"effective_date": date(2022, 6, 1), "multiplier": 1.2},
            {"effective_date": date(2023, 1, 1), "multiplier": 1.5},
        ],
    )
    def test_get_multiplier_for_date(self):
        self.assertEqual(app.get_multiplier_for_date(date(2023, 2, 1)), 1.5)
        self.assertEqual(app.get_multiplier_for_date(date(2022, 7, 1)), 1.2)
        self.assertEqual(app.get_multiplier_for_date(date(2022, 1, 15)), 1.0)
        with self.assertRaises(Exception):
            app.get_multiplier_for_date(date(2020, 1, 1))  # before any effective date

    @patch(
        "app.MONTHLY_RATES",
        [
            {"effective_date": date(2022, 1, 1), "multiplier": 2.0},
        ],
    )
    def test_calculate_rate_adjustment(self):
        transactions = [
            {"book_date": date(2022, 2, 1), "value": 100},
            {"book_date": date(2022, 3, 1), "value": 200},
        ]
        self.assertEqual(app.calculate_rate_adjustment(transactions), 600)

    def test_find_out_of_sequence_transactions(self):
        transactions = [
            {"book_date": date(2022, 1, 1)},
            {"book_date": date(2022, 1, 5)},
            {"book_date": date(2021, 12, 31)},  # out-of-sequence
            {"book_date": date(2022, 1, 6)},
        ]
        result = app.find_out_of_sequence_transactions(transactions)
        self.assertEqual(result, [{"book_date": date(2021, 12, 31)}])

        self.assertEqual(
            app.find_out_of_sequence_transactions([]), []
        )  # edge case: empty list


if __name__ == "__main__":
    unittest.main()
