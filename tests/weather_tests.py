from http import HTTPStatus
import json
import pytest
import responses
import src.open_weather.weather as weather

from src.open_weather.coordinates_info import CoordinatesInfo
from src.open_weather.weather_info import WeatherInfo


@pytest.fixture()
def fake_coordinates_info():
    with open("tests/resources/coordinates_response.json") as f:
        return json.load(f)


@pytest.fixture()
def fake_weather_info():
    with open("tests/resources/open_weather_response.json") as f:
        return json.load(f)


@responses.activate
def test_get_weather_valid(fake_coordinates_info, fake_weather_info):
    city = "London"

    coordinates_url = weather.COORDINATES_API.format(city=city)
    responses.add(
        responses.GET, coordinates_url, json=fake_coordinates_info, status=HTTPStatus.OK
    )

    coordinates_info = CoordinatesInfo.from_dict(fake_coordinates_info[0])
    api_uri = weather.API.format(
        lat=coordinates_info.latitude, lon=coordinates_info.longitude
    )
    responses.add(responses.GET, api_uri, json=fake_weather_info, status=HTTPStatus.OK)

    response = weather.get_weather(city)

    assert response == WeatherInfo.from_dict(fake_weather_info)


def test_get_weather_empty():
    with pytest.raises(Exception) as err:
        weather.get_weather("")

    assert str(err.value) == "City name is required"


@responses.activate
def test_get_weather_invalid_city(fake_coordinates_info):
    city = "London"

    coordinates_url = weather.COORDINATES_API.format(city=city)
    responses.add(responses.GET, coordinates_url, json=[], status=HTTPStatus.OK)

    coordinates_info = CoordinatesInfo.from_dict(fake_coordinates_info[0])
    api_uri = weather.API.format(
        lat=coordinates_info.latitude, lon=coordinates_info.longitude
    )
    responses.add(responses.GET, api_uri, status=HTTPStatus.OK)

    with pytest.raises(Exception) as err:
        weather.get_weather(city)

    assert str(err.value) == f"City '{city}' not found"
