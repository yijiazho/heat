import numpy as np
import matplotlib.pyplot as plt
from constants import Constants
from utility.visulization import Visualization
from utility.thomas import ThomasAlgorithm

# Optimal dt found from golden section search
optimal_dt = 0.00527  

# Define the specific time points for plotting
time_points = [0, 10, 20, 30, 40, 50]  # in seconds

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

def solve_implicit_heat_equation(dt, dx, k, total_time, length, temp_left, temp_right):
    """
    Solves the heat equation using an implicit method (Crank-Nicolson/Backward Euler).

    Parameters:
    dt: float - Time step.
    dx: float - Spatial step.
    k: float - Thermal diffusivity.
    total_time: float - Total simulation time.
    length: float - Length of the domain.
    temp_left: float - Left boundary temperature.
    temp_right: float - Right boundary temperature.

    Returns:
    x_vec: array - Spatial positions.
    t_vec: array - Time values.
    u: array - Numerical temperature distribution.
    u_analytical: array - Analytical solution.
    """
    x_size = int(length / dx)
    t_size = int(total_time / dt)
    x_vec = np.linspace(0, length, x_size)
    t_vec = np.linspace(0, total_time, t_size)

    r = k * dt / (dx * dx)
    f = np.full(x_size, 1 + 2 * r)
    g = np.full(x_size - 1, -r)
    e = np.full(x_size - 1, -r)

    # Initialize numerical solution
    u = np.zeros([t_size, x_size])
    u[:, 0] = temp_left
    u[:, -1] = temp_right

    # Solve numerically using the implicit method
    for t in range(t_size - 1):
        u[t + 1] = ThomasAlgorithm.thomas_solver(f, g, e, u[t])
        u[t + 1, 0] = Constants.TEMP_LEFT
        u[t + 1, -1] = Constants.TEMP_RIGHT

    # Compute analytical solution
    u_analytical = np.zeros([t_size, x_size])
    for t in range(t_size):
        for x in range(x_size):
            u_analytical[t, x] = heat_equation_analytical(x * dx, t * dt, length, k)

    return x_vec, t_vec, u, u_analytical

# Solve the heat equation with the optimal time step
x_vec, t_vec, u_numerical, u_analytical = solve_implicit_heat_equation(
    dt=optimal_dt,
    dx=Constants.DX,
    k=Constants.K,
    total_time=Constants.TOTAL_TIME,
    length=Constants.LENGTH,
    temp_left=Constants.TEMP_LEFT,
    temp_right=Constants.TEMP_RIGHT
)

# Extract the numerical and analytical solutions at the given time points
time_indices = [int(t / optimal_dt) for t in time_points]  # Convert seconds to indices

# Plot numerical vs analytical solution at selected time points
plt.figure(figsize=(10, 6))
for idx, t in zip(time_indices, time_points):
    plt.plot(x_vec, u_numerical[idx], label=f'Numerical (t={t}s)', linestyle='--')
    plt.plot(x_vec, u_analytical[idx], label=f'Analytical (t={t}s)', linestyle='-')

plt.xlabel("Position x (m)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Profile at Different Time Points")
plt.legend()
plt.grid()
plt.savefig("app/plot/temperature_profile_optimal_dt.png", dpi=300, bbox_inches='tight')
plt.show()

# Compute and plot the difference (error) between numerical and analytical solutions
plt.figure(figsize=(10, 6))
for idx, t in zip(time_indices, time_points):
    error = u_numerical[idx] - u_analytical[idx]
    plt.plot(x_vec, error, label=f'Error (t={t}s)')

plt.xlabel("Position x (m)")
plt.ylabel("Error (Numerical - Analytical)")
plt.title("Error at Different Time Points")
plt.legend()
plt.grid()
plt.savefig("app/plot/error_profile_optimal_dt.png", dpi=300, bbox_inches='tight')
plt.show()
