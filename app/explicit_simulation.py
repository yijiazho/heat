import numpy as np
from matplotlib import pyplot

length = 2
# Thermal conductivity, in W / (m K)
# air = 0.026
# water = 0.592
# concrete = 0.92
# copper = 384.1
# aluminum alloy = 126.4
# iron = 80
k = 100
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
time_points = [0, 0.0005,  0.001, 0.002, 0.004, 0.005]

print(r)
#CFL condition to check stability
if r <= 0.5:
    u[:, 0] = temp_left
    u[:, -1] = temp_right

    y_min = 0
    y_max = max(temp_left, temp_right)
    x_min = 0
    x_max = length
    pyplot.ylim([y_min, y_max])
    pyplot.xlim([x_min, x_max])

    for t in range(len(t_vec) - 1):
        for x in range(1, len(x_vec) - 1):
            u[t + 1, x] = r * (u[t, x + 1] - 2 * u[t, x] + u[t, x - 1]) + u[t, x]

        # pyplot.plot(x_vec, u[t], 'blue')
        # pyplot.pause(.0001)
        # pyplot.cla()
        # pyplot.ylim([y_min, y_max])
        # pyplot.xlim([x_min, x_max])
        # print(f"t={t * dt}")


    # Plot temperature distribution at specific times on the same graph
    for time in time_points:
        time_index = int(time / dt)
        pyplot.plot(x_vec, u[time_index], label=f't = {time:.1f} s')
    
    pyplot.ylabel("Temperature (C˚)")
    pyplot.xlabel("Distance Along Rod (m)")
    pyplot.ylim([y_min, y_max])
    pyplot.xlim([x_min, x_max])
    pyplot.legend()
    pyplot.show()
    