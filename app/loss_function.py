import numpy as np
from matplotlib import pyplot as plt
from constants import Constants
from utility.thomas import ThomasAlgorithm
from utility.golden import GoldenSection

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

def compute_loss(dt, dx, k, total_time, length, temp_left, temp_right, analytical_func):
    """
    Compute the loss function for a given time step (dt).

    Parameters:
    dt: float
        Time step.
    dx: float
        Spatial step.
    k: float
        Thermal diffusivity.
    total_time: float
        Total simulation time.
    length: float
        Length of the domain.
    temp_left: float
        Left boundary temperature.
    temp_right: float
        Right boundary temperature.
    analytical_func: function
        Function to compute the analytical solution.

    Returns:
    loss: float
        Computed loss function value.
    """
    x_size = int(length / dx)
    t_size = int(total_time / dt)
    # x_vec = np.linspace(0, length, x_size)
    # t_vec = np.linspace(0, total_time, t_size)
    r = k * dt / (dx * dx)
    f = np.full(x_size, 1 + 2 * r)
    g = np.full(x_size - 1, -r)
    e = np.full(x_size - 1, -r)


    # Initialize numerical solution
    u = np.zeros([t_size, x_size])
    u[:, 0] = temp_left
    u[:, -1] = temp_right

    # Solve numerically
    for t in range(t_size - 1):
        u[t] = ThomasAlgorithm.thomas_solver(f, g, e, u[t - 1])
        u[t, 0] = Constants.TEMP_LEFT
        u[t, -1] = Constants.TEMP_RIGHT


    # Compute analytical solution
    u_analytical = np.zeros([t_size, x_size])
    for t in range(t_size):
        for x in range(x_size):
            u_analytical[t, x] = analytical_func(x * dx, t * dt, length, k)

    # Compute loss
    loss = np.sum((u - u_analytical)**2) * dx * dt
    return loss


def loss_function(dt):
    return compute_loss(
        dt=dt,
        dx=Constants.DX,
        k=Constants.K,
        total_time=Constants.TOTAL_TIME,
        length=Constants.LENGTH,
        temp_left=Constants.TEMP_LEFT,
        temp_right=Constants.TEMP_RIGHT,
        analytical_func=heat_equation_analytical
    )
    
# Define time steps for visualization
lower = 0.001
upper = 0.01
start = np.log10(lower)
end = np.log10(upper)

# Plot

time_steps_log = np.logspace(start, end, 20)
time_steps = np.linspace(lower, upper, 10)

losses = []
for dt in time_steps_log:
    try:
        loss = compute_loss(
            dt=dt,
            dx=Constants.DX,
            k=Constants.K,
            total_time=Constants.TOTAL_TIME,
            length=Constants.LENGTH,
            temp_left=Constants.TEMP_LEFT,
            temp_right=Constants.TEMP_RIGHT,
            analytical_func=heat_equation_analytical
        )
        losses.append(loss)
    except ValueError as e:
        print(e)
        losses.append(np.nan)

# Plot loss vs. time step
plt.figure()
plt.plot(time_steps_log, losses, marker='o', label='Loss')
plt.xlabel("Time Step (dt)")
plt.ylabel("Loss")
plt.title("Loss vs. Time Step")
plt.grid()
plt.legend()
plt.savefig("app/plot/loss_function_log_2", dpi=300, bbox_inches='tight')
plt.show()

# Optimize

optimal_dt = GoldenSection.golden_section_search(loss_function, lower, upper)

print(optimal_dt)
# 0.00526979712198707
