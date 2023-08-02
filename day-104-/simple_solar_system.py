# simple_solar_system.py

from solar_system_3d import SolarSystem, SolarSystemBody

solar_system = SolarSystem(400)

body = SolarSystemBody(solar_system, 100, velocity=(1, 1, 1))

for _ in range(100):
    solar_system.update_all()
    solar_system.draw_all()