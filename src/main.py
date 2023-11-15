from geometry import Point
from geometry import Sphere

a = Point(0, 0, 0)
print(a.getX(), a.getY(), a.getZ())

sphere = Sphere(a, 300)
print(sphere.isOverlapping(Point(300, 0, 0)))
