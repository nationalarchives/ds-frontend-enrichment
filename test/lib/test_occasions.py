import datetime
import unittest

from app.lib.occasions import occasion


def get_date_to_test(day_to_test, month_to_test):
    now = datetime.datetime.now()
    current_day = now.day
    current_month = now.month
    current_year = now.year

    if month_to_test < current_month or (
        month_to_test == current_month and day_to_test < current_day
    ):
        print(f"Testing date: {day_to_test}/{month_to_test}, using next year")
        return datetime.datetime(current_year + 1, month_to_test, day_to_test)

    print(f"Testing date: {day_to_test}/{month_to_test}, using current year")
    return datetime.datetime(current_year, month_to_test, day_to_test)


class MainBlueprintTestCase(unittest.TestCase):
    def test_occasions_january(self):
        self.assertEqual(
            occasion(get_date_to_test(1, 1)), ("fireworks", "Happy New Year")
        )
        self.assertEqual(occasion(get_date_to_test(2, 1)), ("", ""))

    def test_occasions_february(self):
        # self.assertEqual(occasion(get_date_to_test(1, 2)), ("progress", "Celebrating Progress"))
        self.assertEqual(
            occasion(get_date_to_test(14, 2)),
            ("heart", "Happy Valentine's Day"),
        )
        # self.assertEqual(occasion(get_date_to_test(28, 2)), ("progress", "Celebrating Progress"))

    def test_occasions_march(self):
        self.assertEqual(
            occasion(get_date_to_test(5, 3)),
            ("world-book-day", "Celebrating World Book Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(8, 3)),
            ("womens-day", "Celebrating International Women’s Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(16, 3)),
            ("neurodiversity", "Neurodiversity Celebration Week"),
        )
        self.assertEqual(
            occasion(get_date_to_test(19, 3)),
            ("neurodiversity", "Neurodiversity Celebration Week"),
        )
        self.assertEqual(
            occasion(get_date_to_test(20, 3)),
            ("comic-relief", "Celebrating Comic Relief"),
        )

    def test_occasions_april(self):
        self.assertEqual(
            occasion(get_date_to_test(22, 4)),
            ("earth-day", "Celebrating Earth Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(27, 4)),
            ("london-marathon", "The London Marathon"),
        )

    def test_occasions_may(self):
        self.assertEqual(
            occasion(get_date_to_test(12, 5)),
            ("nurses", "Celebrating International Nurses Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(20, 5)),
            ("bee", "Celebrating World Bee Day"),
        )

    def test_occasions_june(self):
        self.assertEqual(
            occasion(get_date_to_test(1, 6)),
            ("pride", "Celebrating Pride Month"),
        )
        self.assertEqual(
            occasion(get_date_to_test(3, 6)),
            ("bike", "Celebrating World Bicycle Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(5, 6)),
            ("environment", "Celebrating World Environment Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(30, 6)),
            ("pride", "Celebrating Pride Month"),
        )

    def test_occasions_july(self):
        self.assertEqual(
            occasion(get_date_to_test(2, 7)),
            ("ufo", "Celebrating World UFO Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(20, 7)),
            ("shark", "Celebrating Shark Week"),
        )
        self.assertEqual(
            occasion(get_date_to_test(25, 7)),
            ("shark", "Celebrating Shark Week"),
        )

    def test_occasions_august(self):
        self.assertEqual(
            occasion(get_date_to_test(19, 8)),
            ("photography", "Celebrating World Photography Day"),
        )

    def test_occasions_september(self):
        self.assertEqual(
            occasion(get_date_to_test(29, 9)),
            ("heart", "Celebrating World Heart Day"),
        )

    def test_occasions_october(self):
        self.assertEqual(
            occasion(get_date_to_test(1, 10)),
            ("black-history", "Celebrating Black History Month"),
        )
        # self.assertEqual(
        #     occasion(get_date_to_test(3, 10)),
        #     ("carrot", "Celebrating British Carrot Day"),
        # )
        self.assertEqual(
            occasion(get_date_to_test(4, 10)),
            ("animal", "Celebrating World Animal Day"),
        )
        self.assertEqual(
            occasion(get_date_to_test(30, 10)),
            ("black-history", "Celebrating Black History Month"),
        )
        self.assertEqual(
            occasion(get_date_to_test(31, 10)), ("halloween", "Happy Halloween")
        )

    def test_occasions_november(self):
        self.assertEqual(occasion(get_date_to_test(1, 11)), ("", ""))
        self.assertEqual(
            occasion(get_date_to_test(2, 11)), ("remembrance", "Lest We Forget")
        )
        self.assertEqual(
            occasion(get_date_to_test(8, 11)), ("remembrance", "Lest We Forget")
        )
        self.assertEqual(occasion(get_date_to_test(15, 11)), ("", ""))

    def test_occasions_december(self):
        self.assertEqual(
            occasion(get_date_to_test(1, 12)), ("christmas", "Merry Christmas")
        )
        self.assertEqual(
            occasion(get_date_to_test(25, 12)), ("christmas", "Merry Christmas")
        )
        self.assertEqual(occasion(get_date_to_test(26, 12)), ("", ""))
