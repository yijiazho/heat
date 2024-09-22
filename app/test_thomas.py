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

