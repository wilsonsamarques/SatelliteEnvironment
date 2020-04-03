# Inverted Pendulum Parameter File
#import numpy as np
#import control as cnt

# Physical parameters of the satellite known to the controller
Js = 530.7     # kg m^2
omega_max = 2 # rad/s

# parameters for animation
#length = 1.0  # length of solar panel
#width = 0.3   # width of satellite body

# Initial Conditions
theta0 = 0.0     # initial base angle
omega0 = 0.024  # initial angular rate of base, rad/s 

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 50.0   # End time of simulation
Ts = 0.1      # sample time for simulation
n_episodes = 300
n_steps = 1000
#t_plot = 0.1   # the plotting and animation is updated at this rate

# saturation limits
tau_max = 0.075  # Max torque, Nm



