from matplotlib import pyplot
import numpy as np
from utility.visulization import Visualization
from constants import Constants

# initialization

x_size = int(Constants.LENGTH / Constants.DX)
x_vec = np.linspace(0, Constants.LENGTH, x_size)
y_size = int(Constants.LENGTH_Y / Constants.DY)
y_vec = np.linspace(0, Constants.LENGTH, y_size)
t_size = int(Constants.TOTAL_TIME/ Constants.DT)
t_vec = np.linspace(0, Constants.TOTAL_TIME, t_size)

u = np.zeros([t_size, x_size, y_size])
r_x = Constants.K * Constants.DT / (Constants.DX * Constants.DX)
r_y = Constants.K * Constants.DT / (Constants.DX * Constants.DX)
pyplot.ylim([0, Constants.TEMP_LEFT])
pyplot.xlim([0, Constants.TEMP_LEFT])

print(f"check stability, r_x = {r_x}, r_y = {r_y}")
#CFL condition to check stability

if r_x + r_y <= 0.5:
    u[:, 0] = Constants.TEMP_LEFT
    u[:, -1] = Constants.TEMP_RIGHT

    y_min = 0
    y_max = max(Constants.TEMP_LEFT, Constants.TEMP_RIGHT)
    x_min = 0
    x_max = Constants.LENGTH


    for t in range(t_size - 1):
        for x in range(1, x_size - 1):
            for y in range(1, y_size - 1):
                u[t + 1, x, y] = (u[t, x, y] + 
                            r_x * (u[t, x + 1, y] - 2 * u[t, x, y] + u[t, x - 1, y]) + 
                            r_y * (u[t, x, y + 1] - 2 * u[t, x, y] + u[t, x, y - 1]))
        # Update the boundary points
        for x in range(1, x_size - 1):
            u[t + 1, x, 0] = Constants.TEMP_LEFT
            u[t + 1, x, -1] = u[t + 1, x, -2]

    # visualization
    Visualization.static_heatmap(u, x_vec, y_vec, 100, Constants.DT, precision=4, file_name="app/plot/explicit_2d")
    Visualization.dynamic_heatmap(u, x_vec, y_vec, t_vec, Constants.DT, precision=4)
    
# Time complexity O(t_size * x_size * y_size)