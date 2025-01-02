import calendar
from datetime import datetime


def occasion():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    november_calendar = cal.monthdatescalendar(now.year, 11)
    second_sunday_in_november = [
        day
        for week in november_calendar
        for day in week
        if day.weekday() == calendar.SUNDAY and day.month == 11
    ][1].day
    if month == 11 and day >= 2 and (day <= max(11, second_sunday_in_november)):
        return "remembrance"
    elif month == 1 and day <= 3:
        return "new-year"
    elif month == 2:
        return "progress"
    elif month == 6:
        return "pride"
    elif month == 10:
        return "black-history"
    elif day == 15 and month == 3 and year == 2025:
        return "comic-relief"
    elif day == 22 and month == 4 and year == 2025:
        return "earth-day"
    return ""
