class Cartesian:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    # DISPLAY
    def display(self) -> tuple:
        return (self.x, self.y, self.z)
    
    # GETTERS
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

