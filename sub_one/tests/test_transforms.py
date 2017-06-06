import unittest
from math import pi
from .. import transforms
import numpy as np
import numpy.testing as npt


class TestRotx(unittest.TestCase):
    angle_rad = 0
    angle_deg = 0
    unit_rad = 'rad'
    unit_deg = 'deg'

    def setUp(self):
        self.angle_rad = pi

    def test_validData_returnData_datatype(self):
        self.assertIsInstance(transforms.rotx(self.angle_rad), np.matrix)

    def test_validData_returnData_dimension(self):
        dimensions = transforms.rotx(self.angle_rad).shape
        self.assertEqual(dimensions, (3, 3))

    def test_validData_boundaryCondition_0_rad(self):
        expected_mat = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        received_mat = transforms.rotx(0)
        caught = False
        expected_mat_str = ""
        received_mat_str = ""
        output_str = ""
        try:
            npt.assert_almost_equal(received_mat, expected_mat)
        except AssertionError:
            expected_mat_str = np.array2string(np.asarray(expected_mat))
            received_mat_str = np.array2string(np.asarray(received_mat))
            output_str = str("Expected Output:-\n" + expected_mat_str + "\n" + "Received Output:\n" + received_mat_str)
            caught = True
        if caught:
            self.fail(output_str)

    def test_validData_boundaryCondition_2pi_rad(self):
        self.assertTrue(True)

    def test_validData_boundaryCondition_2pi_multiple_rad(self):
        self.assertTrue(True)

    def test_validData_boundaryCondition_0_deg(self):
        self.assertTrue(True)

    def test_validData_boundaryCondition_360_deg(self):
        self.assertTrue(True)

    def test_validData_boundaryCondition_360_multiple_deg(self):
        self.assertTrue(True)

    def test_invalidData_arg1_string(self):
        self.assertTrue(True)

    def test_invalidData_arg1_bool(self):
        # self.assertRaises(AssertionError, npt.assert_almost_equal, received_mat, expected_mat)
        self.assertTrue(True)

    def test_invalidData_arg2_string_mismatch(self):
        self.assertTrue(True)

    def test_invalidData_arg2_bool(self):
        self.assertTrue(True)

    def test_invalidData_arg2_int(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
