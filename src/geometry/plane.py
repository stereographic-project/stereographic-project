from geometry.line  import Line
from geometry.point import Point


class Plane:
    def __init__(self, center: Point) -> None:
        self.center = center
    
    def calculateIntersection(self, line: Line) -> Point:
        multiplier = self.center.getZ() / line.getVector().getZ()
        
        x = round(line.getVector().getX() * multiplier, 1)
        y = round(line.getVector().getY() * multiplier, 1)
        z = round(line.getVector().getZ() * multiplier, 1)

        return Point(x, y, z)
    
    # CONDITIONS
    def isOverlapping(self, point: Point) -> bool:
        return point.getZ() == self.center.getZ()
    
    # GETTERS
    def getCenter(self) -> Point:
        return self.center
