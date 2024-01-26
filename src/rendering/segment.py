from geometry           import Line
from coordinates        import Cartesian
from rendering.abstract import Renderable

from pygame      import Surface, Color
from dataclasses import dataclass

import pygame

@dataclass
class Segment(Renderable):
    line: Line

    def render(self, surface: Surface, origin: Cartesian, color: Color = Color(255, 255, 255), weight: float = 3) -> None:
        a = (self.line.a.x + origin.x, self.line.a.y + origin.y)
        b = (self.line.b.x + origin.x, self.line.b.y + origin.y)
        
        pygame.draw.line(surface, color, a, b, weight)
