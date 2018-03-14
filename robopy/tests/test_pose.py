# Created by: Aditya Dua
# 25 July, 2017
"""
Test module for poses: SO2, SE2, SO3 and SE3
"""
import unittest
import numpy as np
from .. import pose
from .test_common import matrix_mismatch_string_builder
from .test_common import matrices_equal
from .. import transforms as tr
from random import uniform


class TestSE2(unittest.TestCase):
    def test_pose_se2_constructor_no_args(self):
        obj = pose.SE2()
        exp_mat = np.asmatrix(np.eye(3, 3))
        rec_mat = obj.data[0]
        if not matrices_equal(rec_mat, exp_mat, ):
            output_str = matrix_mismatch_string_builder(rec_mat, exp_mat)
            self.fail(output_str)


class TestSE3(unittest.TestCase):
    def test_pose_se3_constructor_no_args(self):
        obj = pose.SE3()
        exp_mat = np.asmatrix(np.eye(4, 4))
        rec_mat = obj.data[0]
        if not matrices_equal(rec_mat, exp_mat, ):
            output_str = matrix_mismatch_string_builder(rec_mat, exp_mat)
            self.fail(output_str)


class TestSO3(unittest.TestCase):
    # TODO Validate tests on matrices other than identity as well!!

    def test_pose_so3_constructor_no_args(self):
        obj = pose.SO3()
        exp_mat = np.asmatrix(np.eye(3, 3))
        rec_mat = obj.data[0]
        if not matrices_equal(rec_mat, exp_mat, ):
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
                output_str = matrix_mismatch_string_builder(
                    obj2.data[i], obj1.data[i])
                self.fail(output_str)

    def test_pose_so3_constructor_so3_list(self):
        self.fail("Yet to be implemented")

    def test_pose_so3_constructor_rot_matrix(self):
        rot = tr.rotx(uniform(0, 360), 'deg')
        obj = pose.SO3(rot)
        if not matrices_equal(rot, obj.data[0], ):
            output_str = matrix_mismatch_string_builder(obj.data[0], rot)
            self.fail(output_str)

    def test_pose_so3_constructor_rot_matrix_list(self):
        rot_list = []
        for i in range(5):
            rot_list.append(tr.rotx(uniform(0, 360), unit='deg'))
        obj = pose.SO3(rot_list)
        for i in range(obj.length):
            if not matrices_equal(obj.data[i], rot_list[i], ):
                output_str = matrix_mismatch_string_builder(
                    obj.data[i], rot_list[i])
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
                output_str = matrix_mismatch_string_builder(
                    objso3.data[i], rot_mats[i])
                self.fail(output_str)

    def test_pose_so3_constructor_se3_list(self):
        self.fail("Not yet implemented")

    def test_pose_so3_constructor_rx(self):
        theta = uniform(0, 360)
        rotx = tr.rotx(theta, unit='deg')
        obj = pose.SO3.Rx(theta, unit='deg')
        if not matrices_equal(obj.data[0], rotx, ):
            output_str = matrix_mismatch_string_builder(obj.data[0], rotx)
            self.fail(output_str)

    def test_pose_so3_constructor_rx_list(self):
        theta_list = [uniform(0, 360) for i in range(5)]  # list comprehensions
        rotx_list = [tr.rotx(theta, unit='deg') for theta in theta_list]
        obj = pose.SO3.Rx(theta_list, unit='deg')
        for i in range(obj.length):
            if not matrices_equal(obj.data[i], rotx_list[i], ):
                output_str = matrix_mismatch_string_builder(
                    obj.data[i], rotx_list[i])
                self.fail(output_str)

    def test_pose_so3_constructor_ry(self):
        theta = uniform(0, 360)
        roty = tr.roty(theta, unit='deg')
        obj = pose.SO3.Ry(theta, unit='deg')
        if not matrices_equal(obj.data[0], roty, ):
            output_str = matrix_mismatch_string_builder(obj.data[0], roty)
            self.fail(output_str)

    def test_pose_so3_constructor_ry_list(self):
        theta_list = [uniform(0, 360) for i in range(5)]  # list comprehensions
        roty_list = [tr.roty(theta, unit='deg') for theta in theta_list]
        obj = pose.SO3.Ry(theta_list, unit='deg')
        for i in range(obj.length):
            if not matrices_equal(obj.data[i], roty_list[i], ):
                output_str = matrix_mismatch_string_builder(
                    obj.data[i], roty_list[i])
                self.fail(output_str)

    def test_pose_so3_constructor_rz(self):
        theta = uniform(0, 360)
        rotz = tr.rotz(theta, unit='deg')
        obj = pose.SO3.Rz(theta, unit='deg')
        if not matrices_equal(obj.data[0], rotz, ):
            output_str = matrix_mismatch_string_builder(obj.data[0], rotz)
            self.fail(output_str)

    def test_pose_so3_constructor_rz_list(self):
        theta_list = [uniform(0, 360) for i in range(5)]  # list comprehensions
        rotz_list = [tr.rotz(theta, unit='deg') for theta in theta_list]
        obj = pose.SO3.Rz(theta_list, unit='deg')
        for i in range(obj.length):
            if not matrices_equal(obj.data[i], rotz_list[i], ):
                output_str = matrix_mismatch_string_builder(
                    obj.data[i], rotz_list[i])
                self.fail(output_str)

    def test_pose_so3_constructor_rand(self):
        obj1 = pose.SO3.rand()
        obj2 = pose.SO3.rand()
        if matrices_equal(obj1.data[0], obj2.data[0], ):
            self.fail("SO3.rand() show produces random poses.")

    def test_pose_so3_constructor_eul(self):
        # obj = pose.SO3.eul([uniform(0, 360), uniform(0, 360), uniform(0, 360)], unit='deg')
        self.fail("Test not defined")

    def test_pose_so3_constructor_oa(self):
        self.fail("Not implemented yet")

    def test_pose_so3_constructor_rpy(self):
        mat = np.matrix([[0.7259, 0.4803, 0.4924], [
            0.3536, 0.3536, -0.8660], [-0.5900, 0.8027, 0.0868]])
        obj = pose.SO3.rpy(thetas=[45, 60, 80], order='camera', unit='deg')
        if not matrices_equal(obj.data[0], mat, decimal=4):
            output_str = matrix_mismatch_string_builder(obj.data[0], mat)
            self.fail(output_str)

    def test_pose_so3_constructor_rpy_list(self):
        mat = [0, 0]
        mat[0] = np.matrix([[-0.2248, 0.3502, 0.9093],
                            [-0.7637, -0.6429, 0.0587], [0.6051, -0.6812, 0.4120]])
        mat[1] = np.matrix([[-0.1854, 0.2147, -0.9589],
                            [-0.9018, -0.4248, 0.0793], [-0.3904, 0.8794, 0.2724]])
        obj = pose.SO3.rpy([[1, 2, 3], [4, 5, 6]], order='arm')
        for i in range(obj.length):
            if not matrices_equal(obj.data[i], mat[i], decimal=4):
                output_str = matrix_mismatch_string_builder(
                    obj.data[i], mat[i])
                self.fail(output_str)

    def test_pose_so3_constructor_angvec(self):
        self.fail("Not implemented yet")

    def test_pose_so3_property_zero(self):
        self.fail("Not implemented yet")

    def test_pose_so3_property_isSE(self):
        obj = pose.SO3()
        if obj.isSE:
            self.fail("Is not a SE object.")

    def test_pose_so3_property_isSym(self):
        self.fail("Not implemented yet")

    def test_pose_so3_det(self):
        obj = pose.SO3.Rx(theta=80, unit='deg')
        det = obj.det()
        if det != 1:
            self.fail("Expected determinant value: 1.\n"
                      "Received determinant value: det")

    def test_pose_so3_rotation(self):
        obj = pose.SO3.Rx(theta=45, unit='deg')
        exp_rot = tr.rotx(theta=45, unit='deg')
        rec_rot = obj.rotation()
        if not matrices_equal(rec_rot, exp_rot):
            output_str = matrix_mismatch_string_builder(rec_rot, exp_rot)
            self.fail(output_str)

    def test_pose_so3_rotation_list(self):
        obj = pose.SO3.Rx(theta=[70, 80], unit='deg')
        rot = [0, 0]
        rot[0] = tr.rotx(theta=70, unit='deg')
        rot[1] = tr.rotx(theta=80, unit='deg')
        for i in range(obj.length):
            if not matrices_equal(obj.data[i], rot[i]):
                output_str = matrix_mismatch_string_builder(
                    obj.data[i], rot[i])
                self.fail(output_str)

    def test_pose_so3_tr_matrix(self):
        obj = pose.SO3.Rx(theta=45, unit='deg')
        mat = np.matrix([[1.0000, 0, 0, 0], [0, 0.7071, -0.7071, 0], [0, 0.7071, 0.7071, 0], [0, 0, 0, 1.0000]])
        if not matrices_equal(obj.t_matrix(), mat, decimal=4):
            output_str = matrix_mismatch_string_builder(obj.t_matrix(), mat)
            self.fail(output_str)

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
