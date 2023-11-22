from math import cos, acos, sin, atan
from math import sqrt

from coordinates.spherical import Spherical
from coordinates.cartesian import Cartesian

class Translator:
    @staticmethod
    def sphericalToCartesian(spherical: Spherical) -> Cartesian:
        spherical.toRadians()
        
        x = spherical.getRadius() * sin( spherical.getPhi() ) * cos( spherical.getTheta() )
        y = spherical.getRadius() * sin( spherical.getPhi() ) * sin( spherical.getTheta() )
        z = spherical.getRadius() * cos( spherical.getPhi() )

        return Cartesian(x, y, z)

    @staticmethod
    def cartesianToSpherical(cartesian: Cartesian) -> Spherical:
        radius = sqrt( cartesian.getX()**2 + cartesian.getY()**2 + cartesian.getZ()**2)
        theta  = atan( cartesian.getY() / cartesian.getX() )
        phi    = acos( cartesian.getZ() / radius )
        
        spherical = Spherical(radius, theta, phi)
        spherical.toDegrees()
        
        return spherical
