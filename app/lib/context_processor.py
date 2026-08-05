import json
import os
from datetime import datetime
from urllib.parse import unquote

from flask import current_app, request


def now_iso_8601():
    now = datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%SZ")


def cookie_preference(policy):
    if "cookie_preferences" in request.cookies:
        cookie_preferences = request.cookies["cookie_preferences"]
        preferences = json.loads(unquote(cookie_preferences))
        return preferences.get(policy, None)
    return None


def static_file_exists(path):
    return os.path.exists(os.path.join(str(current_app.static_folder), path))
