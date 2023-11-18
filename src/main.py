from geometry   import Point, Sphere, Plane
from projection import Stereographic

center = Point(0, 0, 0)
sphere = Sphere(center, 300)

center = Point(0, 0, 400)
plane = Plane(center)

pointA = Point(173, 173, 173)
pointB = Point(300, 0, 0)
pointC = Point(0, 300, 0)
pointD = Point(212.1, 0, 212.1)
pointE = Point(0, 0, 300)
pointE = Point(0, 0, -300)
pointF = Point(400, 400, 400)

points = [
    pointA,
    pointB,
    pointC,
    pointD,
    pointE,
    pointF,
]

projection = Stereographic(sphere, plane, points)
print([(point.getX(), point.getY()) for point in projection.execute()])
