from rendering.abstract import Renderable

from pygame      import Surface, Color
from dataclasses import dataclass

@dataclass
class Frame(Renderable):
    title: str
    visible: bool = True

    def render(self, surface: Surface, background: Color = Color(255, 255, 255)) -> None:
        pass
