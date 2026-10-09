import unittest

from pocketlib.duration import format_duration, parse_duration


class ParseDurationTest(unittest.TestCase):
    def test_hours_and_minutes(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_seconds(self):
        self.assertEqual(parse_duration("45s"), 45)

    def test_rejects_unknown_unit(self):
        with self.assertRaises(ValueError):
            parse_duration("3w")


class FormatDurationTest(unittest.TestCase):
    def test_hours_and_minutes(self):
        self.assertEqual(format_duration(5400), "1h 30m")

    def test_seconds(self):
        self.assertEqual(format_duration(59), "59s")

    def test_days_and_hours(self):
        self.assertEqual(format_duration(90000), "1d 1h")

    def test_exact_day(self):
        self.assertEqual(format_duration(86400), "1d")

    def test_zero(self):
        self.assertEqual(format_duration(0), "0s")
