from math        import pi, cos, sin
from dataclasses import dataclass

@dataclass
class Rotation:
    x: float
    y: float
    z: float
    
    @property
    def rad_x(self) -> float:
        return self.x * pi / 180
    
    @property
    def rad_y(self) -> float:
        return self.y * pi / 180
    
    @property
    def rad_z(self) -> float:
        return self.z * pi / 180

    @property
    def matrix_x(self) -> list:
        return [
            [1, 0, 0],
            [0, cos(self.rad_x), -sin(self.rad_x)],
            [0, sin(self.rad_x),  cos(self.rad_x)],
        ]
    
    @property
    def matrix_y(self) -> list:
        return [
            [cos(self.rad_y), 0, -sin(self.rad_y)],
            [0, 1, 0],
            [sin(self.rad_y), 0,  cos(self.rad_y)],
        ]

    @property
    def matrix_z(self) -> list:
        return [
            [cos(self.rad_z), -sin(self.rad_z), 0],
            [sin(self.rad_z),  cos(self.rad_z), 0],
            [0, 0, 1],
        ]
