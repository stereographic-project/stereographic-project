from math        import pi
from dataclasses import dataclass

@dataclass
class Spherical:
    radius: float
    theta:  float
    phi:    float

    @property
    def theta_radian(self) -> float:
        return self.theta * pi / 180

    @property
    def phi_radian(self) -> float:
        return self.phi * pi / 180
