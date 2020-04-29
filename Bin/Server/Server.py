from flask import Flask, request, jsonify
from Bin.Support.sendCsv import sendCsv

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
        return sendCsv(results, 'results.csv', ['Name', 'Time', 'DrCr', 'AccountName', 'Amount'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
