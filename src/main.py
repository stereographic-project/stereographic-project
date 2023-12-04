from geometry    import Plane, Sphere
from coordinates import Spherical
from projection  import Stereographic

points = [
    Spherical(300, 90,   0),
    Spherical(300, 90,  10),
    Spherical(300, 90,  20),
    Spherical(300, 90,  30),
    Spherical(300, 90,  90),
    Spherical(300, 90, 180)
]

sphere = Sphere(300, points)
plane  = Plane(-300)

print(Stereographic(sphere, plane).to_plane())
