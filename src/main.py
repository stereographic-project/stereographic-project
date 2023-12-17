from rendering import Renderer
from coordinates import Spherical

from geometry import Sphere, Plane
from projection import Stereographic
from rotations import Rotation

import random

points = []
for _ in range(20000):
    points.append(Spherical(10, 30, random.uniform(0, 360)))    

sphere = Sphere(10, points)
sphere.rotate(Rotation(20, 50, 0))
plane = Plane(-30)

stereographic = Stereographic(sphere, plane)
points = stereographic.to_plane().points

Renderer().run(points)
