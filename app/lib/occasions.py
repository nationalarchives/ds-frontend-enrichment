import calendar
from datetime import datetime


def occasion(date=None):  # noqa: max-complexity
    if not isinstance(date, datetime):
        date = datetime.now()
    day = date.day
    month = date.month
    year = date.year
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)

    june_calendar = cal.monthdatescalendar(date.year, 6)
    second_saturday_in_june = [
        day
        for week in june_calendar
        for day in week
        if day.weekday() == calendar.SATURDAY and day.month == 6
    ][1].day

    november_calendar = cal.monthdatescalendar(date.year, 11)
    second_sunday_in_november = [
        day
        for week in november_calendar
        for day in week
        if day.weekday() == calendar.SUNDAY and day.month == 11
    ][1].day

    if month == 1 and day == 1:
        return ("fireworks", "Happy New Year")
    elif month == 2 and day == 14:
        return ("heart", "Happy Valentine's Day")
    # elif month == 2:
    #     return ("progress", "Celebrating Progress")
    elif month == 3 and day == 5 and year == 2026:
        return ("world-book-day", "Celebrating World Book Day")
    elif month == 3 and day == 8:
        return ("womens-day", "Celebrating International Women’s Day")
    elif month == 3 and day == 20 and year == 2026:
        return ("comic-relief", "Celebrating Comic Relief")
    elif month == 3 and day >= 16 and day <= 20 and year == 2026:
        return ("neurodiversity", "Neurodiversity Celebration Week")
    elif month == 4 and day == 22:
        return ("earth-day", "Celebrating Earth Day")
    elif month == 4 and day == 27 and year == 2026:
        return ("london-marathon", "The London Marathon")
    elif month == 5 and day == 12:
        return ("nurses", "Celebrating International Nurses Day")
    elif month == 5 and day == 20:
        return ("bee", "Celebrating World Bee Day")
    elif month == 6 and day == 3:
        return ("bike", "Celebrating World Bicycle Day")
    elif month == 6 and day == 5:
        return ("environment", "Celebrating World Environment Day")
    elif month == 6 and day == second_saturday_in_june:
        return ("trooping-colour", "Trooping the Colour")
    elif month == 6:
        return ("pride", "Celebrating Pride Month")
    elif month == 7 and day == 2:
        return ("ufo", "Celebrating World UFO Day")
    elif month == 7 and day >= 20 and day <= 25 and year == 2026:
        return ("shark", "Celebrating Shark Week")
    elif month == 8 and day == 19:
        return ("photography", "Celebrating World Photography Day")
    elif month == 9 and day == 29:
        return ("heart", "Celebrating World Heart Day")
    # elif month == 10 and day == 3:
    #     return ("carrot", "Celebrating British Carrot Day")
    elif month == 10 and day == 4:
        return ("animal", "Celebrating World Animal Day")
    elif month == 10 and day == 31:
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
