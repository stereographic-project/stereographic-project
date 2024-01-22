from coordinates import Spherical, Cartesian, to_cartesian

from dataclasses import dataclass

@dataclass
class Parallel:
    radius: float
    theta:  float

    def __post_init__(self) -> None:
        self.points = [
            Spherical(self.radius, self.theta, 10),
            Spherical(self.radius, self.theta, 130),
            Spherical(self.radius, self.theta, 250)
        ]

    def set_points(self, points: list[Spherical]) -> None:
        self.points = points

