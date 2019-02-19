import heapq as hq
import numpy as np
import matplotlib.pyplot as plt
from .super_navigation import Navigation

class AStar(Navigation):
    def __init__(self, occgrid, *args, **kwargs):
        super().__init__(occgrid, *args, **kwargs)

    def plan(self, goal, costmap=None):
        self.goal = goal
        self.g = np.full(self._occgrid.shape, 0)
        self.h = Navigation.calc_heuristic(self._occgrid.shape, goal)
        self.b = np.full(self._occgrid.shape, None)
        self.open_list, self.closed_list = [], []
        if costmap is None:
            self.costmap = np.ones(self._occgrid.shape) 
        else:
            self.costmap = costmap

    def path(self, start):
        found = False
        current = (0, start)
        hq.heappush(self.open_list, current)
        while self.open_list:
            current = hq.heappop(self.open_list)
            if current[1] == self.goal:
                print("Path found!")
                print("Total cost: {}".format(self.g[self.goal]))
                found = True
                break
            self.closed_list.append(current[1])
            for neighbor in Navigation.neighbors(self._occgrid.shape, current[1]):
                if not self._occgrid[neighbor] and neighbor not in self.closed_list:
                    self.g[neighbor] = self.g[current[1]] + self.costmap[neighbor]
                    hq.heappush(self.open_list, (self.h[neighbor], neighbor))
                    self.b[neighbor] = current[1]
        if not found:
            print("No path found.")
            return False
        self._path = []
        current = self.b[self.goal]
        while current:
            self._path.append(current)
            current = self.b[current]
        self._path.reverse()
        self._path.append(None)
        return True

    def query(self, start, *args, **kwargs):
        if self.path(start):
            return super().query(start, *args, **kwargs)

    def next(self, robot):
        return self._path[self._path.index(robot) + 1]

def DStar(Navigation):
    def __init__(self, occgrid, *args, **kwargs):
        super().__init__(occgrid, *args, **kwargs)

    def plan(self, goal):
        pass
