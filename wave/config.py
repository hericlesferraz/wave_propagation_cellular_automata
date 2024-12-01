"""
Configurações para a simulação de autômatos celulares.
"""

import sys
from numpy import pi

scale = 50
size_x = 6 * scale
size_y = 4 * scale
damping = 0.99
omega = 3 / (2 * pi)

initial_P = 200
vertPos = size_y - 3 * scale
horizPos = 1 * scale
wallTop = size_y - 3 * scale
wall_x_pos = 2 * scale
max_pressure = initial_P / 2
min_presure = -initial_P / 2

argc = len(sys.argv)
if argc > 1 and sys.argv[1] == '1':
    wall = [[1 if x == wall_x_pos and wallTop < y < size_y else 0 for x in range(size_x)] for y in range(size_y)]

elif argc > 1 and sys.argv[1] == '2':
    wall = [[1 if (x == wall_x_pos and wallTop + scale < y < size_y) or
                  (wall_x_pos - scale < x < wall_x_pos and x - wall_x_pos == y - wallTop - scale - 1) or
                  (wall_x_pos < x < wall_x_pos + scale and x - wall_x_pos == -y + wallTop + scale + 1)
             else 0
             for x in range(size_x)] for y in range(size_y)]

else:
    wall = [[1 if (x == wall_x_pos and wallTop + scale < y < size_y) or
                  (wall_x_pos - scale < x < wall_x_pos and x - wall_x_pos == y - wallTop - scale - 1) or
                  (wall_x_pos < x < wall_x_pos + scale and x - wall_x_pos == -y + wallTop + scale + 1) or
                  (wall_x_pos - 0.75 * scale < x < wall_x_pos - scale / 2 and x - wall_x_pos == -y + wallTop - scale / 2 + 1) or
                  (wall_x_pos + scale / 2 < x < wall_x_pos + 0.75 * scale and x - wall_x_pos == y - wallTop + scale / 2 - 1)
             else 0
             for x in range(size_x)] for y in range(size_y)]
