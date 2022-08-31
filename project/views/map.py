from flask import Blueprint, request, jsonify
from project.models.shelter import Shelter

bp = Blueprint('views', __name__, url_prefix='/map')


@bp.route("/<type>")    # 향후 views.py로 모듈 분리
def shelter_search(type):
    print("type : ", type)
    qry = Shelter.query.filter_by(type=type).all()
    print(len(qry))
    data = [{"index": q.idx, "region": q.addr, "name": q.name, "address": q.addr, "tel1": q.phone1, "tel2": q.phone2,
             "target": q.target, "category": q.type, "people": q.limit, "url": q.url,
             "latitude": q.lat, "longitude": q.lng} for q in qry]
    print(data)
    return jsonify(data)

