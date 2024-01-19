from geometry    import Line
from coordinates import Cartesian

from math        import sqrt
from typing      import Self
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float
    center: Cartesian

    @staticmethod
    def calculate_radius(point: Cartesian, center: Cartesian) -> float:
        x = (point.x - center.x) ** 2
        y = (point.y - center.y) ** 2

        return sqrt(x + y)

    @staticmethod
    def from_points(a: Cartesian, b: Cartesian, c: Cartesian) -> Self:
        segment_ab = Line(a, b)
        segment_bc = Line(b, c)

        print(segment_bc.mediator.offset)

        x = (segment_ab.mediator.offset - segment_bc.mediator.offset) / (segment_bc.mediator.slope - segment_ab.mediator.slope)
        y = segment_ab.mediator.slope * x + segment_ab.mediator.offset
        
        center = Cartesian(x, y, a.z)
        radius = Circle.calculate_radius(a, center)

        return Circle(radius, center)
