from datetime import datetime

from flask import make_response, render_template, request
from tna_utilities.flask import cacheable_duration_cloudfront

from app.css import bp
from app.lib.occasions import occasion


@bp.route("/logo-adornments.css")
@cacheable_duration_cloudfront(21600, 3600)
def logo_adornments_css():
    date = request.args.get("debug", None)
    if date:
        date = datetime.strptime(date, "%Y-%m-%d")
    logo_adornment, logo_adornment_description = occasion(date)
    css = render_template(
        "css/logo-adornments.css.jinja",
        logo_adornment=logo_adornment,
        logo_adornment_description=logo_adornment_description,
    )
    response = make_response(css)
    response.headers["Content-Type"] = "text/css; charset=UTF-8"
    return response
