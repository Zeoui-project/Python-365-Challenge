# solar_system_3d.py

import math
import matplotlib.pyplot as plt

from vectors import Vector

class SolarSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()

    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.001)
        self.ax.clear()

# class SolarSystemBody:
# ...