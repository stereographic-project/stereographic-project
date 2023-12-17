import pygame

from coordinates import Cartesian

class Renderer:
    def __init__(self):
        pygame.init()
        
        self.WIDTH      = 1024
        self.HEIGHT     = 720
        self.RESOLUTION = self.WIDTH, self.HEIGHT

        self.FPS    = 60

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock  = pygame.time.Clock()

    def draw(self, points = list[Cartesian]):
        self.screen.fill(pygame.Color("black"))

        for point in points:
            pygame.draw.circle(self.screen, pygame.Color("white"), (point.x + self.WIDTH / 2, point.y + self.HEIGHT / 2), 5)

    def run(self, points = list[Cartesian]):
        while True:
            self.draw(points)
            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]

            pygame.display.set_caption(str(self.clock.get_fps() // 1))
            pygame.display.flip()
            self.clock.tick(self.FPS)
