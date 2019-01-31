from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt

class Navigation(ABC):
    def __init__(self, occgrid, *args, goal=None,
                                       ax=None,
                                       inflate=0,
                                       private=False,
                                       reset=False,
                                       seed=None):
        """
        Initializes Navigation object with an occupancy grid
        :param occgrid: Occupancy grid represented as an np.ndarray.
        :param ax: Matplotlib axes on which to plot occgrid. Defaults to current axes.
        :param inflate: Number of cells by which to inflate obstacles. Defaults to 0.
        """
        self._occgrid = occgrid
        self._goal = goal
        self._ax = ax or plt.gca()

    def query(self, start, animate=False):
        """
        Find a path from start to goal using plan
        :param start: Tuple of form (x, y) representing the starting location for navigation.
        :param animate: Set to visualize plan formation. Defaults to False.
        :return path: Path from start to goal.
        """
        if animate:
            plt.ion()
        else:
            plt.ioff()
        self._start = start
        robot = start
        path = [robot]
        while True:
            robot = self.next(robot)
            if robot is None:
                path.append(self.goal)
                break
            else:
                path.append(robot)
        return path

    def plot(self, *args, **kwargs):
        pass

    @property
    def occgrid(self):
        return self._occgrid

    @property
    def goal(self):
        return self._goal

    @property
    def start(self):
        return self._start
     
    @abstractmethod
    def plan(self):
        raise NotImplementedError("Method 'plan' must be implemented in subclass.")

    @abstractmethod
    def next(self):
        raise NotImplementedError("Method 'next' must be implemented in subclass.")