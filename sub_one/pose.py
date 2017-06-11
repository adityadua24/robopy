import numpy as np
from sub_one.super_pose import SuperPose
import math


class SO2(SuperPose):

    def __init__(self, t=None, unit='rad'):
        self._list = []
        if t is None:
            self._list.append(np.asmatrix(np.eye(2, 2)))
        elif isinstance(t, SO2):
            pass
        elif isinstance(t, np.matrix):
            self._data = t
        elif isinstance(t, list):
            if unit == "rad":
                pass
            elif unit == "deg":
                t_converted = []
                for each in t:
                    t_converted.append(each * math.pi / 180)
            else:
                raise ValueError('Invalid unit value passed')
            for each in t_converted:
                self._list.append(np.matrix([[math.cos(each), -math.sin(each)], [math.sin(each), math.cos(each)]]))
        else:
            pass
        # if unit == "rad":
        #     pass
        # elif unit == "deg":
        #     t = t * math.pi / 180
        # else:
        #     raise ValueError('Invalid unit value passed')
        # self._data = np.matrix([[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]])
        #self._list.append(np.matrix([[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]]))

    def __mul__(self, other):
        assert isinstance(other, SO2)
        return SO2(self._data * other._data)

    def __add__(self, other):
        assert isinstance(other, SO2)
        return self._data + other._data

    @property
    def data(self):
        return self._data

    def do_something_sub_class_specific(self):
        self._data = np.eye(4, 4)

    def __getitem__(self, item):
        return self._list[item]

    def __iter__(self):
        return (each for each in self._list)
