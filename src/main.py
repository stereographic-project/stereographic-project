from coordinates import Spherical

from geometry import Sphere, Plane
from projection import Stereographic
from rotations import Rotation

from rendering import Window

import pygame
import random

points = []
for _ in range(1000):
    points.append(Spherical(10, random.uniform(0, 360), random.uniform(0, 360)))    

sphere = Sphere(10, points)

Window(1024, 720).render(sphere)
    
