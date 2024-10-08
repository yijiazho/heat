from matplotlib import pyplot
import numpy as np
from utility.visulization import Visualization
from constants import Constants
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

# initialization

x_size = int(Constants.LENGTH / Constants.DX)
x_vec = np.linspace(0, Constants.LENGTH, x_size)
y_size = int(Constants.LENGTH_Y / Constants.DY)
y_vec = np.linspace(0, Constants.LENGTH_Y, y_size)
t_size = int(Constants.TOTAL_TIME / Constants.DT)
t_vec = np.linspace(0, Constants.TOTAL_TIME, t_size)

u = np.zeros([t_size, x_size, y_size])

r_x = Constants.K * Constants.DT / (Constants.DX * Constants.DX)
r_y = Constants.K * Constants.DT / (Constants.DY * Constants.DY)

def build_sparse_matrix(): 
    N = x_size * y_size
    A = lil_matrix((N, N))
    
    # the diagonal value
    d = 1 + 2 * r_x + 2 * r_y
    
    # Loop over the grid points to construct the matrix
    for i in range(x_size):
        for j in range(y_size):
            k = j * x_size + i           
            A[k, k] = d
            
            # Set left and right neighbors
            if i > 0:
                A[k, k - 1] = -r_x
            if i < x_size - 1:
                A[k, k + 1] = -r_x
            
            # Set up and down neighbors
            if j > 0:
                A[k, k - x_size] = -r_y
            if j < y_size - 1:
                A[k, k + x_size] = -r_y

    return A

# Boundary conditions
u[:, 0, :] = Constants.TEMP_LEFT
u[:, -1, :] = Constants.TEMP_RIGHT
u[:, :, 0] = Constants.TEMP_LEFT

A = build_sparse_matrix().tocsc()

# Start time loop
for t in range(1, t_size):
    u_flattened_n = u[t - 1].flatten()
    b = u_flattened_n.copy()

    u_flattened_n1 = spsolve(A, b)
    
    # Reshape the flattened solution back into a 2D array
    u[t] = u_flattened_n1.reshape((x_size, y_size))

    # Re-apply boundary conditions
    u[t, 0, :] = Constants.TEMP_LEFT
    u[t, -1, :] = Constants.TEMP_RIGHT
    u[t, :, 0] = Constants.TEMP_LEFT
    u[t, :, -1] = u[t, :, -2]

# visualization
Visualization.static_heatmap(u, x_vec, y_vec, 500, Constants.DT, precision=1, file_name="app/plot/implicit_2d")
Visualization.dynamic_heatmap(u, x_vec, y_vec, t_vec, Constants.DT, precision=1)
# Time complexity O(t_size * (x_size * y_size)^ 1.5) because the sparse matrix solver is O(N ^ {3/2})