import calendar
from datetime import datetime

ADORNMENT_DESCRIPTIONS = {
    "fireworks": "Happy New Year!",
    "valentines": "Happy Valentine's Day",
    "pride": "Celebrating Pride Month",
    "black-history": "Celebrating Black History Month",
    "comic-relief": "Celebrating Comic Relief",
    "earth-day": "Celebrating Earth Day",
    "halloween": "Happy Halloween!",
    "christmas": "Merry Christmas!",
}


def occasion(date=None):
    if not isinstance(date, datetime):
        date = datetime.now()
    day = date.day
    month = date.month
    year = date.year
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    november_calendar = cal.monthdatescalendar(date.year, 11)
    second_sunday_in_november = [
        day
        for week in november_calendar
        for day in week
        if day.weekday() == calendar.SUNDAY and day.month == 11
    ][1].day
    if day == 1 and month == 1:
        return "fireworks"
    elif (
        month == 11 and day >= 2 and (day <= max(11, second_sunday_in_november))
    ):
        return "remembrance"
    # elif month == 2:
    #     return "progress"
    elif day == 14 and month == 2:
        return "valentines"
    elif day == 20 and month == 3 and year == 2026:
        return "comic-relief"
    elif day == 22 and month == 4:
        return "earth-day"
    elif month == 6:
        return "pride"
    elif month == 10:
        return "black-history"
    elif day == 31 and month == 11:
        return "halloween"
    # elif month == 12:
    #     return "christmas"
    return ""
