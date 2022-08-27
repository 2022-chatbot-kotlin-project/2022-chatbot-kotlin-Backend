from flask import Flask, request, jsonify
from .search import search
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config.from_object("project.config.Config")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
app.register_blueprint(search.bp)

class Shelter(db.Model):    # 향후 model.py로 모듈 분리
    __table_name__ = 'shelter'

    index = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    tel1 = db.Column(db.String(100), nullable=False)
    tel2 = db.Column(db.String(100), nullable=True)
    target = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    people = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, region, name, address, tel1, tel2, target, category, people, url, latitude, longitude):
        self.region = region
        self.name = name
        self.address = address
        self.tel1 = tel1
        self.tel2 = tel2
        self.target = target
        self.category = category
        self.people = people
        self.url = url
        self.latitude = latitude
        self.longitude = longitude




@app.route('/')
def hello():
    return "This is a root API page."

@app.route("/map/<keyword>", methods=['GET'])    # 향후 search.py로 모듈 분리
def shelter_search(keyword):
    shelter = Shelter.query.filter(Shelter.category == keyword)
    # shelter_result = shelter_schema.dump(shelter)
    # return shelter_result

if __name__ == '__main__':
    app.run(debug=True)