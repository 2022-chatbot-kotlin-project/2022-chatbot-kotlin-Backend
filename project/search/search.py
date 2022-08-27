from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('search', __name__)
# bp.config.from_object("project.config.Config")

# @bp.route("/map", methods=['GET', 'POST'])   # method가 아니라 methods
# def bptest():
#    return "쉼터 검색 list입니다."