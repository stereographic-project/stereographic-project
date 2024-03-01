from geometry           import Line       as GeometryLine
from coordinates        import Cartesian
from rendering.abstract import Renderable

from pygame      import Surface, Color
from dataclasses import dataclass

import pygame

@dataclass
class Line(Renderable):
    line: GeometryLine

    def render(self, surface: Surface, origin: Cartesian, color: Color = Color(255, 255, 255), weight: float = 3) -> None:
        if (self.line.slope != 0):
            a = ((-self.line.offset + surface.get_rect().top - origin.y) / self.line.slope + origin.x, surface.get_rect().top)
            b = ((-self.line.offset + surface.get_rect().bottom - origin.y) / self.line.slope + origin.x, surface.get_rect().bottom)
            
            pygame.draw.line(surface, color, a, b, weight)
            return

