from dataclasses import dataclass


@dataclass
class CoordinatesInfo:
    latitude: float
    longitude: float

    @classmethod
    def from_dict(self, data: object) -> "CoordinatesInfo":
        return self(
            latitude=data["lat"],
            longitude=data["lon"],
        )
