from pygame      import Surface, Color
from coordinates import Cartesian

class Renderable:
    def render(self, surface: Surface, origin: Cartesian, color: Color = Color(255, 255, 255)) -> None:
        pass
