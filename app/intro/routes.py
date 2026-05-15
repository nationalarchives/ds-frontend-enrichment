from flask import render_template

from app.intro import bp
from app.lib.cache import cache, cache_key_prefix


@bp.route("/")
@cache.cached(key_prefix=cache_key_prefix)
def index():
    return render_template("intro/index.html")
