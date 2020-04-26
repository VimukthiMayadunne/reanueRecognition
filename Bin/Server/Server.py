from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/getTreatment/", methods=['GET', 'POST'])
def treatment():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200

    if request.method == 'POST':
        data = request.form
        return jsonify(isError=False, message="Success", statusCode=200, data=data), 200
