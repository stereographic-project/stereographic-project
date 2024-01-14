import pygame

from geometry import Sphere, Plane
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

            stereographic = Stereographic(sphere, plane)
            points = stereographic.to_plane().points

            for point in points:
                pygame.draw.circle(self.surface, pygame.Color(255, 255, 255), (round(point.x) + self.width / 2, round(point.y) + self.height / 2), 5)

            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        
            pygame.display.set_caption(str(self.clock.get_fps() // 1))
            pygame.display.flip()
            self.clock.tick(self.fps)
