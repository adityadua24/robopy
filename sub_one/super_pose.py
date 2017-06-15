import numpy as np
import math
import sub_one.test_args as test_args
from abc import ABC, abstractmethod


class SuperPose(ABC):
    @property
    @abstractmethod
    def data(self):
        raise NotImplementedError()

    def __repr__(self):
        if len(self._list) >= 1:
            str = '-------------------------------\n'
            for each in self._list:
                array = np.asarray(each)
                str = str + np.array2string(array) \
                      + '\n-------------------------------\n'
            return str
        else:
            return 'No matrix found'

    @property
    def length(self):
        return len(self._list)

    def append(self, item):
        test_args.super_pose_appenditem(self, item)
        if type(item) is np.matrix:
            self._list.append(item)
        else:
            for each_matrix in item:
                self._list.append(each_matrix)

    def __mul__(self, other):
        test_args.super_pose_multiply_check(self, other)
        new_pose = type(self)([])
        for i in range(self.length):
            mat = self[i] * other[i]
            new_pose.append(mat)
        return new_pose
