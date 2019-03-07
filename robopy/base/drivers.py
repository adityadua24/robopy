from random import Random
from time import time
from math import atan2
from .common import ang_diff

class RandomPath:
    def __init__(self, dim, *, speed=1.0, dthresh=None):
        """
        Create a driver for the Vehicle class to steer
        the vehicle through randomly generated waypoints.
        :param dim: Dimension of rectangular region in which random
                    waypoints will be generated. Should be number or
                    iterable. Allowed usage:
                    Scalar; X: -dim to +dim, Y: -dim to +dim
                    1x2; X: -dim[0] to +dim[0], Y: -dim[1] to +dim[1]
                    1x4; X: -dim[0] to +dim[1], Y: -dim[2] to +dim[3]
        :param speed: Speed along path. Defaults to 1 m/s.
        :param dthresh: Distance from goal at which next goal is chosen.
                        Defaults to 2.5% of axes width.
        """
        if not hasattr(dim, '__iter__'):
            self.xrange = [-dim, dim]
            self.yrange = [-dim, dim]
        elif len(dim) == 2:
            self.xrange = [-dim[0], dim[0]]
            self.yrange = [-dim[1], dim[1]]
        elif len(dim) == 4:
            self.xrange = [-dim[0], dim[1]]
            self.yrange = [-dim[2], dim[3]]
        else:
            raise ValueError('dim should be scalar, 1x2, or 1x4')

        self.speed = speed
        if dthresh is None:
            self.dthresh = 0.025 * (self.xrange[1] - self.xrange[0])
        else:
            self.dthresh = dthresh

        self._seed = time()
        self.init()

    def init(self):
        """
        Reset random number generator
        """
        self.goal = None
        self._randstream.seed(self._seed)

    def _set_goal(self):
        pass

    def demand(self):
        """
        Compute speed and heading to waypoint
        :return speed: Speed at which to drive vehicle along path to
                       next waypoint
        :return steer: Steer angle
        """
        if self.goal is None:
            self._set_goal()
        speed = self.speed
        goal_heading = atan2(self.goal[1] - self.veh.x[1],
            self.goal[0] - self.veh.x[0])
        d_heading = ang_diff(goal_heading, self.veh.x[2])