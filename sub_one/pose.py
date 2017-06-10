import numpy as np
from sub_one.super_pose import Pose
import math


class SO2(Pose):
    def __init__(self, t=None, unit='rad'):
        if t is None:
            self._data = np.asmatrix(np.eye(2, 2))
        elif isinstance(t, SO2):
            self._data = t.data
        elif isinstance(t, np.matrix):
            self._data = t
        else:
            pass
        if unit == "rad":
            pass
        elif unit == "deg":
            t = t * math.pi / 180
        else:
            raise ValueError('Invalid unit value passed')
        self._data = np.matrix([[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]])

    def __mul__(self, other):
        assert isinstance(other, SO2)
        return SO2(self._data * other._data)

    def __add__(self, other):
        assert isinstance(other, SO2)
        return self._data + other._data

    def data(self):
        return self._data

    def do_something_sub_class_specific(self):
        self._data = np.eye(4, 4)
