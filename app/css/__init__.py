from flask import Blueprint

bp = Blueprint("css", __name__)

from app.css import routes  # noqa: E402,F401
