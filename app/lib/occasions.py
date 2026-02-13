import calendar
from datetime import datetime


def occasion(date=None):  # noqa: max-complexity
    if not isinstance(date, datetime):
        date = datetime.now()

    day = date.day
    month = date.month
    year = date.year

    cal = calendar.Calendar(firstweekday=calendar.MONDAY)

    if month == 1:
        if day == 1:
            return ("fireworks", "Happy New Year")

    if month == 2:
        if day == 14:
            return ("heart", "Happy Valentine's Day")
        # return ("progress", "Celebrating Progress")

    if month == 3:
        march_calendar = cal.monthdatescalendar(date.year, 3)
        first_thursday_in_march = [
            day
            for week in march_calendar
            for day in week
            if day.weekday() == calendar.THURSDAY and day.month == 3
        ][0].day

        if day == first_thursday_in_march:
            return ("world-book-day", "Celebrating World Book Day")
        if day == 8:
            return ("womens-day", "Celebrating International Women’s Day")
        if day == 20 and year == 2026:
            return ("comic-relief", "Celebrating Comic Relief")
        if day >= 16 and day <= 20 and year == 2026:
            return ("neurodiversity", "Neurodiversity Celebration Week")

    if month == 4:
        if day == 22:
            return ("earth-day", "Celebrating Earth Day")
        if day == 27 and year == 2026:
            return ("london-marathon", "The London Marathon")

    if month == 5:
        if day == 12:
            return ("nurses", "Celebrating International Nurses Day")
        if day == 20:
            return ("bee", "Celebrating World Bee Day")

    if month == 6:
        june_calendar = cal.monthdatescalendar(date.year, 6)
        second_saturday_in_june = [
            day
            for week in june_calendar
            for day in week
            if day.weekday() == calendar.SATURDAY and day.month == 6
        ][1].day

        if day == 3:
            return ("bike", "Celebrating World Bicycle Day")
        if day == 5:
            return ("environment", "Celebrating World Environment Day")
        if day == second_saturday_in_june:
            return ("trooping-colour", "Trooping the Colour")
        return ("pride", "Celebrating Pride Month")

    if month == 7:
        if day == 2:
            return ("ufo", "Celebrating World UFO Day")
        if day >= 20 and day <= 25 and year == 2026:
            return ("shark", "Celebrating Shark Week")

    if month == 8:
        if day == 19:
            return ("photography", "Celebrating World Photography Day")

    if month == 9:
        if day == 29:
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
        november_calendar = cal.monthdatescalendar(date.year, 11)
        second_sunday_in_november = [
            day
            for week in november_calendar
            for day in week
            if day.weekday() == calendar.SUNDAY and day.month == 11
        ][1].day

        if day >= 2 and (day <= max(11, second_sunday_in_november)):
            return ("remembrance", "Lest We Forget")

    if month == 12:
        if day <= 25:
            return ("christmas", "Merry Christmas")

    return ("", "")
