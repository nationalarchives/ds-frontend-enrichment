import datetime
from calendar import monthrange

from app.lib.cache import cache, cache_key_prefix
from app.lib.occasions import occasion
from app.main import bp


@bp.route("/occasions.json")
@cache.cached(key_prefix=cache_key_prefix)
def occasions_json():
    occasions_list = []
    year = datetime.datetime.now().year
    for month in range(1, 13):
        for day in range(monthrange(year, month)[1]):
            date = datetime.datetime(year, month, day + 1)
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
