from typing import List, Self

from geometry.line   import Line
from geometry.plane  import Plane
from geometry.point  import Point
from geometry.sphere import Sphere

class Stereographic:
    def __init__(self, sphere: Sphere, plane: Plane, points: List[Point]) -> None:
        self.sphere = sphere
        self.plane  = plane
        self.points = points
    
    # TODO: REFACTOR THIS !!!
    def execute(self) -> List[Point]:
        pole = Point(0, 0, self.sphere.getRadius())
        
        points = []
        for point in self.points:
            if point == pole:
                continue
            
            if self.sphere.isOverlapping(point):
                line = Line(pole, point)
                intersection = self.plane.calculateIntersection(line)
                points.append(intersection)
        
        return points
    
    # ADDERS
    def addPoint(self, point: Point) -> Self:
        self.points.append(point)
        return self
    
    # GETTERS
    def getSphere(self) -> Sphere:
        return self.sphere
    
    def getPlane(self) -> Plane:
        return self.plane
    
    def getPoints(self) -> List[Point]:
        return self.points
