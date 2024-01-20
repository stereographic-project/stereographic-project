from coordinates        import Cartesian
from rendering.abstract import Renderable

from pygame      import Surface, Color
from dataclasses import dataclass

import pygame

@dataclass
class Point(Renderable):
    point: Cartesian
    
    def render(self, surface: Surface, origin: Cartesian, color: Color = Color(255, 255, 255), size: float = 10) -> None:
        radius   = size / 2
        position = (self.point.x + origin.x, self.point.y + origin.y)
        
        pygame.draw.circle(surface, color, position, radius)
