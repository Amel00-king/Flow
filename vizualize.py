import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive
import ipywidgets as widgets
from IPython.display import display  # Import the display function

# Parameters
resolution = 100  # Resolution of the grid

def plot_velocity_profile(u_max, R, L):
    # Create a grid
    z = np.linspace(0, L, resolution)
    r = np.linspace(0, R, resolution)
    Z, R_grid = np.meshgrid(z, r)

    # Calculate the velocity profile
    U = u_max * (1 - (R_grid / R)**2)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.contourf(Z, R_grid, U, levels=50, cmap='viridis')
    plt.colorbar(label='Velocity (m/s)')
    plt.xlabel('Length of the pipe (m)')
    plt.ylabel('Radius of the pipe (m)')
    plt.title('Velocity Profile in a Pipe')
    plt.show()

# Create interactive widgets
u_max_slider = widgets.FloatSlider(value=2.0, min=0.1, max=5.0, step=0.1, description='Max Velocity')
R_slider = widgets.FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Pipe Radius')
L_slider = widgets.FloatSlider(value=10.0, min=1.0, max=20.0, step=0.5, description='Pipe Length')

# Display the interactive plot
interactive_plot = interactive(plot_velocity_profile, u_max=u_max_slider, R=R_slider, L=L_slider)
output = interactive_plot.children[-1]
output.layout.height = '400px'
display(interactive_plot)

