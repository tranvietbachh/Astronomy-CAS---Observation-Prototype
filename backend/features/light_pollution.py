import os
import rasterio

TIF_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "night_lights.tif")
TIF_PATH = os.path.abspath(TIF_PATH)


def get_light_pollution(lat, lon):
    with rasterio.open(TIF_PATH) as src:
        bounds = src.bounds

        if not (bounds.left <= lon <= bounds.right and bounds.bottom <= lat <= bounds.top):
            return {
                "error": "Coordinates outside raster bounds",
                "bounds": {
                    "left": bounds.left,
                    "right": bounds.right,
                    "bottom": bounds.bottom,
                    "top": bounds.top
                }
            }

        row, col = src.index(lon, lat)
        value = src.read(1)[row, col]

        return {
            "light_pollution": float(value),
            "row": row,
            "col": col
        }