from typing      import List, Self
from dataclasses import dataclass, field

from geometry    import Line
from coordinates import Cartesian, to_spherical

@dataclass
class Plane:
    height: float
    points: List[Cartesian] = field(default_factory=list)
    
    # MAGIC METHODS
    def __add__(self, point: Cartesian) -> Self:
        if is_overlapping(self, point):
            self.points.append(point)
            
        return self
    
    def __post_init__(self):
        self.points = [point for point in self.points if is_overlapping(point)]

def is_overlapping(plane: Plane, point: Cartesian) -> bool:
    return plane.height == point.z

def calculate_intersection(plane: Plane, line: Line) -> Cartesian:
    radius = to_spherical(line.b).radius
    scalar = (plane.height - radius) / (line.b.z - radius)
    
    x = round(line.a.x + line.vector.x * scalar, 1)
    y = round(line.a.y + line.vector.y * scalar, 1)
    z = round(line.a.z + line.vector.z * scalar, 1)
    
    return Cartesian(x, y, z)
