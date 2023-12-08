from math        import pi, cos, sin
from dataclasses import dataclass

from rotations   import Matrix

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
    def matrix_x(self) -> Matrix:
        matrix_x = [
            [1, 0, 0],
            [0, cos(self.rad_x), -sin(self.rad_x)],
            [0, sin(self.rad_x),  cos(self.rad_x)],
        ]
        
        return Matrix(matrix_x)
    
    @property
    def matrix_y(self) -> Matrix:
        matrix_y = [
            [cos(self.rad_y), 0, -sin(self.rad_y)],
            [0, 1, 0],
            [sin(self.rad_y), 0,  cos(self.rad_y)],
        ]
        
        return Matrix(matrix_y)

    @property
    def matrix_z(self) -> Matrix:
        matrix_z = [
            [cos(self.rad_z), -sin(self.rad_z), 0],
            [sin(self.rad_z),  cos(self.rad_z), 0],
            [0, 0, 1],
        ]
        
        return Matrix(matrix_z)

