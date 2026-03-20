from flask import Flask, jsonify, request
from features.weather import get_weather
from features.light_pollution import get_light_pollution

import requests

app = Flask(__name__)

@app.route("/home")
def home():
    return {"status": "Back End on"}

@app.route("/map")
def test():
    return jsonify({
        "message": "API working",
    })

@app.route("/dashboard")


#API work

@app.route("/api/weather")
def weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return jsonify({"error": "Missing coordinates"}), 400

    data = get_weather(lat, lon)
    return jsonify(data)


#@app.route("/api/object")

@app.route("/api/lightpollution")
def light_pollution():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Missing or invalid coordinates"}), 400

    result = get_light_pollution(lat, lon)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True) 