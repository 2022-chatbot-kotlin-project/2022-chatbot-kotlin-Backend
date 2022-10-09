import json
from flask import Blueprint
from models.shelter import Shelter

bp = Blueprint('map', __name__, url_prefix='/api/v1/map')

@bp.route("/all")
def get_all_shelters():
    qry = Shelter.query.all()
    data = [{"index": q.idx, "region": q.addr, "name": q.name, "address": q.addr, "tel1": q.phone1, "tel2": q.phone2,
             "target": q.target, "category": q.type, "people": q.limit, "url": q.url,
             "latitude": q.lat, "longitude": q.lng} for q in qry]
    return json.dumps({'status': 200, 'length': len(data), 'data': data}), 200
