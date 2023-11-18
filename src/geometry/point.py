from typing import Self

class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, point: Self) -> bool:
        return (self.x, self.y, self.z) == (point.getX(), point.getY(), point.getZ())

    # GETTERS
    def getX(self) -> float:
        return self.x
        
    def getY(self) -> float:
        return self.y
    
    def getZ(self) -> float:
        return self.z
