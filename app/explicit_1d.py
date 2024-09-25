import numpy as np
from matplotlib import pyplot

from constants import Constants
from utility.visulization_1d import Visualization

# initialization
x_size = int(Constants.LENGTH / Constants.DX)
x_vec = np.linspace(0, Constants.LENGTH, x_size)
t_size = int(Constants.TOTAL_TIME/ Constants.DT)
t_vec = np.linspace(0, Constants.TOTAL_TIME, t_size)
u = np.zeros([t_size, x_size])
r = Constants.K * Constants.DT / (Constants.DX * Constants.DX)

print(f"check stability, r = {r}")
#CFL condition to check stability
if r <= 0.5:
    
    u[:, 0] = Constants.TEMP_LEFT
    u[:, -1] = Constants.TEMP_RIGHT

    y_min = 0
    y_max = max(Constants.TEMP_LEFT, Constants.TEMP_RIGHT)
    x_min = 0
    x_max = Constants.LENGTH
    pyplot.ylim([y_min, y_max])
    pyplot.xlim([x_min, x_max])

    for t in range(t_size - 1):
        for x in range(1, len(x_vec) - 1):
            u[t + 1, x] = r * (u[t, x + 1] - 2 * u[t, x] + u[t, x - 1]) + u[t, x]

time_points = np.linspace(0, 0.015, 6)
Visualization.plot_by_time(u, x_vec, Constants.DT, time_points, 3)

y_min = np.min(u)
y_max = np.max(u)
Visualization.plot_real_time(u, x_vec, t_vec, Constants.DT, y_min, y_max)
# Time complexity O(t_size * x_size)