from geometry    import Line
from coordinates import Cartesian

from math        import sqrt
from typing      import Self
from pygame      import Surface, Color
from dataclasses import dataclass
from geometry    import Line

from rendering.abstract import Renderable
from rendering import Point, Segment

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
    def from_points(a: Cartesian, b: Cartesian, c: Cartesian) -> Renderable:
        segment_ab = Line(a, b)
        segment_bc = Line(b, c)

        divider = (segment_bc.mediator.slope - segment_ab.mediator.slope)

        if divider == 0:
            return Segment(Line(a, c))

        x = (segment_ab.mediator.offset - segment_bc.mediator.offset) / divider
        y = segment_ab.mediator.slope * x + segment_ab.mediator.offset
        
        center = Cartesian(x, y, a.z)
        radius = Circle.calculate_radius(a, center)

        return Circle(radius, center)
    
    def calculate_intersection(self, line: Line) -> list[Cartesian]:
        if line.a.x - line.b.x == 0:
            x = line.a.x
            
            if self.radius ** 2 < (x - self.center.x) ** 2:
                return []

            y1 = sqrt(self.radius ** 2 - (x - self.center.x) ** 2) + self.center.y
            y2 = -sqrt(self.radius ** 2 - (x - self.center.x) ** 2) + self.center.y

            return [Cartesian(x, y1, line.a.z), Cartesian(x, y2, line.a.z)]
        
        a = line.slope ** 2 + 1
        b = -2 * (self.center.x + line.slope * self.center.y - line.slope * line.offset)
        c = self.center.x ** 2 + self.center.y ** 2 + line.offset ** 2 - 2 * self.center.y * line.offset - self.radius ** 2

        delta = b ** 2 - 4 * a * c
        
        if delta >= 0:
            x1 = (-b - sqrt(delta)) / (2 * a)
            y1 = line.slope * x1 + line.offset

            x2 = (-b + sqrt(delta)) / (2 * a)
            y2 = line.slope * x2 + line.offset
            
            return [Cartesian(x1, y1, line.a.z), Cartesian(x2, y2, line.a.z)]
        
        return []

    def render(self, surface: Surface, origin: Cartesian, color: Color = Color(255, 255, 255), weight: int = 3) -> None:
        frame = [
            Line(Cartesian(-origin.x, -origin.y, origin.z), Cartesian(-origin.x, origin.y, origin.z)),
            Line(Cartesian(origin.x, -origin.y, origin.z), Cartesian(origin.x, origin.y, origin.z)),
            Line(Cartesian(-origin.x, -origin.y, origin.z), Cartesian(origin.x, -origin.y, origin.z)),
            Line(Cartesian(-origin.x, origin.y, origin.z), Cartesian(origin.x, origin.y, origin.z)),
        ]

        position = (self.center.x + origin.x, self.center.y + origin.y)
        pygame.draw.circle(surface, color, position, self.radius, weight)

        for line in frame:
            points = self.calculate_intersection(line)

            for point in points:
                Point(point).render(surface, origin, Color(0, 255, 0), 16)
