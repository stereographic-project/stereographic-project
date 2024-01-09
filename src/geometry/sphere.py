from typing      import Self
from dataclasses import dataclass, field

from rotations   import Rotation
from coordinates import Cartesian, Spherical, to_cartesian, to_spherical

from matrices import Matrix

@dataclass
class Sphere:
    radius: float
    points: list[Spherical] = field(default_factory = list)

    @property
    def pole(self) -> Cartesian:
        return Cartesian(0, 0, self.radius)

    def rotate(self, rotation: Rotation) -> None:
        points = []
        
        for point in self.points:
            point  = to_cartesian(point)
            matrix = Matrix([[point.x, point.y, point.z]])@(rotation.matrix_x + rotation.matrix_y - rotation.matrix_z)
            
            x = matrix.matrix[0][0]
            y = matrix.matrix[0][1]
            z = matrix.matrix[0][2]
            
            point = to_spherical(Cartesian(x, y, z))
            
            points.append(point)
        
        self.points = points
        
    # CRUD METHODS
    def add_point(self, point: Spherical) -> None:
        if point in self.points:
            return
        
        if not self.is_overlapping(point):
            return
        
        self.points.append(point)

    # CONDITIONS
    def is_overlapping(self, point: Spherical, threshold: float = 5) -> bool:
        gap = self.radius * threshold / 100
        return point.radius >= self.radius - gap and point.radius <= self.radius + gap

    # MAGIC METHODS
    def __post_init__(self) -> None:
        self.points = [point for point in self.points if self.is_overlapping(point)]
