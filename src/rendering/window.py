import pygame

from geometry import Sphere, Plane, Line, Circle
from projection import Stereographic
from rotations import Rotation
from coordinates import Cartesian
from dataclasses import dataclass

class Window:
    def __init__(self, width: int, height: int) -> None:
        pygame.init()

        self.resolution = self.width, self.height = width, height
        self.fps        = 120
        
        self.surface    = pygame.display.set_mode(self.resolution)
        self.clock      = pygame.time.Clock()

    def render(self, sphere: Sphere):
        while True:
            self.surface.fill(pygame.Color("black"))

            sphere.rotate(Rotation(.10, .10, .10))
            plane = Plane(-30)

            a = Cartesian(50, 60, 0)
            b = Cartesian(100, 50, 0)
            c = Cartesian(30, 30, 0)

            circle = Circle.from_points(a, b, c)

            pygame.draw.circle(self.surface, pygame.Color(255, 0, 0), (circle.center.x + self.width / 2, circle.center.y + self.height / 2), circle.radius + 3, 5)

            pygame.draw.circle(self.surface, pygame.Color(255, 255, 255), (circle.center.x + self.width / 2, circle.center.y + self.height / 2), 5)
            pygame.draw.circle(self.surface, pygame.Color(255, 255, 255), (a.x + self.width / 2, a.y + self.height / 2), 5)
            pygame.draw.circle(self.surface, pygame.Color(255, 255, 255), (b.x + self.width / 2, b.y + self.height / 2), 5)
            pygame.draw.circle(self.surface, pygame.Color(255, 255, 255), (c.x + self.width / 2, c.y + self.height / 2), 5)


            # pygame.draw.line(self.surface, pygame.Color(255, 255, 0), (line.mediator.a.x, line.mediator.a.y), (line.mediator.b.x, line.mediator.b.y), 2)
            # pygame.draw.line(self.surface, pygame.Color(255, 0, 255), (line.a.x, line.a.y), (line.b.x, line.b.y), 2)

            stereographic = Stereographic(sphere, plane)
            points = stereographic.to_plane().points

            # pygame.draw.line(self.surface, pygame.Color(255, 0, 0), (points[0].x + self.width / 2, points[0].y + self.height / 2), (points[len(points) - 1].x + self.width / 2, points[len(points) - 1].y + self.height / 2), 5)

            # for key in range(len(points) - 1):
            #     pygame.draw.line(self.surface, pygame.Color(255, 0, 0), (points[key].x + self.width / 2, points[key].y + self.height / 2), (points[key + 1].x + self.width / 2, points[key + 1].y + self.height / 2), 5)

            # for point in points:
                # pygame.draw.circle(self.surface, pygame.Color(255, 255, 255), (round(point.x) + self.width / 2, round(point.y) + self.height / 2), 5)

            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        
            pygame.display.set_caption(str(self.clock.get_fps() // 1))
            pygame.display.flip()
            self.clock.tick(self.fps)
