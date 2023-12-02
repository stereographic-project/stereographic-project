from coordinates import Spherical
from geometry    import Sphere, Plane
from projection  import Stereographic

sphere = Sphere(300)

sphere \
    + Spherical(300, 90,  0) \
    + Spherical(300, 90, 20) \
    + Spherical(300, 90, 30) \
    + Spherical(300, 90, 90) \

plane = Plane(-300)

print(Stereographic(sphere, plane).to_plane())
