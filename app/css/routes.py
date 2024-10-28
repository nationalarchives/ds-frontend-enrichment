import calendar
from datetime import datetime

from app.css import bp
from app.lib import cache
from flask import make_response, render_template


@bp.route("/logo-adornments.css")
@cache.cached(timeout=3600)  # 1 hour
def logo_adornments_css():
    now = datetime.now()
    now_day = now.day
    now_month = now.month
    now_year = now.year
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    november_calendar_this_year = cal.monthdatescalendar(now.year, 11)
    second_sunday_in_november_this_year = [
        day
        for week in november_calendar_this_year
        for day in week
        if day.weekday() == calendar.SUNDAY and day.month == 11
    ][1].day
    logo_adornment = ""
    if (
        now_month == 11
        and now_day >= 2
        and (now_day <= max(11, second_sunday_in_november_this_year))
    ):
        logo_adornment = "remembrance"
    elif now_month == 2:
        logo_adornment = "progress"
    elif now_month == 6:
        logo_adornment = "pride"
    elif now_month == 10:
        logo_adornment = "black-history"
    elif now_day == 15 and now_month == 3 and now_year == 2025:
        logo_adornment = "comic-relief"
    elif now_day == 22 and now_month == 4 and now_year == 2025:
        logo_adornment = "earth-day"
    css = render_template(
        "css/logo-adornments.css",
        logo_adornment=logo_adornment,
    )
    response = make_response(css)
    response.headers["Content-Type"] = "text/css; charset=UTF-8"
    return response
