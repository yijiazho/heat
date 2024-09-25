import numpy as np
from matplotlib import pyplot

from utility.thomas import ThomasAlgorithm
   
length = 2
k = 0.001
temp_left = 200
temp_right = 200

total_time = 4

dx = .5
x_size = int(length / dx)
x_vec = np.linspace(0, length, x_size)

dt = .4
t_size = int(total_time/dt)
t_vec = np.linspace(0, total_time, t_size)

u = np.zeros([len(t_vec), len(x_vec)])

r = k * dt / (dx * dx)
print(r)

u[:, 0] = temp_left
u[:, -1] = temp_right

for t in range(len(t_vec) - 1):
    for x in range(1, len(x_vec) - 1):
        u[t + 1, x] = r * (dt / dx**2) * (u[t, x + 1] - 2 * u[t, x] + u[t, x - 1]) + u[t, x]