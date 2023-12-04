from math        import pi
from dataclasses import dataclass

@dataclass(frozen = True)
class Spherical:
    radius: float
    theta:  float
    phi:    float

    @property
    def rad_theta(self) -> float:
        return self.theta * pi / 180

    @property
    def rad_phi(self) -> float:
        return self.phi * pi / 180
