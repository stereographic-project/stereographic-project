from coordinates import Cartesian, Spherical
from geometry    import Sphere, Plane
from projection  import Stereographic

sphere = Sphere(300)

points = [
    Spherical(300, 10, 30),
    Spherical(300, 20, 30),
    Spherical(300, 30, 30),
    Spherical(300, 40, 30),
    Spherical(300, 50, 30),
    Spherical(300, 60, 30),
    Spherical(300, 70, 30),
    Spherical(300, 80, 30)
]

sphere.setPoints( points )

center = Cartesian(0, 0, -200)
plane  = Plane(center)

stereographic = Stereographic(sphere, plane).execute()

for point in stereographic.getPoints():
    print(point.display())

