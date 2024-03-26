import pygame
pygame.init()

from typing      import Callable
from pygame      import K_SPACE, Surface, Color
from pygame.time import Clock
from dataclasses import dataclass

from rendering   import Point, Circle
from rendering   import Line as RenderableLine
from geometry    import Line
from projection  import Stereographic
from coordinates import Cartesian

from math import sqrt

@dataclass
class Window:
    width:  int
    height: int

    # Optionals
    fps: int = 60

    @property
    def resolution(self) -> tuple:
        return (self.width, self.height)

    @property
    def origin(self) -> Cartesian:
        return Cartesian(self.width / 2, self.height / 2, -30)

    def __post_init__(self) -> None:
        self.clock   = Clock()
        self.screen  = pygame.display.set_mode(self.resolution)
        self.surface = Surface(self.resolution)

    def render_meridians(self, stereographic: Stereographic) -> None:
        for meridian in stereographic.sphere.meridians:
            points = []

            for point in meridian.points:
                points.append(stereographic.point_to_plane(point))

            slope1 = Line(points[0], points[1]).slope
            slope2 = Line(points[0], points[2]).slope
            difference = abs(slope1 - slope2)
            
            if (slope1 == slope2 and slope1 == 2147483647):
                continue;
            
            if (difference <= 0.001 and difference != 0):

                line = Line(points[0], points[1])
                RenderableLine(line).render(self.surface, self.origin, Color(127, 127, 127))

                continue

            Circle.from_points(points[0], points[1], points[2]).render(self.surface, self.origin, Color(127, 127, 127))

    def render_parallels(self, stereographic: Stereographic) -> None:
        for parallel in stereographic.sphere.parallels:
            points = []

            for point in parallel.points:
                points.append(stereographic.point_to_plane(point))

            slope1 = Line(points[0], points[1]).slope
            slope2 = Line(points[0], points[2]).slope
            difference = abs(slope1 - slope2)
            
            if (slope1 == slope2 and slope1 == 2147483647):
                continue;
            
            if (difference <= 0.001 and difference != 0):

                line = Line(points[0], points[1])
                RenderableLine(line).render(self.surface, self.origin, Color(127, 127, 127))

                continue

            Circle.from_points(points[0], points[1], points[2]).render(self.surface, self.origin, Color(127, 127, 127))



    def render(self, stereographic: Stereographic) -> None:
        self.render_meridians(stereographic)
        self.render_parallels(stereographic)

        for point in stereographic.plane.points:
            Point(point).render(self.surface, self.origin)

    def run(self, callback: Callable[[], Stereographic]) -> None:
        while True:
            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
            self.clock.tick(self.fps)
            
            if pygame.key.get_pressed()[K_SPACE]:
                pygame.display.set_caption(f"Stereographic Projection: PAUSED")
                continue

            self.surface.fill(Color(0, 0, 0))
            stereographic = callback()
            
            pygame.display.set_caption(f"Stereographic Projection: { len(stereographic.plane.points) } STARS, { len(stereographic.sphere.meridians) } MERIDIANS AND { len(stereographic.sphere.parallels) } PARALLELS. { self.clock.get_fps() // 1 } FPS")
            
            self.render(stereographic)
            
            self.screen.blit(self.surface, (0, 0))
            pygame.display.flip()
