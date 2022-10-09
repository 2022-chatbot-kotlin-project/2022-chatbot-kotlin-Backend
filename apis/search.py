import json
from sqlalchemy import or_, and_
from flask import Blueprint, request
from models.shelter import Shelter

bp = Blueprint('search', __name__, url_prefix='/api/v1/search')


@bp.route("/shelter")    # 향후 views.py로 모듈 분리
def shelter_search():
    sh_gender = request.args.get('gender', None)
    sh_type = request.args.get('type', None)
    print("type : {} / gender : {}".format(sh_type, sh_gender))

    filters = []

    if sh_type:
        filters.append(Shelter.type.like("%{}%".format(sh_type)))

    if sh_gender:
        if sh_gender == 'Y':
            sh_gender = '여자'
        elif sh_gender == 'N':
            sh_gender = '남자'
        else:
            sh_gender = '공용'
        filters.append(Shelter.target == sh_gender)

    qry = Shelter.query.filter(*filters).order_by(Shelter.idx)
    print('length: ', qry.count())

    data = [{"index": q.idx, "region": q.addr, "name": q.name, "address": q.addr, "tel1": q.phone1, "tel2": q.phone2,
             "target": q.target, "category": q.type, "people": q.limit, "url": q.url,
             "latitude": q.lat, "longitude": q.lng} for q in qry]
    return json.dumps({'status': 200, 'length': len(data), 'data': data}), 200