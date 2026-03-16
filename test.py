from pyowm import OWM

owm = OWM("afbfbfbbfbdf02f58893dae21bab3636")
mgr = owm.weather_manager()

observation = mgr.weather_at_place("Tokyo,JP")
weather = observation.weather

print(weather.temperature("celsius"))