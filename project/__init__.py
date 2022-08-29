from flask import Flask, jsonify
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

    def __repr__(self):
        return "category is %s" % (self.category)

    @property
    def serialize(self):
        return {
            'index': self.index,
            'region': self.region,
            'name': self.name,
            'address': self.address,
            'tel1': self.tel1,
            'tel2': self.tel2,
            'target': self.target,
            'category': self.category,
            'people': self.people,
            'url': self.url,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

        # return jsonify(data)

@app.route('/')
def hello():
    return "This is a root API page."

@app.route("/map/<keyword>")    # 향후 search.py로 모듈 분리
def shelter_search(keyword):
    shelters = Shelter.query.filter(Shelter.category == keyword).all()
    return jsonify(shelters)

if __name__ == '__main__':
    app.run(debug=True)