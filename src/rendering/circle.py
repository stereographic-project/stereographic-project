from geometry    import Line
from coordinates import Cartesian

from math        import sqrt
from typing      import Self
from pygame      import Surface, Color
from dataclasses import dataclass

from rendering.abstract import Renderable

import pygame

@dataclass
class Circle(Renderable):
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

        divider = (segment_bc.mediator.slope - segment_ab.mediator.slope)

        if (segment_bc.mediator.slope - segment_ab.mediator.slope) == 0:
            divider = 0.000000000001

        x = (segment_ab.mediator.offset - segment_bc.mediator.offset) / divider
        y = segment_ab.mediator.slope * x + segment_ab.mediator.offset
        
        center = Cartesian(x, y, a.z)
        radius = Circle.calculate_radius(a, center)

        return Circle(radius, center)

    def render(self, surface: Surface, origin: Cartesian, color: Color = Color(255, 255, 255), weight: int = 5) -> None:
        diameter  = self.radius * 2
        rectangle = (origin.x + self.center.x - self.radius, origin.y + self.center.y - self.radius, diameter, diameter)

        print(self.radius)
        pygame.draw.rect(surface, Color(255, 0, 0), rectangle, weight)
        
        # pygame.draw.circle(surface, color, position, self.radius, weight)
