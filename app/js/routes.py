from datetime import datetime

from app.js import bp
from app.lib.cache import cache, cache_key_prefix
from app.lib.occasions import ADORNMENT_DESCRIPTIONS, occasion
from flask import make_response, render_template, request


@bp.route("/logo-adornments.js")
@cache.cached(key_prefix=cache_key_prefix)
def logo_adornments_js():
    date = request.args.get("debug", None)
    if date:
        date = datetime.strptime(date, "%Y-%m-%d")
    logo_adornment = occasion(date)
    js = render_template(
        "js/logo-adornments.js.jinja",
        logo_adornment=logo_adornment,
        logo_adornment_description=ADORNMENT_DESCRIPTIONS.get(
            logo_adornment, ""
        ),
    )
    response = make_response(js)
    response.headers["Content-Type"] = "text/javascript; charset=UTF-8"
    return response
