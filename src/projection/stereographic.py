from dataclasses import dataclass

from geometry    import Plane, Sphere, Line
from coordinates import Cartesian, Spherical, to_cartesian

from time import time_ns
from os import cpu_count

from threading import Thread

@dataclass
class Stereographic:
    sphere: Sphere
    plane:  Plane

    def to_plane(self) -> Plane:
        available_threads = cpu_count()
        print(available_threads)

        def divide_sphere(points: list[Spherical], available_threads: int) -> list:
            for i in range(0, len(points), int(len(points) / (available_threads - 1))):
                yield points[i:i + int(len(points) / (available_threads - 1))]
        
        jobs = []

        spheres = list(divide_sphere(self.sphere.points, available_threads))
        for points in spheres:
            thread = Thread(target=self.points_to_plane, args=[points], )
            jobs.append(thread)

        for job in jobs:
            job.start()

        for job in jobs:
            points = job.join()

        return self.plane
    
    def points_to_plane(self, points: list[Spherical]):
        for point in points:
            cartesian = self.point_to_plane(point)

            if not cartesian: 
                continue

            self.plane.add_point(cartesian)

    def point_to_plane(self, point: Spherical) -> Cartesian:
        cartesian = to_cartesian(point)
            
        if cartesian == self.sphere.pole:
            return None
        
        line = Line(self.sphere.pole, cartesian)
        intersection = self.plane.calculate_intersection(line)

        return intersection
