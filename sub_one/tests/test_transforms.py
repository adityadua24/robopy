# Created by: Aditya Dua
# 10 June, 2017

import unittest
from math import pi
from .. import transforms
import numpy as np
from .test_common import matrix_mismatch_string_builder
from .test_common import matrices_equal


class TestRotx(unittest.TestCase):

    def test_transforms_rotx_validData_returnDatatype(self):
        self.assertIsInstance(transforms.rotx(0), np.matrix)

    def test_transforms_rotx_validData_returnData_dimension(self):
        dimensions = transforms.rotx(0).shape
        self.assertEqual(dimensions, (3, 3))

    def test_transforms_rotx_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(0)

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(pi / 2)

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
        received_mat = transforms.rotx(pi)

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        received_mat = transforms.rotx(3 * pi / 2)

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(2 * pi)

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(0, unit='deg')

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(360, unit='deg')

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(90, unit='deg')

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
        received_mat = transforms.rotx(180, unit='deg')

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        received_mat = transforms.rotx(270, unit='deg')

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(450, unit='deg')

        if not matrices_equal(received_mat, expected_mat):
            output_str = matrix_mismatch_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_transforms_rotx_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.rotx, 'invalid', unit='deg')

    def test_transforms_rotx_invalidData_arg2_string_mismatch(self):
        self.assertRaises(AssertionError, transforms.rotx, 180, unit='invalid unit')

    def test_transforms_rotx_invalidData_arg2_bool(self):
        self.assertRaises(AssertionError, transforms.rotx, 180, unit=True)

    def test_transforms_rotx_invalidData_arg2_int(self):
        self.assertRaises(AssertionError, transforms.rotx, 180, unit=5)


if __name__ == "__main__":
    unittest.main()
