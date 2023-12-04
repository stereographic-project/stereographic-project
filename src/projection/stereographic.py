from dataclasses import dataclass

from geometry    import Plane, Sphere, Line
from coordinates import Cartesian, Spherical, to_cartesian

@dataclass
class Stereographic:
    sphere: Sphere
    plane:  Plane
    
    def to_plane(self) -> Plane:
        for point in self.sphere.points:
            cartesian = self.point_to_plane(point)
            
            if not cartesian:
                continue
            
            self.plane.add_point(cartesian)
            
        return self.plane
    
    def point_to_plane(self, point: Spherical) -> Cartesian:
        cartesian = to_cartesian(point)
            
        if cartesian == self.sphere.pole:
            return None
        
        line = Line(self.sphere.pole, cartesian)
        intersection = self.plane.calculate_intersection(line)
        
        return intersection
