import random

from geometry    import Sphere, Plane
from rotations   import Rotation
from rendering   import Window
from projection  import Stereographic
from coordinates import Spherical


points = []

for _ in range(100):
    points.append(Spherical(10, random.uniform(0, 360), random.uniform(0, 360)))

sphere = Sphere(10, points)

def rotate() -> Stereographic:
    global sphere

    plane = Plane(-30)
    sphere.rotate(Rotation(.10, .10, .10))

    stereographic = Stereographic(sphere, plane)
    stereographic.to_plane()

    return stereographic

Window(1280, 720).run(rotate)
