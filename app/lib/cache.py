from flask import request
from flask_caching import Cache

cache = Cache()


def cache_key_prefix():
    return request.full_path


def cache_key_prefix_logo_adornments():
    return f"{request.base_url}{request.args.get('date', '')}{request.args.get('debug', '')}"
