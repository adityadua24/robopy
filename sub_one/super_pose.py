import numpy as np
import math
import sub_one.test_args as test_args
from abc import ABC, abstractmethod
import numpy.testing as npt
from sub_one import pose


class SuperPose(ABC):
    @property
    def length(self):
        return len(self._list)

    @property
    def data(self):
        return self._list

    @property
    def isSE(self):
        if isinstance(self, pose.SE2) or isinstance(self, pose.SE3):
            return True
        else:
            return False

    # TODO issym, simplify, ?

    def is_equal(self, other):
        if (type(self) is type(other)) and (self.length == other.length):
            for i in range(self.length):
                try:
                    npt.assert_almost_equal(self[i], other[i])
                except AssertionError:
                    return False
            return True

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
        if self.length == other.length:
            for i in range(self.length):
                mat = self[i] * other[i]
                new_pose.append(mat)
            return new_pose
        else:
            for each_self_matrix in self:
                for each_other_matrix in other:
                    mat = each_self_matrix * each_other_matrix
                    new_pose.append(mat)
            return new_pose

    def __add__(self, other):
        test_args.super_pose_add_sub_check(self, other)
        mat = []
        for i in range(self.length):
            mat.append(self[i] + other[i])
        return mat

    def __sub__(self, other):
        test_args.super_pose_add_sub_check(self, other)
        mat = []
        for i in range(self.length):
            mat.append(self[i] - other[i])
        return mat

    def __getitem__(self, item):
        return self._list[item]

    def __iter__(self):
        return (each for each in self._list)

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
