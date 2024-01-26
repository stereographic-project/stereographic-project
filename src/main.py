import random

from geometry    import Sphere, Plane, Meridian, Parallel
from rotations   import Rotation
from rendering   import Window
from projection  import Stereographic
from coordinates import Spherical


points = []

for _ in range(500):
    points.append(Spherical(10, random.uniform(0, 360), random.uniform(0, 360)))

meridians = [
    Meridian(10, 30)
]

# for i in range(12):
#     meridians.append(Meridian(10, i * 360 / 12))

parallels = [
    Parallel(10, 30)
]

# for i in range(18):
#     parallels.append(Parallel(10, i * 10))

sphere = Sphere(10, points, meridians, parallels)

def rotate() -> Stereographic:
    global spheres

    plane = Plane(-50)
    sphere.rotate(Rotation(.1, .1, .1))

    stereographic = Stereographic(sphere, plane)
    stereographic.to_plane()

    return stereographic

Window(1280, 720).run(rotate)
