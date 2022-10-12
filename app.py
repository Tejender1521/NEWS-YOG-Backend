import json

from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from mordecai import Geoparser
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



def geoparse():
    geo = Geoparser()
    def fetch_geo():
        return geo
    return fetch_geo


geo_instance = geoparse()

@app.post("/mordecai")
@cross_origin()
def hello_world():
    geo = geo_instance()
    data = request.get_json(force=True)
    text = data["key"]
    result = geo.geoparse(text)
    result = json.dumps(str(result))
    # print(type(result))
    
    response = app.response_class(
        response= result,
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)
