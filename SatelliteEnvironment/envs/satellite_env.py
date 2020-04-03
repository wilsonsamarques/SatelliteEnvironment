import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path

import SatelliteParam as P

class SatelliteEnv(gym.Env):
    metadata = {
        'render.modes' : ['human', 'rgb_array'],
        'video.frames_per_second' : 30
    }

    def __init__(self):
        #super(SatelliteEnv, self).__init__()

        self.state = np.array([P.theta0, P.omega0])
        self.Ts = P.Ts
        self.Js = P.Js
        self.max_torque = P.tau_max
        self.max_omega = P.omega_max

    
        self.viewer = None
        # Define action and observation space
        # They must be gym.spaces objects
        high = np.array([1., self.max_omega], dtype=np.float32)
        self.action_space = spaces.Box(low=-self.max_torque, high=self.max_torque, shape=(1,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-high, high=high, dtype=np.float32)

        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, u):

        theta = self.state.item(0)
        omega = self.state.item(1)

        dt = self.Ts

        u = np.clip(u, -self.max_torque, self.max_torque)[0]
        self.rk4_step(u)  # propagate the state by one time sample
        y = self.h()  # return the corresponding output


        costs = angle_normalize(theta)**2 + .1*omega**2 + .001*(u**2)

        
        #newthdot = np.clip(newthdot, -self.max_speed, self.max_speed) #pylint: disable=E1111

        return y, -costs, False, {}

    def f(self, state, u):
        # Return xdot = f(x,u)

        theta = state.item(0)
        omega = state.item(1)
        tau = u
        # The equation of motion.
        thetaddot = tau/self.Js
        # build xdot and return
        xdot = np.array([omega, thetaddot])
        return xdot

    def reset(self):
        high = np.array([np.pi, 1])
        self.state = self.np_random.uniform(low=-high, high=high)
        return self.h()

    def h(self):
        # return y = h(x)
        theta = self.state.item(0)
        thetadot = self.state.item(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        y = np.array([np.cos(theta), thetadot])
        return y

    def render(self, mode='human'):
        pass
    
    def rk4_step(self, u):
        # Integrate ODE using Runge-Kutta RK4 algorithm
        F1 = self.f(self.state, u)
        F2 = self.f(self.state + self.Ts / 2 * F1, u)
        F3 = self.f(self.state + self.Ts / 2 * F2, u)
        F4 = self.f(self.state + self.Ts * F3, u)
        self.state = self.state + (self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4))

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None

def angle_normalize(x):
    return (((x+np.pi) % (2*np.pi)) - np.pi)