from math        import pi, sqrt, cos, sin, atan2
from coordinates import Cartesian, Spherical

def to_cartesian(point: Spherical) -> Cartesian:
    x = point.radius * sin(point.rad_phi) * cos(point.rad_theta)
    y = point.radius * sin(point.rad_phi) * sin(point.rad_theta)
    z = point.radius * cos(point.rad_phi)
    
    return Cartesian(x, y, z)

def to_spherical(point: Cartesian) -> Spherical:
    radius = sqrt(point.x ** 2 + point.y ** 2 + point.z ** 2)
    theta  = atan2(point.y, point.x)                           * (180 / pi)
    phi    = atan2(sqrt(point.x ** 2 + point.y ** 2), point.z) * (180 / pi)
    
    return Spherical(radius, theta, phi)
