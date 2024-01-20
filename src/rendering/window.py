import pygame
pygame.init()

from typing      import Callable
from pygame      import Surface, Color
from pygame.time import Clock
from dataclasses import dataclass

from rendering   import Point
from projection  import Stereographic
from coordinates import Cartesian

@dataclass
class Window:
    width:  int
    height: int
    
    # Optionals
    fps: int = 120

    @property
    def resolution(self) -> tuple:
        return (self.width, self.height)

    def __post_init__(self) -> None:
        self.clock   = Clock()
        self.surface = pygame.display.set_mode(self.resolution)

    def render(self, stereographic: Stereographic) -> None:
        for point in stereographic.plane.points:
            Point(point).render(self.surface, Cartesian(self.width / 2, self.height / 2, -30))

    def run(self, callback: Callable[[], Stereographic]) -> None:
        while True:
            self.surface.fill(Color(0, 0, 0))
            stereographic = callback()

            self.render(stereographic)

            pygame.display.set_caption(f"Stereographic Projection: { len(stereographic.plane.points) } POINTS, { self.clock.get_fps() // 1 } FPS")
            pygame.display.flip()

            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
            self.clock.tick(self.fps)
