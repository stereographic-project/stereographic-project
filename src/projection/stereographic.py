from coordinates import to_cartesian
from geometry import Plane, Sphere, Line
from geometry.plane import calculate_intersection

class Stereographic:
    def __init__(self, sphere: Sphere, plane: Plane) -> None:
        self.sphere = sphere
        self.plane  = plane

    def to_plane(self) -> Plane:
        for point in self.sphere.points:
            cartesian = to_cartesian(point)
            
            if cartesian == self.sphere.pole:
                continue
            
            line = Line(self.sphere.pole, cartesian)
            intersection = calculate_intersection(self.plane, line)
            
            self.plane + intersection
            
        return self.plane
