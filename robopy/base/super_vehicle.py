from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, x0=None, dt=0.1, L=1.0, max_speed=1.0, rdim=0.2, covar=None):
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
        self.rdim = rdim
        self.covar = [[0, 0], [0, 0]] if covar is None else covar
        self.hist = []

    def init(self, x0=None):
        """
        Reset vehicle state and clear history
        :param x0: State to which to set vehicle. Default is the original x0.
        """
        if x0 is None:
            self.x = self.x0[:]
        else:
            self.x = x0[:]
        self.hist = []
