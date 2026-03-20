import requests
import re
from datetime import datetime, timedelta, timezone

def get_celestial_position(target_name, lat, lon):
    targets = {
        "moon": "301",
        "mars": "499",
        "jupiter": "599",
        "saturn": "699",
        "venus": "299",
        "sun": "10"
    }

    target_id = targets.get(target_name.lower())
    if not target_id:
        return {"error": f"Unknown target: {target_name}"}

    now_utc = datetime.now(timezone.utc)
    start_time = now_utc.strftime("%Y-%m-%d %H:%M")
    stop_time = (now_utc + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")

    url = "https://ssd-api.jpl.nasa.gov/horizons.api"
    params = {
        "format": "json",
        "COMMAND": target_id,
        "CENTER": "coord@399",
        "COORD_TYPE": "GEODETIC",
        "SITE_COORD": f"{lon},{lat},0",
        "MAKE_EPHEM": "YES",
        "EPHEM_TYPE": "OBSERVER",
        "QUANTITIES": "4",
        "START_TIME": start_time,
        "STOP_TIME": stop_time,
        "STEP_SIZE": "1m",
        "CSV_FORMAT": "YES"
    }

    response = requests.get(url, params=params, timeout=20)
    print("Status:", response.status_code)
    print("Raw response:", response.text[:1000])

    response.raise_for_status()

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "API did not return JSON", "raw_response": response.text[:1000]}

    raw_text = data.get("result", "")
    search = re.search(r"\$\$SOE\s*(.*?)\s*\$\$EOE", raw_text, re.DOTALL)

    if search:
        data_line = search.group(1).strip().split(",")

        return {
            "target": target_name.capitalize(),
            "azimuth": float(data_line[3].strip()),
            "elevation": float(data_line[4].strip()),
            "timestamp_utc": start_time
        }

    return {"error": "Could not extract coordinates from NASA data.", "result": raw_text[:1000]}

print(get_celestial_position("moon", 35, 139))