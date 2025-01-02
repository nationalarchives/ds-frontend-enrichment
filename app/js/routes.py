from app.js import bp
from app.lib.cache import cache
from app.lib.occasions import occasion
from flask import make_response, render_template


@bp.route("/logo-adornments.js")
@cache.cached(timeout=3600)  # 1 hour
def logo_adornments_js():
    logo_adornment = occasion()
    js = render_template(
        "js/logo-adornments.js",
        logo_adornment=logo_adornment,
    )
    response = make_response(js)
    response.headers["Content-Type"] = "text/javascript; charset=UTF-8"
    return response
