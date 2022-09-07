from email import message
import imp
from flask import Flask, jsonify, request
import io
import string
import time
import os
import numpy
import tensorflow as tf
from keras.models import load_model
from flask import Blueprint

bp = Blueprint('chatbot', __name__)

# model = load_model()

def chatbot_response(m):
    return 'This is response'

@bp.route('/chatbot/<msg>')
def get_response(msg):
    res = chatbot_response(msg)
    return jsonify({"message": msg, "response": res})