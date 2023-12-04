from dataclasses import dataclass, field

from coordinates import Cartesian, Spherical

@dataclass
class Sphere:
    radius: float
    points: list[Spherical] = field(default_factory = list)

    @property
    def pole(self) -> Cartesian:
        return Cartesian(0, 0, self.radius)

    # CRUD METHODS
    def add_point(self, point: Spherical) -> None:
        if point in self.points:
            return
        
        if not self.is_overlapping(point):
            return
        
        self.points.append(point)

    # CONDITIONS
    def is_overlapping(self, point: Spherical) -> bool:
        return self.radius == point.radius

    # MAGIC METHODS
    def __post_init__(self) -> None:
        self.points = [point for point in self.points if self.is_overlapping(point)]
