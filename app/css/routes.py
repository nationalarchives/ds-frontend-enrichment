from app.css import bp
from app.lib.cache import cache
from app.lib.occasions import occasion
from flask import make_response, render_template


@bp.route("/logo-adornments.css")
@cache.cached()
def logo_adornments_css():
    logo_adornment = occasion()
    css = render_template(
        "css/logo-adornments.css",
        logo_adornment=logo_adornment,
    )
    response = make_response(css)
    response.headers["Content-Type"] = "text/css; charset=UTF-8"
    return response
