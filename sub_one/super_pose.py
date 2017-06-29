# Author - Aditya Dua - 13 June, 2017

import numpy as np
from . import test_args
from abc import ABC, abstractmethod
import numpy.testing as npt
from . import pose


class SuperPose(ABC):
    @property
    def length(self):
        return len(self.data)

    @property
    def data(self):
        return self._list

    @property
    def isSE(self):
        if isinstance(self, pose.SE2) or isinstance(self, pose.SE3):
            return True
        else:
            return False

    @property
    def shape(self):
        return self.data[0].shape

    # TODO issym, simplify, ?

    def is_equal(self, other):
        if (type(self) is type(other)) and (self.length == other.length):
            for i in range(self.length):
                try:
                    npt.assert_almost_equal(self.data[i], other.data[i])
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

    def tr_2_rt(self):
        assert isinstance(self, pose.SE2) or isinstance(self, pose.SE3)

    def t_2_r(self):
        assert isinstance(self, pose.SE2) or isinstance(self, pose.SE3)
        for each_matrix in self:
            pass  # TODO

    def __mul__(self, other):
        test_args.super_pose_multiply_check(self, other)
        if isinstance(other, SuperPose):
            new_pose = type(self)([])  # Creates empty poses with no data
            if self.length == other.length:
                for i in range(self.length):
                    mat = self.data[i] * other.data[i]
                    new_pose.append(mat)
                return new_pose
            else:
                for each_self_matrix in self:
                    for each_other_matrix in other:
                        mat = each_self_matrix * each_other_matrix
                        new_pose.append(mat)
            return new_pose
        elif isinstance(other, np.matrix):
            mat = []
            for each_matrix in self:
                mat.append(each_matrix * other)
            if len(mat) == 1:
                return mat[0]
            elif len(mat) > 1:
                return mat

    def __truediv__(self, other):
        test_args.super_pose_divide_check(self, other)
        new_pose = type(self)([])  # Creates empty poses with no data
        if self.length == other.length:
            for i in range(self.length):
                new_pose.append(self.data[i] * np.linalg.inv(other.data[i]))
        elif self.length == 1:
            for i in range(other.length):
                new_pose.append(np.linalg.inv(self.data[0]) * other.data[i])
        elif other.length == 1:
            for i in range(self.length):
                new_pose.append(self.data[i] * np.linalg.inv(other.data[0]))
        return new_pose

    def __add__(self, other):
        test_args.super_pose_add_sub_check(self, other)
        mat = []
        for i in range(self.length):
            mat.append(self.data[i] + other.data[i])
        if len(mat) == 1:
            return mat[0]
        elif len(mat) > 1:
            return mat

    def __sub__(self, other):
        test_args.super_pose_add_sub_check(self, other)
        mat = []
        for i in range(self.length):
            mat.append(self.data[i] - other.data[i])
        if len(mat) == 1:
            return mat[0]
        elif len(mat) > 1:
            return mat

    def __getitem__(self, item):
        new_pose = type(self)([])
        new_pose.append(self._list[item])
        return new_pose

    def __iter__(self):
        return (each for each in self._list)

    def __repr__(self):
        if len(self.data) >= 1:
            str = '-----------------------------------------\n'
            for each in self._list:
                array = np.asarray(each)
                str = str + np.array2string(array) \
                      + '\n-----------------------------------------\n'
            return str
        else:
            return 'No matrix found'
