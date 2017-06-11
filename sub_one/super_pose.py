import numpy as np
import math
import sub_one.pose as pose
import sub_one.test_args as test_args
from abc import ABC, abstractmethod


class SuperPose(ABC):

    @property
    @abstractmethod
    def data(self):
        raise NotImplementedError()

    def __repr__(self):
        str = '-------------------------------\n'
        for each in self._list:
            array = np.asarray(each)
            str = str + np.array2string(array) \
                  + '\n-------------------------------\n'
        return str

    def length(self):
        return len(self._list)

    def append(self, item):
        pass

    def __mul__(self, other):
        assert type(self) is type(other)
        assert test_args.valid_pose(self)
        assert test_args.valid_pose(other)
        newPose = type(self)()
        for each_self_pose in self:
            for each_other_pose in other:
                pass


