import numpy as np
from matplotlib import pyplot

from utility.thomas import ThomasAlgorithm
   
length = 2
# Thermal conductivity, in W / (m K)
# air = 0.026
# water = 0.592
# concrete = 0.92
# copper = 384.1
# aluminum alloy = 126.4
# iron = 80
k = 0.8
temp_left = 200
temp_right = 200

total_time = 0.5

dx = .1
x_size = int(length / dx)
x_vec = np.linspace(0, length, x_size)

dt = .00001
t_size = int(total_time/dt)
t_vec = np.linspace(0, total_time, t_size)

u = np.zeros([t_size, x_size])

r = k * dt / (dx * dx)
time_points = [0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.4999]

u[:, 0] = temp_left
u[:, -1] = temp_right

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
        
#     pyplot.plot(x_vec, u[t], 'blue')
#     pyplot.pause(.0001)
#     pyplot.cla()
#     pyplot.ylim([y_min, y_max])
#     pyplot.xlim([x_min, x_max])
#     print(f"t={t * dt}")
    
# pyplot.plot(x_vec, u[0])
# pyplot.ylabel("Temperature (C˚)")
# pyplot.xlabel("Distance Along Rod (m)")
# pyplot.show()

for time in time_points:
    time_index = int(time / dt)
    pyplot.plot(x_vec, u[time_index], label=f't = {time:.1f} s')
    
pyplot.ylabel("Temperature (C˚)")
pyplot.xlabel("Distance Along Rod (m)")
pyplot.ylim([y_min, y_max])
pyplot.xlim([x_min, x_max])
pyplot.legend()
pyplot.show()