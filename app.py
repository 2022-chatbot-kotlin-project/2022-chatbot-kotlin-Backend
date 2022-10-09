from xmlrpc.client import ProtocolError
from flask import Flask, jsonify

app = Flask(__name__)
# register Blueprint
from apis.chatbot import bp as chatbot_module
from apis.map_all import bp as map_module
from apis.search import bp as search_module
app.register_blueprint(map_module)
app.register_blueprint(search_module)
app.register_blueprint(chatbot_module)

@app.route('/', methods=['GET'])
def root():
    return "Docker test complete"

@app.errorhandler
def error_page(err):
    return jsonify(error=str(err)), 500


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)