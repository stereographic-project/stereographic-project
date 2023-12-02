from dataclasses import dataclass

from geometry    import Vector
from coordinates import Cartesian

@dataclass
class Line:
    a: Cartesian
    b: Cartesian

    @property
    def vector(self) -> Vector:
        x = self.b.x - self.a.x
        y = self.b.y - self.a.y
        z = self.b.z - self.a.z
        
        return Vector(x, y, z)
