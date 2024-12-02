"""
Propagatio simulation of Cellular Automata.
"""

from math import sin
from config import size_x, size_y, damping, omega, initial_P, vertPos, horizPos, wall


class Simulation:
    
    def __init__(self):
        """Start the states."""
        self.frame = 0
        self.pressure = [[0.0 for _ in range(size_x)] for _ in range(size_y)]
        self._velocities = [[[0.0, 0.0, 0.0, 0.0] for _ in range(size_x)] for _ in range(size_y)]
        self.pressure[vertPos][horizPos] = initial_P

    def update_velocities(self):
        """Update the velocities"""
        V = self._velocities
        P = self.pressure
        for i in range(size_y):
            for j in range(size_x):
                if wall[i][j] == 1:
                    V[i][j] = [0.0, 0.0, 0.0, 0.0]
                    continue
                cell_pressure = P[i][j]
                V[i][j][0] = V[i][j][0] + cell_pressure - P[i - 1][j] if i > 0 else cell_pressure
                V[i][j][1] = V[i][j][1] + cell_pressure - P[i][j + 1] if j < size_x - 1 else cell_pressure
                V[i][j][2] = V[i][j][2] + cell_pressure - P[i + 1][j] if i < size_y - 1 else cell_pressure
                V[i][j][3] = V[i][j][3] + cell_pressure - P[i][j - 1] if j > 0 else cell_pressure

    def update_pressure(self):
        """Update the pressure"""
        for i in range(size_y):
            for j in range(size_x):
                self.pressure[i][j] -= 0.5 * damping * sum(self._velocities[i][j])

    def step(self):
        """Make a step in simulation."""
        self.pressure[vertPos][horizPos] = initial_P * sin(omega * self.frame)
        self.update_velocities()
        self.update_pressure()
        self.frame += 1
