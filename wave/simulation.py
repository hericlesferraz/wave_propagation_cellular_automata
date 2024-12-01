"""
Simulação de propagação de ondas em autômatos celulares.
"""

from math import sin
from config import size_x, size_y, damping, omega, initial_P, vertPos, horizPos, wall


class Simulation:
    """Classe que implementa a lógica de simulação."""
    
    def __init__(self):
        """Inicializa os estados da simulação."""
        self.frame = 0
        self.pressure = [[0.0 for _ in range(size_x)] for _ in range(size_y)]
        self._velocities = [[[0.0, 0.0, 0.0, 0.0] for _ in range(size_x)] for _ in range(size_y)]
        self.pressure[vertPos][horizPos] = initial_P

    def update_velocities(self):
        """Atualiza as velocidades de saída das células com base nas diferenças de pressão."""
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
        """Atualiza as pressões das células com base nas velocidades."""
        for i in range(size_y):
            for j in range(size_x):
                self.pressure[i][j] -= 0.5 * damping * sum(self._velocities[i][j])

    def step(self):
        """Realiza uma iteração da simulação."""
        self.pressure[vertPos][horizPos] = initial_P * sin(omega * self.frame)
        self.update_velocities()
        self.update_pressure()
        self.frame += 1
