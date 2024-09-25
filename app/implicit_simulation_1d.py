import numpy as np
from matplotlib import pyplot

from utility.visulization_1d import Visualization
from utility.thomas import ThomasAlgorithm
   
# hyperparameters

# Thermal conductivity, in W / (m K)
# air = 0.026
# water = 0.592
# concrete = 0.92
# copper = 384.1
# aluminum alloy = 126.4
# iron = 80
k = 80
length = 2
temp_left = 200
temp_right = 200
total_time = 0.5
dx = .1
dt = .00001
# --------------------

# initialization
x_size = int(length / dx)
x_vec = np.linspace(0, length, x_size)
t_size = int(total_time/dt)
t_vec = np.linspace(0, total_time, t_size)
u = np.zeros([t_size, x_size])
r = k * dt / (dx * dx)
u[0, 0] = temp_left
u[0, -1] = temp_right

y_min = 0
y_max = max(temp_left, temp_right)
x_min = 0
x_max = length
pyplot.ylim([y_min, y_max])
pyplot.xlim([x_min, x_max])

f = np.full(x_size, 1 + 2 * r)
g = np.full(x_size - 1, -r)
e = np.full(x_size - 1, -r)

for t in range(1, t_size - 1):
    
    u[t] = ThomasAlgorithm.thomas_solver(f, g, e, u[t - 1])
    # Reapply boundary conditions
    u[t, 0] = temp_left
    u[t, -1] = temp_right

time_points = np.linspace(0, 0.015, 6)
Visualization.plot_by_time(u, x_vec, dt, time_points, precision=3)

y_min = np.min(u)
y_max = np.max(u)
Visualization.plot_real_time(u, x_vec, t_vec, dt, y_min, y_max)