import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_EN = True  # CSRF (cross site forgery) for signing POST requests to server
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JSONIFY_PRETTYPRINT_REGULAR = False
    JSON_AS_ASCII = False   # Korean Trans for json return
