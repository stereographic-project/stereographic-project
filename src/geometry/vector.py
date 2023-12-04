from dataclasses import dataclass

@dataclass(frozen = True)
class Vector:
    x: float
    y: float
    z: float
