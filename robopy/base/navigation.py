import heapq as hq
import numpy as np
import matplotlib.pyplot as plt
from .super_navigation import Navigation

class AStar(Navigation):
    def __init__(self, occgrid, *args, **kwargs):
        super().__init__(occgrid, *args, **kwargs)

    def plan(self, goal):
        self.goal = goal
        self.costmap = Navigation.calc_heuristic(self._occgrid.shape, goal)
        self.backpointers = np.full(self._occgrid.shape, None)
        self.open_list, self.closed_list = [], []

    def path(self, start):
        found = False
        current = (0, start)
        hq.heappush(self.open_list, current)
        while self.open_list:
            current = hq.heappop(self.open_list)
            if current[1] == self.goal:
                print("Path found!")
                found = True
                break
            self.closed_list.append(current[1])
            for neighbor in Navigation.neighbors(current[1]):
                if not self._occgrid[neighbor] and neighbor not in self.closed_list:
                    hq.heappush(self.open_list, (self.costmap[neighbor], neighbor))
                    self.backpointers[neighbor] = current[1]
        if not found:
            print("No path found.")
            return False
        self._path = []
        current = self.backpointers[goal]
        while current:
            self._path.append(current)
            current = backpointers[current]
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
