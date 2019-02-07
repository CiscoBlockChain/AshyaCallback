from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def index():
    if (request.method == "GET"):
        return jsonify({"status": "ok"}), 200

    #curl -X POST -d '{"some": "data"}' -H "Content-Type: application/json" localhost:5252
    elif(request.method == "POST"):
        print("json: " , request.json)
        if request.json == None:
            return jsonify({"status": "no json received. send header with Content-Type: application/json or send data"}), 200
        else:
            return jsonify({"status": request.json})
    else:
        return jsonify({"status": "unrecognized method {0}".format(request.method)}), 200

if __name__ == "__main__":
    print ("Script has started...")
    app.run(debug = True,host = '0.0.0.0',port=5252)
