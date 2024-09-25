from matplotlib import pyplot
import numpy as np


class Visualization:
    @staticmethod
    def plot_real_time(u, x_vec, t_vec, dt, y_min, y_max, step=10):
        """
        Plots the temperature distribution in real-time for each time step.
        
        Parameters:
        u : 2D array
            Temperature distribution over time and space.
        x_vec : 1D array
            Spatial positions along the rod.
        t_vec : 1D array
            Time steps.
        dt : float
            Time step size.
        y_min, y_max : float
            Min and max values for the y-axis (temperature).
        step: integer
            The step speed of the graph inreal time
        """
        for t in range(0, len(t_vec) - 1, step):
            pyplot.plot(x_vec, u[t], 'blue')
            pyplot.ylim([y_min, y_max])
            pyplot.xlim([x_vec[0], x_vec[-1]])
            pyplot.pause(0.0001)
            pyplot.cla()
            print(f"t = {t * dt:.3f} s")
        pyplot.plot(x_vec, u[-1])
        pyplot.ylabel("Temperature (C˚)")
        pyplot.xlabel("Distance Along Rod (m)")
        pyplot.ylim([y_min, y_max])
        pyplot.show()
                
    def plot_by_time(u, x_vec, dt, time_points, precision=2):
        """
        Plots the temperature distribution at specific times on the same graph.
        
        Parameters:
        u : 2D array
            Temperature distribution over time and space.
        x_vec : 1D array
            Spatial positions along the rod.
        dt : float
            Time steps
        time_points : list of float
            Specific times (in seconds) at which to plot the temperature distribution.
        precision: integer
            Numer of digits taken in time in the legend
        """
        
        for time in time_points:
            time_index = int(time / dt)
            pyplot.plot(x_vec, u[time_index], label=f't = {time:.{precision}f} s')
            
        pyplot.ylabel("Temperature (C˚)")
        pyplot.xlabel("Distance Along Rod (m)")
        pyplot.ylim([np.min(u), np.max(u)])
        pyplot.legend()
        pyplot.show()
        
    
        
