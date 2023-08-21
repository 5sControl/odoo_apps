import json

from typing import Any, Dict

from odoo import http
from odoo.http import Response



def send(request: Dict[Any, Any]) -> Response:
    result: Dict[Any, Any] = json.dumps(request)
    return Response(result, content_type="application/json")


def route(route=None, **kwargs):
    if route is None:
        raise ValueError("Route must not be None")

    if "methods" not in kwargs:
        kwargs["methods"] = ["OPTIONS", "GET"]
    if "type" not in kwargs:
        kwargs["type"] = "http"
    if "auth" not in kwargs:
        kwargs["auth"] = "public"
    if "csrf" not in kwargs:
        kwargs["csrf"] = False

    def wrapper(f):
        return http.route(route, **kwargs)(f)

    return wrapper
