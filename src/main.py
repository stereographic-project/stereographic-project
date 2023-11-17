
from geometry import Point, Sphere

center = Point(0, 0, 0)
sphere = Sphere(center, 300)

pointA = Point(212, 212, 0)
print(sphere.isOverlapping(pointA))
