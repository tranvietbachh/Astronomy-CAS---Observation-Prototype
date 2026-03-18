from flask import Flask, jsonify, request
from features.weather import get_weather
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

#@app.route("/api/lightpollution")


if __name__ == "__main__":
    app.run(debug=True) 