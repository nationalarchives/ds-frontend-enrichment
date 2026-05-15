from flask import Blueprint

bp = Blueprint("js", __name__)

from app.js import routes
