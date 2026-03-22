from flask import Flask, jsonify, request
from features.weather import get_weather
from features.light_pollution import get_light_pollution
from features.observation_guide import get_celestial_position
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/home")
def home():
    return {"status": "Back End on"}

@app.route("/api/weather")
def weather():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Missing lat or lon"}), 400

    try:
        return jsonify(get_weather(lat, lon))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/lightpollution")
def light_pollution():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Missing lat or lon"}), 400

    try:
        result = get_light_pollution(lat, lon)
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/object")
def object_position():
    target = request.args.get("target")
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if not target or lat is None or lon is None:
        return jsonify({"error": "Missing target, lat, or lon"}), 400

    try:
        result = get_celestial_position(target, lat, lon)
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/observation")
def observation():
    target = request.args.get("target")
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if not target or lat is None or lon is None:
        return jsonify({"error": "Missing target, lat, or lon"}), 400

    try:
        weather_data = get_weather(lat, lon)
        light_data = get_light_pollution(lat, lon)
        object_data = get_celestial_position(target, lat, lon)

        return jsonify({
            "location": {
                "latitude": lat,
                "longitude": lon
            },
            "weather": weather_data,
            "light_pollution": light_data,
            "object": object_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)