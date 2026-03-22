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

    url = "https://ssd.jpl.nasa.gov/api/horizons.api"
    params = {
        "format": "json",
        "COMMAND": f"'{target_id}'",
        "CENTER": "'coord@399'",
        "COORD_TYPE": "'GEODETIC'",
        "SITE_COORD": f"'{lon},{lat},0'",
        "MAKE_EPHEM": "'YES'",
        "EPHEM_TYPE": "'OBSERVER'",
        "QUANTITIES": "'4'",
        "START_TIME": f"'{start_time}'",
        "STOP_TIME": f"'{stop_time}'",
        "STEP_SIZE": "'1m'",
        "CSV_FORMAT": "'YES'"
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return {
            "error": str(e),
            "raw_text": response.text[:1000] if "response" in locals() else None
        }

    raw_text = data.get("result", "")
    match = re.search(r"\$\$SOE\s*(.*?)\s*\$\$EOE", raw_text, re.DOTALL)

    if not match:
        return {
            "error": "Could not extract coordinates from NASA data.",
            "preview": raw_text[:1500]
        }

    first_line = match.group(1).strip().splitlines()[0]
    parts = [x.strip() for x in first_line.split(",")]

    try:
        return {
            "target": target_name.capitalize(),
            "azimuth": float(parts[3]),
            "elevation": float(parts[4]),
            "timestamp_utc": start_time
        }
    except Exception as e:
        return {
            "error": f"Parsing failed: {e}",
            "line": first_line,
            "parts": parts
        }


print(get_celestial_position("moon", 35, 139))