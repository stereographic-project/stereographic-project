from typing      import Self
from dataclasses import dataclass

from geometry    import Vector
from coordinates import Cartesian

@dataclass(frozen = True)
class Line:
    a: Cartesian
    b: Cartesian
    
    @property
    def slope(self) -> float:
        if self.b.x - self.a.x == 0:
            return 2147483647

        return (self.b.y - self.a.y) / (self.b.x - self.a.x)

    @property
    def offset(self) -> float:
        offset = -self.a.x * self.slope
        return offset + self.a.y

    @property
    def vector(self) -> Vector:
        x = self.b.x - self.a.x
        y = self.b.y - self.a.y
        z = self.b.z - self.a.z
        
        return Vector(x, y, z)

    @property
    def mediator(self) -> Self:
        center = Cartesian((self.a.x + self.b.x) / 2, (self.a.y + self.b.y) / 2, (self.a.z + self.b.z) / 2)

        c = Cartesian(center.x - self.vector.y / 2, center.y + self.vector.x / 2, center.z + self.vector.z / 2)
        d = Cartesian(center.x + self.vector.y / 2, center.y - self.vector.x / 2, center.z - self.vector.z / 2)

        return Line(c, d)
