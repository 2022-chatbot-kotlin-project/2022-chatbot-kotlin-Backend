from flask import jsonify, Blueprint

bp = Blueprint('chatbot', __name__, url_prefix='/api/v1')

# model = load_model()

def chatbot_response(m):
    return m

@bp.route('/chatbot/<msg>')
def get_response(msg):
    res = chatbot_response(msg)
    return jsonify({"message": msg, "response": res})