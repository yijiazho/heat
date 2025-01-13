import numpy as np
from matplotlib import pyplot

from constants import Constants
from utility.visulization import Visualization

def heat_equation_analytical(x, t, L, k, terms=100):
    """
    Analytical solution for the 1D heat equation with given boundary conditions.

    Parameters:
    x: float
        position(s) along the bar (0 <= x <= L).
    t: float
        time.
    L: float
        length of the bar.
    k: float
        thermal diffusivity.
    terms: int
        number of terms to include in the summation (default: 100).

    Returns:
    u: float 
        temperature at position(s) x and time t.
    """
    u = 200  # Steady-state component
    for n in range(1, 2 * terms, 2):  # Only odd n values
        coefficient = -800 / (n * np.pi)
        sine_term = np.sin(n * np.pi * x / L)
        exponential_term = np.exp(-n**2 * np.pi**2 * k * t / L**2)
        u += coefficient * sine_term * exponential_term
    return u


# initialization
x_size = int(Constants.LENGTH / Constants.DX)
x_vec = np.linspace(0, Constants.LENGTH, x_size)
t_size = int(Constants.TOTAL_TIME/ Constants.DT)
t_vec = np.linspace(0, Constants.TOTAL_TIME, t_size)
u = np.zeros([t_size, x_size])
r = Constants.K * Constants.DT / (Constants.DX * Constants.DX)

# Analytical
u_analytical = np.zeros([t_size, x_size])

for t in range(t_size - 1):
    u[t, 0] = Constants.TEMP_LEFT
    u[t, -1] = Constants.TEMP_RIGHT
    for x in range(1, len(x_vec) - 1):
        u_analytical[t, x] = heat_equation_analytical(x * Constants.DX, t * Constants.DT, Constants.LENGTH, Constants.K)


y_min = np.min(u_analytical)
y_max = np.max(u_analytical)
Visualization.plot_real_time(u_analytical, x_vec, t_vec, Constants.DT, y_min, y_max)

# Numerical
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

# time_points = np.linspace(0, 50, 6)
# Visualization.plot_by_time(u, x_vec, Constants.DT, time_points, 0, file_name="app/plot/explicit_1d")

y_min = np.min(u)
y_max = np.max(u)


        
u_array = np.stack([u, u_analytical])

Visualization.plot_array_real_time(u_array, x_vec, t_vec, Constants.DT, y_min, y_max)

# Time complexity O(t_size * x_size)

