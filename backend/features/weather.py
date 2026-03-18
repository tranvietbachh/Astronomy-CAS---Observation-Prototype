import requests

def get_weather(lat, lon):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,cloud_cover,weather_code,precipitation,is_day"
    )

    response = requests.get(url)
    data = response.json()["current"]

    return {
        "temperature": data["temperature_2m"],
        "humidity": data["relative_humidity_2m"],
        "cloud_cover": data["cloud_cover"],
        "weather_code": data["weather_code"],
        "precipitation": data["precipitation"],
        "is_day": data["is_day"]
    }