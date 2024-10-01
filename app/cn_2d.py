import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from matplotlib import pyplot
from utility.visulization import Visualization
from constants import Constants

x_size = int(Constants.LENGTH / Constants.DX)
x_vec = np.linspace(0, Constants.LENGTH, x_size)
y_size = int(Constants.LENGTH_Y / Constants.DY)
y_vec = np.linspace(0, Constants.LENGTH_Y, y_size)
t_size = int(Constants.TOTAL_TIME / Constants.DT)
t_vec = np.linspace(0, Constants.TOTAL_TIME, t_size)

u = np.zeros([t_size, x_size, y_size])

r_x = Constants.K * Constants.DT / (2 * Constants.DX ** 2)
r_y = Constants.K * Constants.DT / (2 * Constants.DY ** 2)

# Boundary conditions
u[:, 0, :] = Constants.TEMP_LEFT
u[:, -1, :] = Constants.TEMP_RIGHT
u[:, :, 0] = Constants.TEMP_LEFT

def build_crank_nicolson_matrix():
    N = x_size * y_size
    A_1 = lil_matrix((N, N))
    A_2 = lil_matrix((N, N))

    d_1 = 1 + 2 * r_x + 2 * r_y
    d_2 = 1 - 2 * r_x - 2 * r_y

    for i in range(x_size):
        for j in range(y_size):
            k = j * x_size + i

            A_1[k, k] = d_1
            A_2[k, k] = d_2
            
            if i > 0:
                A_1[k, k - 1] = -r_x
                A_2[k, k - 1] = r_x
            if i < x_size - 1:
                A_1[k, k + 1] = -r_x
                A_2[k, k + 1] = r_x

            if j > 0:
                A_1[k, k - x_size] = -r_y
                A_2[k, k - x_size] = r_y
            if j < y_size - 1:
                A_1[k, k + x_size] = -r_y
                A_2[k, k + x_size] = r_y

    return A_1.tocsc(), A_2.tocsc()

A_1, A_2 = build_crank_nicolson_matrix()

# Start time loop
for t in range(1, t_size):
    # Flatten the u field at the current time step (u^n)
    u_flattened_n = u[t - 1].flatten()
    b = A_2 @ u_flattened_n

    u_flattened_n1 = spsolve(A_1, b)

    # Reshape the flattened solution back into a 2D array
    u[t] = u_flattened_n1.reshape((x_size, y_size))

    # Re-apply boundary conditions (just for safety)
    u[t, 0, :] = Constants.TEMP_LEFT
    u[t, -1, :] = Constants.TEMP_RIGHT
    u[t, :, 0] = Constants.TEMP_LEFT

# visualization
Visualization.static_heatmap(u, x_vec, y_vec, 100, Constants.DT, precision=4, file_name="app/plot/cn_2d")
Visualization.dynamic_heatmap(u, x_vec, y_vec, t_vec, Constants.DT, precision=4)
# Time complexity O(t_size * (x_size * y_size)^ 1.5) because the sparse matrix solver is O(N ^ {3/2})