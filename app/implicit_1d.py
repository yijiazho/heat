import numpy as np
from matplotlib import pyplot

from constants import Constants
from utility.visulization import Visualization
from utility.thomas import ThomasAlgorithm

# initialization
x_size = int(Constants.LENGTH / Constants.DX)
x_vec = np.linspace(0, Constants.LENGTH, x_size)
t_size = int(Constants.TOTAL_TIME/ Constants.DT)
t_vec = np.linspace(0, Constants.TOTAL_TIME, t_size)
u = np.zeros([t_size, x_size])
r = Constants.K * Constants.DT / (Constants.DX * Constants.DX)
u[0, 0] = Constants.TEMP_LEFT
u[0, -1] = Constants.TEMP_RIGHT

y_min = 0
y_max = max(Constants.TEMP_LEFT, Constants.TEMP_RIGHT)
x_min = 0
x_max = Constants.LENGTH
pyplot.ylim([y_min, y_max])
pyplot.xlim([x_min, x_max])

f = np.full(x_size, 1 + 2 * r)
g = np.full(x_size - 1, -r)
e = np.full(x_size - 1, -r)

for t in range(1, t_size - 1):
    
    u[t] = ThomasAlgorithm.thomas_solver(f, g, e, u[t - 1])
    # Reapply boundary conditions
    u[t, 0] = Constants.TEMP_LEFT
    u[t, -1] = Constants.TEMP_RIGHT

time_points = np.linspace(0, 50, 6)
Visualization.plot_by_time(u, x_vec, Constants.DT, time_points, precision=0, file_name="app/plot/implicit_1d")

y_min = np.min(u)
y_max = np.max(u)
Visualization.plot_real_time(u, x_vec, t_vec, Constants.DT, y_min, y_max)
# Time complexity O(t_size * x_size)