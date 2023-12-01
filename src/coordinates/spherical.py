from math import pi

class Spherical:
    def __init__(self, radius: float, theta: float, phi: float) -> None:
        self.radius = radius
        self.theta  = theta
        self.phi    = phi

    def toRadians(self) -> None:
        multiplier = pi / 180
        
        self.theta *= multiplier
        self.phi   *= multiplier

    def toDegrees(self) -> None:
        multiplier = 180 / pi
        
        self.theta *= multiplier
        self.phi   *= multiplier
    
    # DISPLAY
    def display(self) -> tuple:
        return (self.radius, self.theta, self.phi)
    
    # GETTERS
    def getRadius(self) -> float:
        return self.radius

    def getTheta(self) -> float:
        return self.theta

    def getPhi(self) -> float:
        return self.phi
