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

    def query(self, start, animate=False, dt=1e-3):
        """
        Find a path from start to goal using plan
        :param start: Tuple of form (x, y) representing the starting location for navigation.
        :param animate: Set to visualize plan formation. Defaults to False.
        :return path: Path from start to goal.
        """
        self._plot()
        if animate:
            plt.ion()
        else:
            plt.ioff()
        robot = start
        path = [robot]
        while robot:
            self._ax.plot(robot[1], robot[0], 'r.')
            if animate:
                plt.pause(dt)
            robot = self.next(robot)
            path.append(robot)
        plt.show()
        return path

    def _plot(self, *args, **kwargs):
        plt.cla()
        plt.ion()
        self._ax.imshow(self._occgrid, cmap='gray_r')
        if self.goal:
            self._ax.plot(self.goal[1], self.goal[0], 'g*')
        plt.pause(1e-3)

    @property
    def occgrid(self):
        return self._occgrid

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        if goal is not None:
            assert self._occgrid[goal] == 0, 'Goal must be in free space'
        self._goal = goal

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        if start is not None:
            assert self._occgrid[start] == 0, 'Start must be in free space'
        self._start = start

    @property
    def path(self):
        return self._path

    @abstractmethod
    def plan(self, *args, **kwargs):
        raise NotImplementedError("Method 'plan' must be implemented in subclass.")

    @abstractmethod
    def next(self, *args, **kwargs):
        raise NotImplementedError("Method 'next' must be implemented in subclass.")

    @staticmethod
    def calc_heuristic(size, goal, type='cityblock'):
        m, n = size
        Y, X = np.meshgrid([i for i in range(m)],
                           [i for i in range(n)])
        return abs(X - goal[0]) + abs(Y - goal[1])

    @staticmethod
    def neighbors(size, current):
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = size
        for dy, dx in moves:
            y = current[0] + dy
            x = current[1] + dx
            if y < m and y >= 0 and x < n and x >= 0:
                yield (y, x)