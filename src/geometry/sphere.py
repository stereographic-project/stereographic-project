from typing import List, Self

from coordinates import Spherical

class Sphere:
    points = []

    def __init__(self, radius: float) -> None:
        self.radius = radius    

    # CONDITIONS
    def isOverlapping(self, point: Spherical) -> bool:
        return point.getRadius() == self.radius

    # GETTERS
    def getRadius(self) -> float:
        return self.radius
    
    def getPoints(self) -> List[Spherical]:
        return self.points

    # SETTERS
    def setPoints(self, points: List[Spherical]) -> Self:
        self.points = [point for point in points if self.isOverlapping(point)]
        return self

    # ADDERS
    def addPoint(self, point: Spherical) -> Self:
        if self.isOverlapping(point):
            self.points.append(point)
        
        return self
