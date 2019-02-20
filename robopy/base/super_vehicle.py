from abc import ABC, abstractmethod
from math import sqrt, cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt

class Vehicle(ABC):
    def __init__(self, *, x0=None, dt=0.1, L=1.0, max_speed=1.0, max_steer=pi/2, rdim=0.2, covar=None, ax=None):
        """
        Initializes Vehicle object that implements the kinematic mode
        of a wheeled vehicle.
        :param x0: Initial state [x, y, theta] as a list. Defaults to [0, 0, 0].
        :param dt: Time interval in seconds. Defaults to 0.1 s.
        :param L: Wheel base in meters. Defaults to 1 m.
        :param max_speed: Maximum speed in meters per second. Defaults to 1 m/s.
        :param rdim: Robot size as fraction of plot axes. Defaults to 0.2.
        :param covar: Odometry covariance (2x2). Defaults to [[0, 0], [0, 0]]. 
        """ 
        self.x0 = [0, 0, 0] if x0 is None else x0[:] #  TODO: allow x0 to be SE2
        self.dt = dt
        self.L = L
        self.max_speed = max_speed
        self.max_steer = max_steer
        self.rdim = rdim
        self.V = [[0, 0], [0, 0]] if covar is None else covar
        self.x_hist = []
        self._ax = ax or plt.gca()

    def init(self, *, x0=None):
        """
        Reset vehicle state and clear history.
        :param x0: State to which to set vehicle. Default is the original x0.
        """
        if x0 is None:
            self.x = self.x0[:]
        else:
            self.x = x0[:]
        self.x_hist = []

    def add_driver(self, driver):
        """
        Add driver for the vehicle.
        :param driver: Driver to add to the vehicle
        """
        self.driver = driver
        driver.veh = self

    def update(self, u):
        """
        Update vehicle state.
        :param u: Control input [speed, steer]
        :return odo: True odometry value
        """
        prev = self.x[:]
        self.x[0] += u[0] * cos(self.x[2]) * self.dt
        self.x[1] += u[0] * sin(self.x[2]) * self.dt
        self.x[2] += u[0] * u[1] * self.dt / self.L
        odo = [sqrt((self.x[0] - prev[0])**2 + (self.x[1] - prev[1])**2)]
        odo.append(self.x[2] - prev[2])
        self.odometry = odo
        self.x_hist.append(self.x)
        return odo

    def step(self, *, u=None):
        """
        Advance one time step
        :param u: Control input [speed, steer]
        :return odo: Noisy odometry
        """
        u = self.control(u)
        odo = self.update(u)
        rand = np.random.randn(2, 1)
        odo[0] += rand[0, 0] * self.V[0][0] + rand[1, 0] * self.V[0][1]
        odo[1] += rand[0, 0] * self.V[0][1] + rand[1, 0] * self.V[1][1]
        return odo

    def control(self, *, u=None):
        """
        Compute the control input taking into account speed and
        steering limits. If no control input is applied, one will
        be demanded from the driver. If there is no driver, a control
        input of [0, 0] is returned.
        :param u: Control input [speed, steer]. Defaults to None.
        :return u: Clipped control input.
        """
        if u is None:
            if hasattr(self, 'driver'):
                speed, steer = self.driver.demand()
            else:
                speed, steer = 0, 0
        else:
            speed, steer = u[0], u[1]
        speed = min(self.max_speed, max(-self.max_speed, speed))
        steer = max(-self.max_steer, min(self.max_steer, steer))
        return [speed, steer]

    def run(self, *, x0=None, u=None, nsteps=1000, animate=False):
        """
        Run the vehicle model for nsteps time steps and plots the
        vehicle pose at each time step.
        :param x0: State from which to start simulation. Defaults to original
                   vehicle state.
        :param u: Control input. If a sequence of control inputs is given, this
                  will override nsteps and the numbers of steps will equal the
                  length of the input sequence. If it is a single control input,
                  it will be applied at every step for nsteps. If None, the
                  vehicle's driver will be used. Defaults to None.
        :param nsteps: Number of time steps to simulate. Defaults to 1000.
        :param animate: Set to True to plot vehicle. Defaults to False.
        :return P: State history
        """
        if hasattr(self, 'driver') and u is None:
            self.driver.init()
        self.init(x0=x0)
        if u is None or not hasattr(u[0], '__iter__'):
            for step in range(nsteps):
                self.step(u=u)
                if animate:
                    self.plot()
        else:
            for control in u:
                self.step(u=control)
                if animate:
                    self.plot()
        return self.x_hist[:]
        