from datetime import UTC, datetime

from flask import make_response, render_template, request
from tna_utilities.flask import cacheable_duration_cloudfront

from app.js import bp
from app.lib.occasions import occasion


@bp.route("/logo-adornments.js")
@cacheable_duration_cloudfront(21600, 3600)
def logo_adornments_js():
    date = request.args.get("debug", None)
    if date:
        date = datetime.strptime(date, "%Y-%m-%d").astimezone(UTC)
    logo_adornment, logo_adornment_description = occasion(date)
    js = render_template(
        "js/logo-adornments.js.jinja",
        logo_adornment=logo_adornment,
        logo_adornment_description=logo_adornment_description,
    )
    response = make_response(js)
    response.headers["Content-Type"] = "text/javascript; charset=UTF-8"
    return response
