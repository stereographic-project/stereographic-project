from geometry    import Plane, Sphere, Line
from coordinates import Cartesian, Translator

class Stereographic:
    def __init__(self, sphere: Sphere, plane: Plane) -> None:
        self.sphere = sphere
        self.plane  = plane
    
    def execute(self) -> Plane:
        pole = Cartesian(0, 0, self.sphere.getRadius())
        
        for point in self.sphere.getPoints():
            if point == pole:
                continue
            
            if not self.sphere.isOverlapping(point):
                continue
            
            cartesian    = Translator.sphericalToCartesian(point)
            line         = Line(pole, cartesian)
            intersection = self.plane.calculateIntersection(line)
            
            self.plane.addPoint(intersection)
        
        return self.plane
    
    # GETTERS
    def getSphere(self) -> Sphere:
        return self.sphere
    
    def getPlane(self) -> Plane:
        return self.plane
