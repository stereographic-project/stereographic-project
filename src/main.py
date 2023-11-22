from coordinates import *

spherical = Spherical(100, 12, 50)
print((spherical.getRadius(), spherical.getTheta(), spherical.getPhi()))

cartesian = Translator.sphericalToCartesian(spherical)
print((cartesian.getX(), cartesian.getY(), cartesian.getZ()))

spherical = Translator.cartesianToSpherical(cartesian)
print((spherical.getRadius(), spherical.getTheta(), spherical.getPhi()))
