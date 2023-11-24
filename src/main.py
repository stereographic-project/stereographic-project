from coordinates import *

spherical = Spherical(100, 12, 50)
cartesian = Translator.sphericalToCartesian(spherical)
spherical = Translator.cartesianToSpherical(cartesian)

print(cartesian.getX(), cartesian.getY(), cartesian.getZ())
print(spherical.getRadius(), spherical.getTheta(), spherical.getPhi())
