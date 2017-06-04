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
        # self.assertAlmostEqual(expected_mat, transforms.rotx(0))
        npt.assert_almost_equal(expected_mat, transforms.rotx(0))

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
        self.assertTrue(True)

    def test_invalidData_arg2_string_mismatch(self):
        self.assertTrue(True)

    def test_invalidData_arg2_bool(self):
        self.assertTrue(True)

    def test_invalidData_arg2_int(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
