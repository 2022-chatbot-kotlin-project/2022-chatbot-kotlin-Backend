from flask import Flask
from .search import search
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")

app.register_blueprint(search.bp)

@app.route('/')
def hello():
    return "왜안돼"