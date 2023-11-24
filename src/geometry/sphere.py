from typing import List, Self

from coordinates import Cartesian, Spherical

class Sphere:
    points = []

    def __init__(self, center: Cartesian, radius: float) -> None:
        self.center = center
        self.radius = radius    

    # CONDITIONS
    def isOverlapping(self, point: Spherical) -> bool:
        return point.getRadius == self.radius

    # GETTERS
    def getCenter(self) -> Cartesian:
        return self.center

    def getRadius(self) -> float:
        return self.radius
    
    def getPoints(self) -> List[Spherical]:
        return self.points

    # SETTERS
    def setPoints(self, points: List[Spherical]) -> Self:
        self.points = points
        return self

    # ADDERS
    def addPoint(self, point: Spherical) -> Self:
        if self.isOverlapping(point):
            self.points.append(point)
        
        return self
