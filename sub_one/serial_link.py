from abc import ABC, abstractmethod
from . import pose
import math
import numpy as np


class SerialLink:
    def __init__(self, links, name=None, base=None):
        # Argument checks
        self.links = links
        self.q = []  # List of al angles
        self.base = np.asmatrix(np.eye(4, 4))
        self.tool = np.asmatrix(np.eye(4, 4))

    @property
    def length(self):
        return len(self.links)

    def fkine(self, q):
        # q is vector of real numbers (List of angles)
        t = self.base
        for i in range(self.length):
            t = t * self.links[i].A(q[i])
        t = t * self.tool
        return t

    def plot(self, q=None):
        # PLot the serialLink object
        pass


class Link(ABC):
    # Abstract methods
    def __init__(self, j, theta, d, a, alpha, offset=None, kind='', mdh=0, flip=None):
        self.theta = theta
        self.d = d
        # self.j = j
        self.a = a
        self.alpha = alpha
        self.offset = offset
        self.kind = kind
        self.mdh = mdh
        self.flip = flip

    def A(self, q):
        sa = math.sin(self.alpha)
        ca = math.cos(self.alpha)
        if self.flip:
            q = -q + self.offset
        else:
            q = q + self.offset
        st = 0
        ct = 0
        d = 0
        if self.kind == 'r':
            st = math.sin(q)
            ct = math.cos(q)
            d = self.d
        elif self.type == 'p':
            st = math.sin(self.theta)
            ct = math.cos(self.theta)
            d = q

        se3_np = 0
        if self.mdh == 0:
            se3_np = np.matrix([[ct, -st * ca, st * sa, self.a * ct],
                                [st, ct * ca, -ct * sa, self.a * st],
                                [0, sa, ca, d],
                                [0, 0, 0, 1]])

        return se3_np


class Revolute(Link):
    def __init__(self, j, theta, d, a, alpha, offset):
        super().__init__(j=j, theta=theta, d=d, a=a, alpha=alpha, offset=offset, kind='r')
        pass


class Prismatic(Link):
    def __init__(self, j, theta, d, a, alpha, offset):
        super().__init__(j=j, theta=theta, d=d, a=a, alpha=alpha, offset=offset, kind='p')
        pass

    pass
