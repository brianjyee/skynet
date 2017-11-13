from flask import Blueprint, Response


home = Blueprint('home', __name__, url_prefix='/')


@home.route('/', methods=["GET"])
def index():
    """Send a string to let the user know the service is running"""
    return Response("Skynet has become self aware", status=200, mimetype="text/plain")
