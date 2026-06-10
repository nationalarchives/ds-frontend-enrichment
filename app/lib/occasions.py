import calendar
from datetime import datetime


def nth_day_in_month(year, month, weekday, nth):
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    month_calendar = cal.monthdatescalendar(year, month)
    return [
        day
        for week in month_calendar
        for day in week
        if day.weekday() == weekday and day.month == month
    ][nth - 1].day


def occasion(date=None):  # noqa: C901
    if not isinstance(date, datetime):
        date = datetime.now()

    day = date.day
    month = date.month
    year = date.year

    if month == 1 and day == 1:
        return ("fireworks", "Happy New Year")

    if month == 2 and day == 14:
        return ("heart", "Happy Valentine’s Day")
        # return ("progress", "Celebrating Progress")

    if month == 3:
        if day == 1:
            return ("wales", "Celebrating St David’s Day")
        if day == nth_day_in_month(year, month, calendar.THURSDAY, 1):
            return ("world-book-day", "Celebrating World Book Day")
        if day == 8:
            return ("womens-day", "Celebrating International Women’s Day")
        if day == 17:
            return ("union-flag", "Celebrating St Patrick’s Day")
        if day == 27:
            return ("theatre", "Celebrating World Theatre Day")
        # if day == 20 and year == 2026:
        #     return ("comic-relief", "Celebrating Comic Relief")
        # if day >= 16 and day <= 20 and year == 2026:
        #     return ("neurodiversity", "Neurodiversity Celebration Week")

    if month == 4:
        if day == 22:
            return ("earth-day", "Celebrating Earth Day")
        if day == 23:
            return ("england", "Celebrating St George’s Day")
        if day == 25 and year == 2027:
            return ("london-marathon", "The London Marathon")

    if month == 5:
        if day == 12:
            return ("nurses", "Celebrating International Nurses Day")
        if day == 20:
            return ("bee", "Celebrating World Bee Day")

    if month == 6:
        if day == nth_day_in_month(year, month, calendar.SATURDAY, 2):
            return ("crown", "Trooping the Colour")
        # if day == 3:
        #     return ("bike", "Celebrating World Bicycle Day")
        if day == 5:
            return ("environment", "Celebrating World Environment Day")
        if day == 8:
            return ("oceans", "Celebrating Oceans Day")
        return ("pride", "Celebrating Pride Month")

    if month == 7:
        if day == 2:
            return ("ufo", "Celebrating World UFO Day")
        if day >= 6 and day <= 12 and year == 2026:
            return ("shark", "Celebrating Shark Week")

    if month == 8 and day == 19:
        return ("photography", "Celebrating World Photography Day")

    if month == 9 and day == 29:
        return ("heart", "Celebrating World Heart Day")

    if month == 10:
        # if day == 3:
        #     return ("carrot", "Celebrating British Carrot Day")
        if day == 4:
            return ("animal", "Celebrating World Animal Day")
        if day == 31:
            return ("halloween", "Happy Halloween")
        return ("black-history", "Celebrating Black History Month")

    if month == 11:
        if day >= 2 and (
            day <= max(11, nth_day_in_month(year, month, calendar.SUNDAY, 2))
        ):
            return ("remembrance", "Lest We Forget")
        if day == 14:
            return ("union-flag", "Celebrating the birthday of His Majesty The King")
        if day == 30:
            return ("scotland", "Celebrating St Andrew’s Day")

    if month == 12 and day <= 25:
        return ("christmas", "Merry Christmas")

    return ("", "")
