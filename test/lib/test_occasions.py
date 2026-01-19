import datetime
import unittest

from app.lib.occasions import occasion


class MainBlueprintTestCase(unittest.TestCase):
    def test_occasions(self):
        self.assertEqual(occasion(datetime.datetime(2025, 1, 1)), "fireworks")
        self.assertEqual(occasion(datetime.datetime(2025, 1, 2)), "")
        self.assertEqual(occasion(datetime.datetime(2025, 11, 1)), "")
        self.assertEqual(
            occasion(datetime.datetime(2025, 11, 2)), "remembrance"
        )
        self.assertEqual(
            occasion(datetime.datetime(2025, 11, 8)), "remembrance"
        )
        self.assertEqual(occasion(datetime.datetime(2025, 11, 15)), "")
        # self.assertEqual(occasion(datetime.datetime(2025, 2, 1)), "progress")
        # self.assertEqual(occasion(datetime.datetime(2025, 2, 28)), "progress")
        self.assertEqual(occasion(datetime.datetime(2025, 2, 14)), "valentines")
        self.assertEqual(occasion(datetime.datetime(2025, 4, 22)), "earth-day")
        self.assertEqual(occasion(datetime.datetime(2025, 6, 1)), "pride")
        self.assertEqual(occasion(datetime.datetime(2025, 6, 30)), "pride")
        self.assertEqual(
            occasion(datetime.datetime(2025, 10, 1)), "black-history"
        )
        self.assertEqual(
            occasion(datetime.datetime(2025, 10, 31)), "black-history"
        )
        self.assertEqual(
            occasion(datetime.datetime(2026, 3, 20)), "comic-relief"
        )
        self.assertEqual(occasion(datetime.datetime(2026, 11, 31)), "halloween")
        # self.assertEqual(
        #     occasion(datetime.datetime(2026, 12, 1)), "christmas"
        # )
