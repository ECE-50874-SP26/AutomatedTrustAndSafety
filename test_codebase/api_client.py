"""A tiny fake HTTP client used by example code/tests.

This module simulates building and sending requests for testing
purposes; it does not perform real network I/O.
"""

import json


def build_request(url, method="GET", payload=None):
    """Return a dictionary representing an HTTP request.

    `payload` defaults to an empty dict when not provided.
    """
    return {
        "url": url,
        "method": method,
        "payload": payload or {}
    }


def send_request(request):
    """Simulate sending `request` and return a fake response dict."""
    return {
        "status": 200,
        "data": {"message": "success"},
        "request": request
    }


def parse_response(response):
    """Serialize `response` to a pretty-printed JSON string."""
    return json.dumps(response, indent=2)


def fetch_user(user_id):
    """Construct a request for a user resource and send it.

    Returns the simulated response dict.
    """
    return send_request(build_request(f"/users/{user_id}"))