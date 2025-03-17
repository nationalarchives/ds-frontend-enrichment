from datetime import datetime

from app.css import bp
from app.lib.cache import cache, cache_key_prefix
from app.lib.occasions import occasion
from flask import make_response, render_template, request


@bp.route("/logo-adornments.css")
@cache.cached(key_prefix=cache_key_prefix)
def logo_adornments_css():
    date = request.args.get("debug", None)
    if date:
        date = datetime.strptime(date, "%Y-%m-%d")
    logo_adornment = occasion(date)
    css = render_template(
        "css/logo-adornments.css",
        logo_adornment=logo_adornment,
    )
    response = make_response(css)
    response.headers["Content-Type"] = "text/css; charset=UTF-8"
    return response
