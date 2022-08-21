from flask import Blueprint

bp = Blueprint('search', __name__)

@bp.route("/map")
def bptest():
    return "hi"