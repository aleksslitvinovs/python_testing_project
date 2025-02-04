import requests

from typing import Optional

from .coordinates_info import CoordinatesInfo
from .weather_info import WeatherInfo


API_KEY = "3899eaf1acd1c74c73b0142a058d8eca"

COORDINATES_BASE_URL = "https://api.openweathermap.org/geo/1.0/direct"
COORDINATES_API = f"{COORDINATES_BASE_URL}?q={{city}}&limit=1&appid={API_KEY}"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API = f"{BASE_URL}?lat={{lat}}&lon={{lon}}&units=metric&appid={API_KEY}"


def get_weather(city: str) -> WeatherInfo:
    if not city:
        raise Exception("City name is required")

    coordinates = _get_coordinates(city)
    if not coordinates:
        raise Exception(f"City '{city}' not found")

    url = API.format(
        lat=coordinates.latitude, lon=coordinates.longitude, API_KEY=API_KEY
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to get weather", response.json())

    data = response.json()
    weather_info = WeatherInfo.from_dict(data)

    return weather_info


def _get_coordinates(city: str) -> CoordinatesInfo:
    url = COORDINATES_API.format(city=city, API_KEY=API_KEY)

    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    if not data:
        return None

    coordinates = CoordinatesInfo.from_dict(data[0])

    return coordinates
