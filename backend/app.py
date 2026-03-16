from flask import Flask, jsonify, request
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

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,cloud_cover,weather_code,precipitation,is_day"

    response = requests.get(url)
    data = response.json()

    weather = data["current"]

    temperature = weather["temperature_2m"]
    humidity = weather["relative_humidity_2m"]
    cloud_cover = weather["cloud_cover"]
    weather_code = weather["weather_code"]
    precipitation = weather["precipitation"]
    is_day = weather["is_day"]

    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "cloud_cover": cloud_cover,
        "weather_code": weather_code,
        "precipitation": precipitation,
        "is_day": is_day
    })


#@app.route("/api/object")

#@app.route("/api/lightpollution")


if __name__ == "__main__":
    app.run(debug=True) 