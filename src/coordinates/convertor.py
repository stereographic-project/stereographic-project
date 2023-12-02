from math        import pi, sqrt
from math        import cos, sin, atan2

from coordinates import Cartesian, Spherical

def to_cartesian(spherical: Spherical) -> Cartesian:
    x = round(spherical.radius * sin(spherical.phi_radian) * cos(spherical.theta_radian), 8)
    y = round(spherical.radius * sin(spherical.phi_radian) * sin(spherical.theta_radian), 8)
    z = round(spherical.radius * cos(spherical.phi_radian), 8)

    return Cartesian(x, y, z)

def to_spherical(cartesian: Cartesian) -> Spherical:
    radius       = sqrt(cartesian.x ** 2 + cartesian.y ** 2 + cartesian.z ** 2)
    theta_radian = atan2(cartesian.y, cartesian.x)
    phi_radian   = atan2(sqrt(cartesian.x ** 2 + cartesian.y ** 2), cartesian.z)

    multiplier = 180 / pi
    theta = multiplier * theta_radian
    phi   = multiplier * phi_radian

    return Spherical(radius, theta, phi)
