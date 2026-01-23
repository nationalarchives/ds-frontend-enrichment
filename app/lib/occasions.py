import calendar
from datetime import datetime


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
        return ("fireworks", "Happy New Year")
    elif day == 14 and month == 2:
        return ("valentines", "Happy Valentine's Day")
    # elif month == 2:
    #     return ("progress", "Celebrating Progress")
    elif day == 5 and month == 3 and year == 2026:
        return ("world-book-day", "Celebrating World Book Day")
    elif day == 20 and month == 3 and year == 2026:
        return ("comic-relief", "Celebrating Comic Relief")
    elif day == 22 and month == 4:
        return ("earth-day", "Celebrating Earth Day")
    elif month == 6:
        return ("pride", "Celebrating Pride Month")
    elif day == 31 and month == 10:
        return ("halloween", "Happy Halloween")
    elif month == 10:
        return ("black-history", "Celebrating Black History Month")
    elif (
        month == 11 and day >= 2 and (day <= max(11, second_sunday_in_november))
    ):
        return ("remembrance", "Lest We Forget")
    elif month == 12 and day <= 25:
        return ("christmas", "Merry Christmas")
    return ("", "")
