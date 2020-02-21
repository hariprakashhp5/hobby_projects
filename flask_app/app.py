
import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from flask import Flask, request, jsonify
from flask_app.modules.model_factory import get_model

app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    model = get_model(request)
    prediction = model.get_prediction()
    return jsonify(prediction)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=3039)
