from typing import Self
from math   import sqrt

from geometry.point import Point

class Sphere:
    def __init__(self, center: Point, radius: float, error: float = 1.0) -> None:
        self.center = center
        self.radius = radius
        self.error  = error

    def calculateDistanceToCenter(self, point: Point) -> float:
        x = (point.getX() - self.center.getX())**2
        y = (point.getY() - self.center.getY())**2
        z = (point.getZ() - self.center.getZ())**2

        return sqrt(x + y + z)

    def calculateAbsoluteError(self, radius: float) -> float:
        return abs(self.radius - radius)

    def calculateRelativeError(self, absoluteError: float) -> float:
        return (absoluteError / self.radius) * 100

    # CONDITIONS
    def isOverlapping(self, point: Point) -> bool:
        radius        = self.calculateDistanceToCenter(point)
        absoluteError = self.calculateAbsoluteError(radius)
        relativeError = self.calculateRelativeError(absoluteError)
        
        return relativeError <= self.error

    # GETTERS
    def getCenter(self) -> Point:
        return self.center

    def getRadius(self) -> float:
        return self.radius

    def getError(self) -> float:
        return self.error

    # SETTERS
    def setError(self, value: float) -> Self:      
        self.error = value
        return self
