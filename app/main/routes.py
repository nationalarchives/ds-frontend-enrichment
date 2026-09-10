from calendar import monthrange
from datetime import UTC, datetime

from tna_utilities.flask import cacheable_duration

from app.lib.occasions import occasion
from app.main import bp


@bp.route("/occasions.json")
@cacheable_duration(86400)
def occasions_json():
    occasions_list = []
    year = datetime.now(UTC).year
    for month in range(1, 13):
        for day in range(monthrange(year, month)[1]):
            date = datetime(year, month, day + 1, tzinfo=UTC)
            logo_adornment, logo_adornment_description = occasion(date)
            if logo_adornment and logo_adornment_description:
                occasions_list.append(
                    {
                        "date": f"{year}-{month:02d}-{day + 1:02d}",
                        "logo_adornment_class": logo_adornment,
                        "logo_adornment_description": logo_adornment_description,
                    }
                )
            else:
                occasions_list.append(
                    {
                        "date": f"{year}-{month:02d}-{day + 1:02d}",
                        "logo_adornment_class": None,
                        "logo_adornment_description": None,
                    }
                )
    return occasions_list
