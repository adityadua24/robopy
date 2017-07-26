# Created by: Aditya Dua
# 25 July, 2017
"""
Test module for poses: SO2, SE2, SO3 and SE3
"""
import unittest
import numpy as np
from .. import pose
from .common import matrix_mismatch_string_builder
from .common import matrices_equal
from .. import transforms as tr
from random import uniform


class TestSO3(unittest.TestCase):
    # TODO Validate tests on matrices other than identity as well!!

    def test_pose_so3_constructor_no_args(self):
        obj = pose.SO3()
        exp_mat = np.asmatrix(np.eye(3, 3))
        rec_mat = obj.data[0]
        if not matrices_equal(rec_mat, exp_mat):
            output_str = matrix_mismatch_string_builder(rec_mat, exp_mat)
            self.fail(output_str)

    def test_pose_so3_constructor_so3_object_length(self):
        obj1 = pose.SO3()  # TODO
        obj2 = pose.SO3(obj1)
        self.assertEquals(obj1.length, obj2.length)

    def test_pose_so3_constructor_so3_object_data(self):
        obj1 = pose.SO3()  # TODO
        obj2 = pose.SO3(obj1)
        for i in range(obj2.length):
            if not np.array_equal(obj1.data[i], obj2.data[i]):
                output_str = matrix_mismatch_string_builder(obj2.data[i], obj1.data[i])
                self.fail(output_str)

    def test_pose_so3_constructor_rot_matrix(self):
        rot = tr.rotx(uniform(0, 360), 'deg')
        obj = pose.SO3(rot)
        if not np.array_equal(rot, obj.data[0]):
            output_str = matrix_mismatch_string_builder(obj.data[0], rot)
            self.fail(output_str)

    def test_pose_so3_constructor_se3_length(self):
        objse3 = pose.SE3()
        objso3 = pose.SO3(objse3)
        self.assertEquals(objse3.length, objso3.length)

    def test_pose_so3_constructor_se3_data(self):
        objse3 = pose.SE3()
        objso3 = pose.SO3(objse3)
        rot_mats = []
        for each in objse3:
            rot_mats.append(tr.t2r(each))
        for i in range(objso3.length):
            if not np.array_equal(rot_mats[i], objso3.data[i]):
                output_str = matrix_mismatch_string_builder(objso3.data[i], rot_mats[i])
                self.fail(output_str)

    def test_pose_so3_constructor_rx(self):
        theta = uniform(0, 360)
        rotx = tr.rotx(theta, unit='deg')
        obj = pose.SO3(rx=theta, unit='deg')


if __name__ == '__main__':
    unittest.main()
