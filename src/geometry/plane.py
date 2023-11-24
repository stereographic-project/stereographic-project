from typing import List, Self

from geometry    import Line
from coordinates import Cartesian

class Plane:
    points = []

    def __init__(self, center: Cartesian) -> None:
        self.center = center

    # CALCULATORS
    def calculateIntersection(self, line: Line) -> Cartesian:
        multiplier = self.center.getZ() / line.getVector().getZ()
        
        x = round(line.getVector().getX() * multiplier, 1)
        y = round(line.getVector().getY() * multiplier, 1)
        z = round(line.getVector().getZ() * multiplier, 1)
        
        return Cartesian(x, y, z)

    # CONDITIONS
    def isOverlapping(self, point: Cartesian) -> bool:
        return point.getZ() == self.center.getZ()

    # GETTERS
    def getCenter(self) -> Cartesian:
        return self.center

    def getPoints(self) -> List[Cartesian]:
        return self.points

    # SETTERS
    def setPoints(self, points: List[Cartesian]) -> Self:
        self.points = points
        return self

    # ADDERS
    def addPoint(self, point: Cartesian) -> Self:
        if self.isOverlapping(point):
            self.points.append(point)
        
        return self
