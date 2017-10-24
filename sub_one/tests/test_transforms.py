# Created by: Jack Button, Aditya Dua
# 10 June, 2017

import unittest
import numpy as np
from math import pi
from .test_common import matrices_equal, matrix_mismatch_string_builder
from .. import transforms


# ---------------------------------------------------------------------------------------#
#                                    3D Transforms
# ---------------------------------------------------------------------------------------#
# angvec2r  | ready


# angvec2tr | ready


# rotx | complete
class TestRotx(unittest.TestCase):
    def test_transforms_3d_rotx_validData_returnDatatype(self):
        self.assertIsInstance(transforms.rotx(0), np.matrix)

    def test_transforms_3d_rotx_validData_returnData_dimension(self):
        dimensions = transforms.rotx(0).shape
        self.assertEqual(dimensions, (3, 3))

    def test_transforms_3d_rotx_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
        received_mat = transforms.rotx(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        received_mat = transforms.rotx(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
        received_mat = transforms.rotx(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        received_mat = transforms.rotx(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotx_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.rotx, 'invalid', unit='deg')

    def test_transforms_3d_rotx_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.rotx,
                          180, unit='invalid unit')

    def test_transforms_3d_rotx_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.rotx, 180, unit=True)

    def test_transforms_3d_rotx_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.rotx, 180, unit=5)


# roty | complete
class Testroty(unittest.TestCase):
    def test_transforms_3d_roty_validData_returnDatatype(self):
        self.assertIsInstance(transforms.roty(0), np.matrix)

    def test_transforms_3d_roty_validData_returnData_dimension(self):
        dimensions = transforms.roty(0).shape
        self.assertEqual(dimensions, (3, 3))

    def test_transforms_3d_roty_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.roty(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[0., 0., 1.], [0, 1, 0.], [-1, 0., 0.]])
        received_mat = transforms.roty(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[-1., 0., 0.], [0, 1, 0.], [-0, 0., -1.]])
        received_mat = transforms.roty(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[-0., 0., -1.], [0, 1, 0.], [1, 0., -0.]])
        received_mat = transforms.roty(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.roty(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.roty(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.roty(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[0., 0., 1.], [0, 1, 0.], [-1, 0., 0.]])
        received_mat = transforms.roty(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[-1., 0., 0.], [0., 1., 0.], [-0., 0., -1.]])
        received_mat = transforms.roty(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[-0., 0., -1.], [0, 1, 0.], [1, 0., -0.]])
        received_mat = transforms.roty(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[0., 0., 1.], [0, 1, 0.], [-1, 0., 0.]])
        received_mat = transforms.roty(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_roty_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.roty, 'invalid', unit='deg')

    def test_transforms_3d_roty_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.roty,
                          180, unit='invalid unit')

    def test_transforms_3d_roty_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.roty, 180, unit=True)

    def test_transforms_3d_roty_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.roty, 180, unit=5)


# rotz | complete
class Testrotz(unittest.TestCase):
    def test_transforms_3d_rotz_validData_returnDatatype(self):
        self.assertIsInstance(transforms.rotz(0), np.matrix)

    def test_transforms_3d_rotz_validData_returnData_dimension(self):
        dimensions = transforms.rotz(0).shape
        self.assertEqual(dimensions, (3, 3))

    def test_transforms_3d_rotz_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotz(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[0., -1., 0.], [1, 0, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[-1., -0., 0.], [0, -1, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[-0., 1., 0.], [-1, -0, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1., 0., 0.], [-0, 1, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotz(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotz(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[0., -1., 0.], [1, 0, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[-1., -0., 0.], [0, -1, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[-0., 1., 0.], [-1, -0, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[0., -1., 0.], [1, 0, 0.], [0, 0., 1.]])
        received_mat = transforms.rotz(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_rotz_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.rotz, 'invalid', unit='deg')

    def test_transforms_3d_rotz_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.rotz,
                          180, unit='invalid unit')

    def test_transforms_3d_rotz_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.rotz, 180, unit=True)

    def test_transforms_3d_rotz_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.rotz, 180, unit=5)


# trotx |  complete
class Testtrotx(unittest.TestCase):
    def test_transforms_3d_trotx_validData_returnDatatype(self):
        self.assertIsInstance(transforms.trotx(0), np.matrix)

    def test_transforms_3d_trotx_validData_returnData_dimension(self):
        dimensions = transforms.trotx(0).shape
        self.assertEqual(dimensions, (4, 4))

    def test_transforms_3d_trotx_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 1., -0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 0., -1., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., -1., -0., 0.], [0., 0., -1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., -0., 1., 0.], [0., -1., -0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., -0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 1., -0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., -0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 0., -1., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., -1., -0., 0.], [0., 0., -1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., -0., 1., 0.], [0., -1., -0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 0., -1., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotx(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotx_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.trotx, 'invalid', unit='deg')

    def test_transforms_3d_trotx_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.trotx,
                          180, unit='invalid unit')

    def test_transforms_3d_trotx_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.trotx, 180, unit=True)

    def test_transforms_3d_trotx_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.trotx, 180, unit=5)


# troty |  complete
class Testtroty(unittest.TestCase):
    def test_transforms_3d_troty_validData_returnDatatype(self):
        self.assertIsInstance(transforms.troty(0), np.matrix)

    def test_transforms_3d_troty_validData_returnData_dimension(self):
        dimensions = transforms.troty(0).shape
        self.assertEqual(dimensions, (4, 4))

    def test_transforms_3d_troty_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 1., 0., 0.], [-0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[0., 0., 1., 0.], [0., 1., 0., 0.], [-1., 0., 0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[-1., 0., 0., 0.], [0., 1., 0., 0.], [-0., 0., -1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[-0., 0., -1., 0.], [0., 1., 0., 0.], [1., 0., -0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1., 0., -0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 1., 0., 0.], [-0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1., 0., -0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[0., 0., 1., 0.], [0., 1., 0., 0.], [-1., 0., 0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[-1., 0., 0., 0.], [0., 1., 0., 0.], [-0., 0., -1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[-0., 0., -1., 0.], [0., 1., 0., 0.], [1., 0., -0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[0., 0., 1., 0.], [0., 1., 0., 0.], [-1., 0., 0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.troty(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_troty_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.troty, 'invalid', unit='deg')

    def test_transforms_3d_troty_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.troty,
                          180, unit='invalid unit')

    def test_transforms_3d_troty_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.troty, 180, unit=True)

    def test_transforms_3d_troty_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.troty, 180, unit=5)


# trotz |  complete
class Testtrotz(unittest.TestCase):
    def test_transforms_3d_trotz_validData_returnDatatype(self):
        self.assertIsInstance(transforms.trotz(0), np.matrix)

    def test_transforms_3d_trotz_validData_returnData_dimension(self):
        dimensions = transforms.trotz(0).shape
        self.assertEqual(dimensions, (4, 4))

    def test_transforms_3d_trotz_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1., -0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[0., -1., 0., 0.], [1., 0., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[-1., -0., 0., 0.], [0., -1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[-0., 1., 0., 0.], [-1., -0., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [-0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1., -0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [-0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[0., -1., 0., 0.], [1., 0., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[-1., -0., 0., 0.], [0., -1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[-0., 1., 0., 0.], [-1., -0., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[0., -1., 0., 0.], [1., 0., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.trotz(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_3d_trotz_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.trotz, 'invalid', unit='deg')

    def test_transforms_3d_trotz_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.trotz,
                          180, unit='invalid unit')

    def test_transforms_3d_trotz_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.trotz, 180, unit=True)

    def test_transforms_3d_trotz_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.trotz, 180, unit=5)


# r2t
class TestR2t(unittest.TestCase):
    def test_transforms_r2t_validData_returnDatatype(self):  # pass
        self.assertIsInstance(transforms.r2t(transforms.rotx(0)), np.matrix)

    def test_transforms_r2t_validData_returnData_dimension(self):  # pass
        dimensions = transforms.r2t(transforms.rotx(0)).shape
        self.assertEqual(dimensions, (4, 4))

    def test_transforms_r2t_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 1., -0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.r2t(transforms.rotx(0))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_r2t_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[1., 0., 0., 0.], [0., 0., -1., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.]])
        received_mat = transforms.r2t(transforms.rotx(pi / 2))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)


# t2r
class TestT2r(unittest.TestCase):
    def test_transforms_t2r_validData_returnDatatype(self):  # pass
        self.assertIsInstance(transforms.t2r(transforms.trotx(0)), np.matrix)

    def test_transforms_t2r_validData_returnData_dimension(self):  # pass
        dimensions = transforms.t2r(transforms.trotx(0)).shape
        self.assertEqual(dimensions, (3, 3))

    def test_transforms_t2r_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, -0], [0, 0, 1]])
        received_mat = transforms.t2r(transforms.trotx(0))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_t2r_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0.]])
        received_mat = transforms.t2r(transforms.trotx(pi / 2))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)


# # rpy2r | ready
# class TestRpy2r(unittest.TestCase):
#     def test_transforms_rpy2r_validData_returnDatatype(self):  # pass
#         self.assertIsInstance(transforms.rpy2r([[11, 1, 1]]), np.matrix)


# oa2tr
class TestOa2tr(unittest.TestCase):
    def test_transforms_oa2tr_validData_returnDatatype(self):  # pass
        self.assertIsInstance(transforms.oa2tr([[1, 0, 1]], [[1, 1, 1]]), np.matrix)


# to test:

# tr2rt

# rt2tr

# trlog

# trexp

# ---------------------------------------------------------------------------------------#
#                                    2D Transforms
# ---------------------------------------------------------------------------------------#
# rot2
class Testrot2(unittest.TestCase):
    def test_transforms_2d_rot2_validData_returnDatatype(self):
        self.assertIsInstance(transforms.rot2(0), np.matrix)

    def test_transforms_2d_rot2_validData_returnData_dimension(self):
        dimensions = transforms.rot2(0).shape
        self.assertEqual(dimensions, (2, 2))

    def test_transforms_2d_rot2_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0], [0, 1]])
        received_mat = transforms.rot2(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[0, -1, ], [1, 0]])
        received_mat = transforms.rot2(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[-1, -0, ], [0, -1]])
        received_mat = transforms.rot2(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[-0, 1, ], [-1, -0]])
        received_mat = transforms.rot2(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1, 0, ], [-0, 1]])
        received_mat = transforms.rot2(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1, -0, ], [0, 1]])
        received_mat = transforms.rot2(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1, 0, ], [-0, 1]])
        received_mat = transforms.rot2(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[0, -1, ], [1, 0]])
        received_mat = transforms.rot2(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[-1, -0, ], [0, -1]])
        received_mat = transforms.rot2(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[-0, 1, ], [-1, -0]])
        received_mat = transforms.rot2(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[0, -1, ], [1, 0]])
        received_mat = transforms.rot2(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_rot2_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.rot2, 'invalid', unit='deg')

    def test_transforms_2d_rot2_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.rot2,
                          180, unit='invalid unit')

    def test_transforms_2d_rot2_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.rot2, 180, unit=True)

    def test_transforms_2d_rot2_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.rot2, 180, unit=5)


# trot2
class Testtrot2(unittest.TestCase):
    def test_transforms_2d_trot2_validData_returnDatatype(self):
        self.assertIsInstance(transforms.trot2(0), np.matrix)

    def test_transforms_2d_trot2_validData_returnData_dimension(self):
        dimensions = transforms.trot2(0).shape
        self.assertEqual(dimensions, (3, 3))

    def test_transforms_2d_trot2_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1., -0., 0.], [0., 1., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(0)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[-1., -0., 0.], [0., -1., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[-0., 1., 0.], [-1., -0., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1., 0., 0.], [-0., 1., 0.], [0, 0, 1]])
        received_mat = transforms.trot2(2 * pi)

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1., -0., 0.], [0., 1., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1., 0., 0.], [-0., 1., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[-1., -0., 0.], [0., -1., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[-0., 1., 0.], [-1., -0., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]])
        received_mat = transforms.trot2(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_2d_trot2_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.trot2, 'invalid', unit='deg')

    def test_transforms_2d_trot2_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.trot2,
                          180, unit='invalid unit')

    def test_transforms_2d_trot2_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.trot2, 180, unit=True)

    def test_transforms_2d_trot2_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.trot2, 180, unit=5)


# trexp2
class Testtrexp2(unittest.TestCase):
    def test_transforms_2d_trexp2_validData_returnDatatype(self):
        self.assertIsInstance(transforms.trexp2(transforms.rot2(10)), np.matrix)


# ---------------------------------------------------------------------------------------#
#                                 Differential Motion
# ---------------------------------------------------------------------------------------#
# skew
class TestSkew(unittest.TestCase):
    # Tests for if the vector is 1
    # Ensure matrix is returned
    def test_transforms_dif_skew_validData_returnDatatype(self):
        self.assertIsInstance(transforms.skew(np.matrix([1])), np.matrix)

    # Check Matrix Dimensions vectorsize=1
    def test_transforms_dif_skew_validData_returnData_dimension(self):
        dimensions = transforms.skew(np.matrix([1])).shape
        self.assertEqual(dimensions, (2, 2))

    # Tests for if the vector is 3

    # Ensure matrix is returned
    def test_transforms_dif_skew_validData_returnDatatype_v3(self):
        self.assertIsInstance(transforms.skew(np.matrix([1, 1, 1])), np.matrix)

    # Check Matrix Dimensions vectorsize=1
    def test_transforms_dif_skew_validData_returnData_dimension_v3(self):
        dimensions = transforms.skew(np.matrix([1, 1, 1])).shape
        self.assertEqual(dimensions, (3, 3))

    # boundary for vectore size of 1

    def test_transforms_dif_skew_validData_boundaryCondition_1(self):
        expected_mat = np.matrix([[0, -1], [1, 0]])
        received_mat = transforms.skew(np.matrix([1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skew_validData_boundaryCondition_2(self):
        expected_mat = np.matrix([[0, -2], [2, 0]])
        received_mat = transforms.skew(np.matrix([2]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skew_validData_boundaryCondition_3(self):
        expected_mat = np.matrix([[0, -3], [3, 0]])
        received_mat = transforms.skew(np.matrix([3]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skew_validData_boundaryCondition_4(self):
        expected_mat = np.matrix([[0, -4], [4, 0]])
        received_mat = transforms.skew(np.matrix([4]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skew_validData_boundaryCondition_5(self):
        expected_mat = np.matrix([[0, -5], [5, 0]])
        received_mat = transforms.skew(np.matrix([5]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    # boundary tests if 3 vector

    def test_transforms_dif_skew_validData_boundaryCondition_111(self):
        expected_mat = np.matrix([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
        received_mat = transforms.skew(np.matrix([1, 1, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skew_validData_boundaryCondition_101(self):
        expected_mat = np.matrix([[0, -1, 0], [1, 0, -1], [0, 1, 0]])
        received_mat = transforms.skew(np.matrix([1, 0, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skew_validData_boundaryCondition_100(self):
        expected_mat = np.matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.skew(np.matrix([1, 0, 0]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skew_validData_boundaryCondition_321(self):
        expected_mat = np.matrix([[0, -1, 2], [1, 0, -3], [-2, 3, 0]])
        received_mat = transforms.skew(np.matrix([3, 2, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)


# skewa
class TestSkewa(unittest.TestCase):
    # Tests for if the vector is 3x1
    # Ensure matrix is returned
    def test_transforms_dif_skewa_validData_returnDatatype(self):
        self.assertIsInstance(transforms.skewa(np.matrix([1, 1, 1])), np.matrix)

    # Check Matrix Dimensions vectorsize=3x1
    def test_transforms_dif_skewa_validData_returnData_dimension(self):
        dimensions = transforms.skewa(np.matrix([1, 1, 1])).shape
        self.assertEqual(dimensions, (3, 3))

    # Tests for if the vector is 6x1
    # Ensure matrix is returned
    def test_transforms_dif_skewa_validData_returnDatatype_v3(self):
        self.assertIsInstance(transforms.skewa(np.matrix([1, 1, 1, 1, 1, 1])), np.matrix)

    # Check Matrix Dimensions of 4x4 if v = 6x1
    def test_transforms_dif_skew_validData_returnData_dimension_v3(self):
        dimensions = transforms.skewa(np.matrix([1, 1, 1, 1, 1, 1])).shape
        self.assertEqual(dimensions, (4, 4))

    # boundary for vectore size of 1

    def test_transforms_dif_skewa_validData_boundaryCondition_1(self):
        expected_mat = np.matrix([[0, -1, 1], [1, 0, 1], [0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([1, 1, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skewa_validData_boundaryCondition_2(self):
        expected_mat = np.matrix([[0, -3, 1], [3, 0, 2], [0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([1, 2, 3]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    # def test_transforms_dif_skewa_validData_boundaryCondition_2_6x1(self):
    #     expected_mat = np.matrix([[1, 0], [0, 1]])
    #     received_mat = transforms.skewa(np.matrix([]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skewa_validData_boundaryCondition_2_4x4(self):
        expected_mat = np.matrix([[0, -1, 1, 1], [1, 0, -1, 0], [-1, 1, 0, 1], [0, 0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([1, 0, 1, 1, 1, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    # boundary tests if 3 vector

    def test_transforms_dif_skewa_validData_boundaryCondition_111(self):
        expected_mat = np.matrix([[0, -1, 1], [1, 0, 1], [0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([1, 1, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skewa_validData_boundaryCondition_101(self):
        expected_mat = np.matrix([[0, -1, 1], [1, 0, 0], [0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([1, 0, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skewa_validData_boundaryCondition_100(self):
        expected_mat = np.matrix([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([1, 0, 0]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skewa_validData_boundaryCondition_123(self):
        expected_mat = np.matrix([[0, -3, 1], [3, 0, 2], [0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([1, 2, 3]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_dif_skewa_validData_boundaryCondition_321(self):
        expected_mat = np.matrix([[0, -1, 3], [1, 0, 2], [0, 0, 0]])
        received_mat = transforms.skewa(np.matrix([3, 2, 1]))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)


# vex
class TestVex(unittest.TestCase):
    # test for 3x3 matrix
    def test_transforms_dif_vex_validData_returnDatatype1(self):
        self.assertIsInstance(transforms.vex(transforms.rotx(30)), np.matrix)

    # ensure returns 3x1 if matrix is 3x3
    def test_transforms_dif_vex_validData_returnData_dimension1(self):
        dimensions = transforms.vex(transforms.rotx(30)).shape
        self.assertEqual(dimensions, (3, 1))

    def test_transforms_dif_vex_validData_returnDatatype2(self):
        self.assertIsInstance(transforms.vex(transforms.rot2(0)), np.matrix)

    # ensure returns 1 if matrix is 2x2
    def test_transforms_dif_vex_validData_returnData_dimension2(self):
        dimensions = transforms.vex(transforms.rot2(30)).shape
        self.assertEqual(dimensions, (1, 1))

    def test_transforms_dif_vex_validData_boundaryCondition_rot_0(self):
        expected_mat = np.matrix([[0.], [0.], [0.]])
        received_mat = transforms.vex(transforms.roty(0))

        if not matrices_equal(received_mat, expected_mat, ):
            output_str = matrix_mismatch_string_builder(
                expected_mat, received_mat)
            self.fail(output_str)

    # # check whats going on herie
    # def test_transforms_dif_vex_validData_boundaryCondition_roty_30(self):
    #     expected_mat = np.matrix([[0.], [-0.98803162], [0.]])
    #     received_mat = transforms.vex(transforms.roty(30))
    #
    #     if not matrices_equal(received_mat, expected_mat, ):
    #         output_str = matrix_mismatch_string_builder(
    #             expected_mat, received_mat)
    #         self.fail(output_str)


# ---------------------------------------------------------------------------------------#
#                                      Utility
# ---------------------------------------------------------------------------------------#

# unit


if __name__ == "__main__":
    unittest.main()
