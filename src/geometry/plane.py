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
        
        # TODO: Find why it doesn't works
        # if not self.is_overlapping(point):
        #     return
        
        self.points.append(point)

    # CALCULATORS
    def calculate_intersection(self, line: Line) -> Cartesian:
        radius = to_spherical(line.b).radius
        scalar = (self.height - radius) / (line.b.z - radius)
        
        x = line.a.x + line.vector.x * scalar
        y = line.a.y + line.vector.y * scalar
        z = line.a.z + line.vector.z * scalar
        
        return Cartesian(x, y, z)

    # CONDITIONS
    def is_overlapping(self, point: Cartesian, threshold: float = 10) -> bool:
        gap = abs(self.height * threshold / 100)
        
        # print(self.height == point.z, " -> ", (point.z >= self.height - gap) and (point.z <= self.height + gap))
        return (point.z >= self.height - gap) and (point.z <= self.height + gap)

    # MAGIC METHODS
    def __post_init__(self) -> None:
        self.points = [point for point in self.points if self.is_overlapping(point)]
