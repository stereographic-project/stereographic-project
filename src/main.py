import random

from geometry    import Sphere, Plane, Meridian, Parallel
from rotations   import Rotation
from rendering   import Window
from projection  import Stereographic
from coordinates import Spherical

points = []

for _ in range(int(3690 / 1)):
    points.append(Spherical(10, random.uniform(0, 360), random.uniform(0, 360)))

meridians = [
    # Meridian(10, 20),
    # Meridian(10, 40),
    # Meridian(10, 60),
    # Meridian(10, 80),
    # Meridian(10, 100),
    # Meridian(10, 120),
    # Meridian(10, 140),
    # Meridian(10, 160),
    # Meridian(10, 180),
    # Meridian(10, 200),
    # Meridian(10, 220),
    # Meridian(10, 240),
    # Meridian(10, 260),
    # Meridian(10, 280),
    # Meridian(10, 300),
    # Meridian(10, 320),
    # Meridian(10, 340),
    # Meridian(10, 360),
]

parallels = [
    # Parallel(10, 20),
    # Parallel(10, 40),
    # Parallel(10, 60),
    # Parallel(10, 80),
    # Parallel(10, 100),
    # Parallel(10, 120),
    # Parallel(10, 140),
    # Parallel(10, 160),
    # Parallel(10, 180),
    # Parallel(10, 200),
    # Parallel(10, 220),
    # Parallel(10, 240),
    # Parallel(10, 260),
    # Parallel(10, 280),
    # Parallel(10, 300),
    # Parallel(10, 320),
    # Parallel(10, 340),
    # Parallel(10, 360),
]

sphere = Sphere(10, points, meridians, parallels)

def rotate() -> Stereographic:
    global sphere

    plane = Plane(-1000)
    sphere.rotate(Rotation(-1, 0, 0))

    stereographic = Stereographic(sphere, plane)
    stereographic.to_plane()

    return stereographic

Window(1280, 720).run(rotate)
