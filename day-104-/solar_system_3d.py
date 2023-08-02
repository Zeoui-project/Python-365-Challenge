# solar_system_3d.py

import matplotlib.pyplot as plt

from vectors import Vector

# class SolarSystem:
# ...  

class SolarSystemBody:
    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)

        self.solar_system.add_body(self)