from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object("project.config.Config")

from project.chatbot.chatbot import bp as chatbot_module
from project.views.map import bp as map_module
# register Blueprint
app.register_blueprint(map_module)
app.register_blueprint(chatbot_module)


@app.route('/')
def hello():
    return "This is a root API page."


@app.errorhandler
def error_page(err):
    return jsonify(error=str(err)), 500


if __name__ == '__main__':
    app.run(debug=True)