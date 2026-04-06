import json


def build_request(url, method="GET", payload=None):
    return {
        "url": url,
        "method": method,
        "payload": payload or {}
    }


def send_request(request):
    # fake request simulation
    return {
        "status": 200,
        "data": {"message": "success"},
        "request": request
    }


def parse_response(response):
    return json.dumps(response, indent=2)


def fetch_user(user_id):
    return send_request(build_request(f"/users/{user_id}"))