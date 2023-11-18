from geometry import Point, Sphere, Line, Plane

center = Point(0, 0, 0)
sphere = Sphere(center, 300)

pointA = Point(173, 173, 173)
print(sphere.isOverlapping(pointA))

line = Line(center, pointA)
intersection = Plane(Point(0, 0, 400)).calculateIntersection(line)

print((intersection.getX(), intersection.getY(), intersection.getZ()))
