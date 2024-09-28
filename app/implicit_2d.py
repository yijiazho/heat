from matplotlib import pyplot
import numpy as np
from utility.visulization import Visualization
from constants import Constants

def gauss_seidel(u, b, r_x, r_y, max_iter=1000, tol=1e-6):
    """
    Gauss-Seidel method to solve the implicit 2D heat equation.
    
    Parameters:
    u : 2D numpy array
        Current temperature distribution.
    b : 2D numpy array
        Right-hand side of the system (previous time step).
    r_x, r_y : float
        Discretization parameters in x and y directions.
    max_iter : int
        Maximum number of iterations.
    tol : float
        Tolerance for convergence.
        
    Returns:
    u : 2D numpy array
        Updated temperature distribution after solving the linear system.
    """
    for iteration in range(max_iter):
        u_old = u.copy()  # Store the old solution to check for convergence
        for x in range(1, u.shape[0] - 1):
            for y in range(1, u.shape[1] - 1):
                u[x, y] = (r_x * (u[x + 1, y] + u[x - 1, y]) +
                           r_y * (u[x, y + 1] + u[x, y - 1]) + b[x, y]) / (1 + 2 * (r_x + r_y))
        
        # Check for convergence
        if np.linalg.norm(u - u_old) < tol:
            break
    return u

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

print(f"check stability, r_x = {r_x}, r_y = {r_y}")

# Boundary conditions
u[:, 0, :] = Constants.TEMP_LEFT  # Left boundary
u[:, -1, :] = Constants.TEMP_RIGHT  # Right boundary

# Start time loop
for t in range(1, t_size):
    # Right-hand side of the equation (previous time step)
    b = u[t - 1, :, :]
    
    # Solve using Gauss-Seidel method
    u[t, :, :] = gauss_seidel(u[t - 1, :, :], b, r_x, r_y)

    # Boundary conditions after each time step
    u[t, :, 0] = Constants.TEMP_LEFT  # Left boundary
    u[t, :, -1] = u[t, :, -2]  # Right boundary (insulated)

# visualization
Visualization.dynamic_heatmap(u, x_vec, y_vec, t_vec, Constants.DT, precision=4)
