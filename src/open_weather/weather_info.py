from dataclasses import dataclass


@dataclass
class WeatherInfo:
    temp: float
    wind_speed: float
    chance_of_rain: float

    @classmethod
    def from_dict(self, data: object) -> "WeatherInfo":
        return self(
            temp=data["main"]["temp"],
            wind_speed=data["wind"]["speed"],
            chance_of_rain=data.get("rain", 0).get("1h", 0),
        )
