import numpy as np
import matplotlib.pyplot as plt
import panel as pn
import param

pn.extension()

class VelocityProfile(param.Parameterized):
    u_max = param.Number(2.0, bounds=(0.1, 5.0), step=0.1, doc="Maximum Velocity")
    R = param.Number(1.0, bounds=(0.1, 5.0), step=0.1, doc="Pipe Radius")
    L = param.Number(10.0, bounds=(1.0, 20.0), step=0.5, doc="Pipe Length")

    def plot(self):
        resolution = 100  # Resolution of the grid
        z = np.linspace(0, self.L, resolution)
        r = np.linspace(0, self.R, resolution)
        Z, R_grid = np.meshgrid(z, r)

        # Calculate the velocity profile
        U = self.u_max * (1 - (R_grid / self.R) ** 2)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.contourf(Z, R_grid, U, levels=50, cmap='viridis')
        plt.colorbar(label='Velocity (m/s)')
        plt.xlabel('Length of the pipe (m)')
        plt.ylabel('Radius of the pipe (m)')
        plt.title('Velocity Profile in a Pipe')
        return plt.gcf()

    def view(self):
        return pn.Row(
            self.param,
            pn.Column(pn.bind(self.plot))
        )

velocity_profile = VelocityProfile()
pn.serve(velocity_profile.view())

