import requests
import re
from datetime import datetime, timedelta, timezone

def get_celestial_position(target_name, lat, lon):
    # 1. Translate the name to NASA's ID
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

    # 2. NASA requires the exact time in UTC
    now_utc = datetime.now(timezone.utc)
    start_time = now_utc.strftime("%Y-%m-%d %H:%M")
    stop_time = (now_utc + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")

    # 3. Build the URL parameters 
    # (Using a dictionary here is much cleaner than a massive f-string because of NASA's single quotes)
    url = "https://ssd-api.jpl.nasa.gov/horizons_api.cgi"
    params = {
        "format": "json",
        "COMMAND": f"'{target_id}'",
        "CENTER": "'coord@399'",
        "COORD_TYPE": "'GEODETIC'",
        "SITE_COORD": f"'{lon},{lat},0'", # NASA wants longitude first
        "MAKE_EPHEM": "'YES'",
        "EPHEM_TYPE": "'OBSERVER'",
        "QUANTITIES": "'4'",
        "START_TIME": f"'{start_time}'",
        "STOP_TIME": f"'{stop_time}'",
        "STEP_SIZE": "'1m'",
        "CSV_FORMAT": "'YES'"
    }

    # 4. Fetch the data
    response = requests.get(url, params=params)
    data = response.json()
    
    # 5. Extract the text and find the numbers using Regex
    raw_text = data.get("result", "")
    search = re.search(r"\$\$SOE\s*(.*?)\s*\$\$EOE", raw_text, re.DOTALL)
    
    if search:
        data_line = search.group(1).split(",")
        
        # Return a clean dictionary, just like your friend's weather code!
        return {
            "target": target_name.capitalize(),
            "azimuth": float(data_line[4].strip()),
            "elevation": float(data_line[5].strip()),
            "timestamp_utc": start_time
        }
        
    return {"error": "Could not extract coordinates from NASA data."}
