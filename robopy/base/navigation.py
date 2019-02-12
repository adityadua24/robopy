import heapq as hq
import numpy as np
import matplotlib.pyplot as plt
from .super_navigation import Navigation

class AStar(Navigation):
    def __init__(self, occgrid, *args, **kwargs):
        super().__init__(occgrid, *args, **kwargs)

    def plan(self, start, goal):
        self.start = start
        self.goal = goal
        shape = self._occgrid.shape
        costmap = super().calc_heuristic(shape, goal)
        backpointers = np.full(shape, None)
        open_list, closed_list = [], []
        current = (0, start)
        hq.heappush(open_list, current)
        while open_list:
            current = hq.heappop(open_list)
            if current[1] == goal:
                print("Path found!")
                break
            closed_list.append(current[1])
            for neighbor in super()._neighbors(current[1]):
                if not self._occgrid[neighbor] and neighbor not in closed_list:
                    hq.heappush(open_list, (costmap[neighbor], neighbor))
                    backpointers[neighbor] = current[1]
        if not open_list:
            print("No path found.")
            return
        self._path = []
        current = backpointers[goal]
        while current:
            self._path.append(current)
            current = backpointers[current]
        self._path.reverse()
        self._path.append(None)

    def next(self, robot):
        return self._path[self._path.index(robot) + 1]
