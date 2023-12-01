from math import cos, sin, atan2
from math import sqrt

from coordinates import Spherical
from coordinates import Cartesian

class Translator:
    @staticmethod
    def sphericalToCartesian(spherical: Spherical) -> Cartesian:
        spherical.toRadians()
        
        radius = spherical.getRadius()
        theta  = spherical.getTheta()
        phi    = spherical.getPhi()
        
        x = radius * sin(phi) * cos(theta)
        y = radius * sin(phi) * sin(theta)
        z = radius * cos(phi)

        return Cartesian(x, y, z)

    @staticmethod
    def cartesianToSpherical(cartesian: Cartesian) -> Spherical:
        x = cartesian.getX()
        y = cartesian.getY()
        z = cartesian.getZ()
        
        radius = sqrt(x ** 2 + y ** 2 + z ** 2)
        theta  = atan2(sqrt(x ** 2 + y ** 2), z)
        phi    = atan2(y, x)
        
        spherical = Spherical(radius, theta, phi)
        spherical.toDegrees()
        
        return spherical
