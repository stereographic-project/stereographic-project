from geometry.point  import Point
from geometry.vector import Vector

class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.vector = self.calculateVector(a, b)
        
    def calculateVector(self, a: Point, b: Point) -> Vector:
        x = b.getX() - a.getX()
        y = b.getY() - a.getY()
        z = b.getZ() - a.getZ()
        
        return Vector(x, y, z)
    
    # GETTERS
    def getVector(self) -> Vector:
        return self.vector
