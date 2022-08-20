from flask import Flask
from . import search

app = Flask(__name__)

app.register_blueprint(search.bp)

@app.route('/')
def hello():
    return "왜안돼"