from flask import Flask, request, jsonify
from Bin.Server.serverInput import appendData

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/getTreatment/", methods=['GET', 'POST'])
def treatment():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200

    if request.method == 'POST':
        data = request.json
        results = appendData(data)
        return jsonify(isError=False, message="Success", statusCode=200, data=results), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
