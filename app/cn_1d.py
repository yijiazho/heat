import numpy as np
from matplotlib import pyplot

from utility.matrix import MatrixUtils
from constants import Constants
from utility.visulization_1d import Visualization

# Crank-Nicolson method guaranteed to be stable

# initialization
x_size = int(Constants.LENGTH / Constants.DX)
x_vec = np.linspace(0, Constants.LENGTH, x_size)
t_size = int(Constants.TOTAL_TIME/ Constants.DT)
t_vec = np.linspace(0, Constants.TOTAL_TIME, t_size)
u = np.zeros([t_size, x_size])
r = Constants.K * Constants.DT / (2 * Constants.DX * Constants.DX)

u[0, 0] = Constants.TEMP_LEFT
u[0, -1] = Constants.TEMP_RIGHT

y_min = 0
y_max = max(Constants.TEMP_LEFT, Constants.TEMP_RIGHT)
x_min = 0
x_max = Constants.LENGTH
pyplot.ylim([y_min, y_max])
pyplot.xlim([x_min, x_max])

def build_matrix(n, f, g, e):
    A = np.zeros((n, n))
    A[n - 1, n - 1] = f
    for i in range(n - 1):
        A[i, i] = f
        A[i, i + 1] = g
        A[i + 1, i] = e
    return A
# A_1 @ u[t + 1] = A_2 @ u[t]
# u[t + 1] = inverse(A_1) @ A_2 @ u[t]
A_1 = build_matrix(x_size, 1 + 2 * r, -r, -r)
A_2 = build_matrix(x_size, 1 - 2 * r, r, r)
M = MatrixUtils.matrix_multiply(MatrixUtils.matrix_inverse(A_1), A_2)

for t in range(t_size - 1):      
    u[t + 1] = MatrixUtils.matrix_transpose(MatrixUtils.matrix_multiply(M, MatrixUtils.matrix_transpose(u[t])))
    u[t + 1, 0] = Constants.TEMP_LEFT
    u[t + 1, -1] = Constants.TEMP_RIGHT
            
time_points = np.linspace(0, 0.015, 6)
Visualization.plot_by_time(u, x_vec, Constants.DT, time_points, 3)

y_min = np.min(u)
y_max = np.max(u)
Visualization.plot_real_time(u, x_vec, t_vec, Constants.DT, y_min, y_max)
# Time complexity O(t_size * x_size * x_size)