import random

from geometry    import Sphere, Plane, Meridian, Parallel
from rotations   import Rotation
from rendering   import Window
from projection  import Stereographic
from coordinates import Spherical


points = []

# for _ in range(500):
#     points.append(Spherical(10, random.uniform(0, 360), random.uniform(0, 360)))

meridians = [
    Meridian(10, 90)
]

parallels = [
    Parallel(10, 90)
]

sphere = Sphere(10, points, meridians, parallels)

def rotate() -> Stereographic:
    global sphere

    plane = Plane(-500)
    sphere.rotate(Rotation(0, .1, .1))

    stereographic = Stereographic(sphere, plane)
    stereographic.to_plane()

    return stereographic

Window(1280, 720).run(rotate)
