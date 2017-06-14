import unittest
from math import pi
from sub_one import transforms
import numpy as np
import numpy.testing as npt


class TestRotx(unittest.TestCase):

    def test_validData_returnData_datatype(self):
        self.assertIsInstance(transforms.rotx(0), np.matrix)

    def test_validData_returnData_dimension(self):
        dimensions = transforms.rotx(0).shape
        self.assertEqual(dimensions, (3, 3))

    def test_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(0)
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_pi_by2_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(pi / 2)
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_pi_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
        received_mat = transforms.rotx(pi)
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_three_pi_by2_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        received_mat = transforms.rotx(3 * pi / 2)
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_2pi_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(2 * pi)
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_0_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(0, unit='deg')
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_360_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(360, unit='deg')
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_90_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(90, unit='deg')
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_180_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
        received_mat = transforms.rotx(180, unit='deg')
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_270_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        received_mat = transforms.rotx(270, unit='deg')
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_validData_boundaryCondition_450_deg(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        received_mat = transforms.rotx(450, unit='deg')
        caught = False
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            caught = True
        if caught:
            output_str = TestRotx.failedtest_string_builder(expected_mat, received_mat)
            self.fail(output_str)

    def test_invalidData_arg1_string(self):
        self.assertRaises(TypeError, transforms.rotx, 'invalid', unit='deg')

    def test_invalidData_arg2_string_mismatch(self):
        self.assertRaises(ValueError, transforms.rotx, 180, unit='invalid unit')

    def test_invalidData_arg2_bool(self):
        self.assertRaises(ValueError, transforms.rotx, 180, unit=True)

    def test_invalidData_arg2_int(self):
        self.assertRaises(ValueError, transforms.rotx, 180, unit=5)

    @staticmethod
    def failedtest_string_builder(exp_mat, rec_mat):
        expected_mat_str = np.array2string(np.asarray(exp_mat))
        received_mat_str = np.array2string(np.asarray(rec_mat))
        output_str = str("\n----------------------\n"
                         + "    Expected Output    "
                         + "\n----------------------\n"
                         + expected_mat_str
                         + "\n----------------------\n"
                         + "    Received Output    "
                         + "\n----------------------\n"
                         + received_mat_str)
        return output_str


if __name__ == "__main__":
    unittest.main()
