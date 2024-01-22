from coordinates import Spherical, Cartesian, to_cartesian

from dataclasses import dataclass

@dataclass
class Meridian:
    radius: float
    phi:    float

    def __post_init__(self) -> None:
        self.points = [
            Spherical(self.radius, 10, self.phi),
            Spherical(self.radius, 130, self.phi),
            Spherical(self.radius, 250, self.phi)
        ]

    def set_points(self, points: list[Spherical]) -> None:
        self.points = points
