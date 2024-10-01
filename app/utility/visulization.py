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
                
    def plot_by_time(u, x_vec, dt, time_points, precision=2, file_name=None):
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
        file_name : str or None
            File name to save the figure (optional). If None, the figure is not saved.
        """
        
        for time in time_points:
            time_index = int(time / dt)
            pyplot.plot(x_vec, u[time_index], label=f't = {time:.{precision}f} s')
            
        pyplot.ylabel("Temperature (C˚)")
        pyplot.xlabel("Distance Along Rod (m)")
        pyplot.ylim([np.min(u), np.max(u)])
        pyplot.legend()
        
        if file_name:
            pyplot.savefig(file_name, dpi=300, bbox_inches='tight')
        pyplot.show()
        
    @staticmethod
    def dynamic_heatmap(u, x_vec, y_vec, t_vec, dt, step=10, precision=2):
        """
        Dynamically display a heatmap of the temperature distribution over time.
        
        Parameters:
        u : 3D numpy array
            Temperature distribution over time, x, and y.
        x_vec : 1D numpy array
            Spatial positions along the x-axis.
        y_vec : 1D numpy array
            Spatial positions along the y-axis.
        t_vec : 1D numpy array
            Time steps.
        dt : float
            Time step size.
        step : int
            Number of time steps to skip between heatmap updates (default is 10).
        """
        pyplot.figure(figsize=(8, 6))
        for t in range(0, len(t_vec), step):
            pyplot.imshow(u[t, :, :], extent=[x_vec.min(), x_vec.max(), y_vec.min(), y_vec.max()],
                       origin='lower', cmap='hot', aspect='auto', vmin = 0)
            pyplot.colorbar(label="Temperature (C°)")
            pyplot.xlabel("Y Position (m)")
            pyplot.ylabel("X Position (m)")
            pyplot.title(f"Temperature Distribution at t = {t*dt:.{precision}f} seconds")
            pyplot.pause(0.01)
            pyplot.clf()
        
        pyplot.show()
        
    @staticmethod
    def static_heatmap(u, x_vec, y_vec, time_index, dt, precision=2, cmap='hot', file_name=None):
        """
        Display and optionally save a static heatmap of the temperature distribution at a specific time step.

        Parameters:
        u : 3D numpy array
            Temperature distribution over time, x, and y.
        x_vec : 1D numpy array
            Spatial positions along the x-axis.
        y_vec : 1D numpy array
            Spatial positions along the y-axis.
        time_index : int
            The index of the time step to display.
        dt : float
            Time step size.
        precision : int
            Decimal precision for the displayed time in the title (default is 2).
        cmap : str
            Colormap for the heatmap (default is 'hot').
        file_name : str or None
            File name to save the figure (optional). If None, the figure is not saved.
        """
        pyplot.figure(figsize=(8, 6))

        # Plot the heatmap for the selected time step
        heatmap = pyplot.imshow(u[time_index, :, :], extent=[x_vec.min(), x_vec.max(), y_vec.min(), y_vec.max()],
                                origin='lower', cmap=cmap, aspect='auto', vmin=np.min(u), vmax=np.max(u))
        
        # Add colorbar and labels
        pyplot.colorbar(heatmap, label="Temperature (C°)")
        pyplot.xlabel("Y Position (m)")
        pyplot.ylabel("X Position (m)")
        pyplot.title(f"Temperature Distribution at t = {time_index * dt:.{precision}f} seconds")

        if file_name:
            pyplot.savefig(file_name, dpi=300, bbox_inches='tight')
        
        pyplot.show()
        
