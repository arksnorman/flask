from flask_cors import CORS
from flask import Flask, jsonify, request
import awsgi

app = Flask(__name__)
CORS(app)

# Constant variable with path prefix
BASE_ROUTE = "/items"

@app.route(BASE_ROUTE, methods=['GET'])
def list_songs():
  return jsonify(message="hello world")


def handler(event, context):
  return awsgi.response(app, event, context)
