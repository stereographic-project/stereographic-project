from geometry    import Vector
from coordinates import Cartesian

class Line:
    vector: Vector
    
    def __init__(self, a: Cartesian, b: Cartesian) -> None:
        self.a = a
        self.b = b
        
        self.calculateVector()
    
    # CALCULATORS
    def calculateVector(self) -> None:
        x = self.b.getX() - self.a.getX()
        y = self.b.getY() - self.a.getY()
        z = self.b.getZ() - self.a.getZ()
        
        self.vector = Vector(x, y, z)

    # GETTERS
    def getA(self) -> Cartesian:
        return self.a
    
    def getB(self) -> Cartesian:
        return self.b
    
    def getVector(self) -> Vector:
        return self.vector
