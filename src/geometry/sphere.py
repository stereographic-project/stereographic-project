from geometry.point import Point

class Sphere:
    def __init__(self, center: Point, radius: int) -> None:
        self.center = center
        self.radius = radius
        
    def isOverlapping(self, point: Point) -> bool:
        x = (point.getX() - self.center.getX())**2
        y = (point.getY() - self.center.getY())**2
        z = (point.getZ() - self.center.getZ())**2
        
        return x + y + z == self.radius**2
