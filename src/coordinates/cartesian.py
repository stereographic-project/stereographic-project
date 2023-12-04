from dataclasses import dataclass

@dataclass(frozen = True)
class Cartesian:
    x: float
    y: float
    z: float
