from typing      import List, Self
from dataclasses import dataclass, field

from coordinates import Spherical
from coordinates.cartesian import Cartesian

@dataclass
class Sphere:
    radius: float
    points: List[Spherical] = field(default_factory=list)
    
    @property
    def pole(self) -> Cartesian:
        return Cartesian(0, 0, self.radius)
    
    # MAGIC METHODS
    def __add__(self, point: Spherical) -> Self:
        if is_overlapping(self, point):
            self.points.append(point)
            
        return self
    
    def __post_init__(self):
        self.points = [point for point in self.points if is_overlapping(point)]
    
def is_overlapping(sphere: Sphere, point: Spherical) -> bool:
    return sphere.radius == point.radius
