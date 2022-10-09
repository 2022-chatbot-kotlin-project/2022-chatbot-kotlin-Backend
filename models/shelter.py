# from models.database import db
# db.metadata.clear()  # for redefine objects

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shelter(db.Model):
    __tablename__ = 'TB_SHELTER_INFO'

    idx = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    phone1 = db.Column(db.String(100), nullable=False)
    phone2 = db.Column(db.String(100), nullable=True)
    target = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    limit = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {key: val for key, val in self.__dict__.itmes()}