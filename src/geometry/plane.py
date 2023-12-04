from dataclasses import dataclass, field

from coordinates import Cartesian
from coordinates.convertor import to_spherical
from geometry import Line

@dataclass
class Plane:
    height: float
    points: list[Cartesian] = field(default_factory=list)

    # CRUD METHODS
    def add_point(self, point: Cartesian):
        if point in self.points:
            return
        
        if not self.is_overlapping(point):
            return
        
        self.points.append(point)

    # CALCULATORS
    def calculate_intersection(self, line: Line) -> Cartesian:
        radius = to_spherical(line.b).radius
        scalar = (self.height - radius) / (line.b.z - radius)
        
        x = round(line.a.x + line.vector.x * scalar, 1)
        y = round(line.a.y + line.vector.y * scalar, 1)
        z = round(line.a.z + line.vector.z * scalar, 1)
        
        return Cartesian(x, y, z)

    # CONDITIONS
    def is_overlapping(self, point: Cartesian) -> bool:
        return self.height == point.z

    # MAGIC METHODS
    def __post_init__(self) -> None:
        self.points = [point for point in self.points if self.is_overlapping(point)]
