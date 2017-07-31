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
        self.assertEqual(obj1.length, obj2.length)

    def test_pose_so3_constructor_so3_object_data(self):
        obj1 = pose.SO3()  # TODO
        obj2 = pose.SO3(obj1)
        for i in range(obj2.length):
            if not np.array_equal(obj1.data[i], obj2.data[i]):
                output_str = matrix_mismatch_string_builder(obj2.data[i], obj1.data[i])
                self.fail(output_str)

    def test_pose_so3_constructor_so3_list(self):
        self.fail("Yet to be implemented")

    def test_pose_so3_constructor_rot_matrix(self):
        rot = tr.rotx(uniform(0, 360), 'deg')
        obj = pose.SO3(rot)
        if not matrices_equal(rot, obj.data[0]):
            output_str = matrix_mismatch_string_builder(obj.data[0], rot)
            self.fail(output_str)

    def test_pose_so3_constructor_rot_matrix_list(self):
        rot_list = []
        for i in range(5):
            rot_list.append(tr.rotx(uniform(0, 360), unit='deg'))
        obj = pose.SO3(rot_list)
        for i in range(obj.length):
            if not matrices_equal(obj.data[i], rot_list[i]):
                output_str = matrix_mismatch_string_builder(obj.data[i], rot_list[i])
                self.fail(output_str)

    def test_pose_so3_constructor_se3_length(self):
        objse3 = pose.SE3()
        objso3 = pose.SO3(objse3)
        self.assertEqual(objse3.length, objso3.length)

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

    def test_pose_so3_constructor_se3_list(self):
        self.fail("Not yet implemented")

    def test_pose_so3_constructor_rx(self):
        theta = uniform(0, 360)
        rotx = tr.rotx(theta, unit='deg')
        obj = pose.SO3.Rx(theta, unit='deg')
        if not matrices_equal(obj.data[0], rotx):
            output_str = matrix_mismatch_string_builder(obj.data[0], rotx)
            self.fail(output_str)

    def test_pose_so3_constructor_ry(self):
        theta = uniform(0, 360)
        roty = tr.roty(theta, unit='deg')
        obj = pose.SO3.Ry(theta, unit='deg')
        if not matrices_equal(obj.data[0], roty):
            output_str = matrix_mismatch_string_builder(obj.data[0], roty)
            self.fail(output_str)

    def test_pose_so3_constructor_rz(self):
        theta = uniform(0, 360)
        rotz = tr.rotz(theta, unit='deg')
        obj = pose.SO3.Rz(theta, unit='deg')
        if not matrices_equal(obj.data[0], rotz):
            output_str = matrix_mismatch_string_builder(obj.data[0], rotz)
            self.fail(output_str)

    def test_pose_so3_constructor_rand(self):
        self.fail("Not implemented yet")

    def test_pose_so3_constructor_eul(self):
        self.fail("Not implemented yet")

    def test_pose_so3_constructor_oa(self):
        self.fail("Not implemented yet")

    def test_pose_so3_constructor_rpy(self):
        self.fail("Not implemented yet")

    def test_pose_so3_constructor_angvec(self):
        self.fail("Not implemented yet")

    def test_pose_so3_property_zero(self):
        self.fail("Not implemented yet")

    def test_pose_so3_property_isSE(self):
        self.fail("Not implemented yet")

    def test_pose_so3_property_isSym(self):
        self.fail("Not implemented yet")

    def test_pose_so3_det(self):
        self.fail("Not implemented yet")

    def test_pose_so3_eig(self):
        self.fail("Not implemented yet")

    def test_pose_so3_log(self):
        self.fail("Not implemented yet")

    def test_pose_so3_inv(self):
        self.fail("Not implemented yet")

    def test_pose_so3_interp(self):
        self.fail("Not implemented yet")

    def test_pose_so3_simplify(self):
        self.fail("Not implemented yet")

    def test_pose_so3_static_check(self):  # TODO Check is necessary
        self.fail("Not implemented yet")

    def test_pose_so3_static_rx(self):
        self.fail("Not implemented yet")

    def test_pose_so3_static_ry(self):
        self.fail("Not implemented yet")

    def test_pose_so3_static_rz(self):
        self.fail("Not implemented yet")

    def test_pose_so3_static_rpy(self):
        self.fail("Not implemented yet")

if __name__ == '__main__':
    unittest.main()
