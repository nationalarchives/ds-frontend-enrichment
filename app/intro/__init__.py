from flask import Blueprint

bp = Blueprint("intro", __name__)

from app.intro import routes  # noqa: E402,F401
