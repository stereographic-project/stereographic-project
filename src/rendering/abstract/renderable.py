from pygame      import Surface
from coordinates import Cartesian

class Renderable:
    def render(self, surface: Surface, origin: Cartesian) -> None:
        pass
