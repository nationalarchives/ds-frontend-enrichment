from flask import render_template

from app.intro import bp


@bp.route("/")
def index():
    return render_template("intro/index.html")
