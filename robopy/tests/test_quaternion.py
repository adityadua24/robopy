# Created by: Daniel Ingram
# 28 December, 2018
"""
Test module for quaternions: Quaternion and UnitQuaternion
"""
import unittest
import numpy as np
from ..base.quaternion import Quaternion, UnitQuaternion
from .test_common import matrix_mismatch_string_builder
from .test_common import matrices_equal
from .. import transforms as tr
from random import uniform

class TestQuaternion(unittest.TestCase):
    def test_quaternion_constructor_no_args(self):
        q = Quaternion()
        exp_vec = np.mat([[0, 0, 0]])
        exp_sca = 0
        self.assertEqual(q.s, exp_sca)
        if not matrices_equal(q.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_constructor_with_scalar(self):
        exp_sca = uniform(-1, 1)
        q = Quaternion(exp_sca)
        self.assertEqual(q.s, exp_sca)

    def test_quaternion_constructor_with_vector(self):
        exp_vec = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q = Quaternion(v=exp_vec)
        if not matrices_equal(q.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_constructor_with_scalar_and_vector(self):
        exp_sca = uniform(-1, 1)
        exp_vec = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q = Quaternion(exp_sca, exp_vec)
        self.assertEqual(q.s, exp_sca)
        if not matrices_equal(q.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_qt_constructor(self):
        q1 = Quaternion()
        q2 = Quaternion.qt(q1)
        self.assertEqual(q1.s, q2.s)
        if not matrices_equal(q1.v, q2.v):
            output_str = matrix_mismatch_string_builder(
                q1.v, q2.v)
            self.fail(output_str)

    def test_quaternion_pure_constructor(self):
        exp_vec = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q = Quaternion.pure(exp_vec)
        self.assertEqual(q.s, 0)
        if not matrices_equal(q.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_double(self):
        exp_vec = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q = Quaternion(float(exp_vec[0, 0]), exp_vec[0, 1:])
        rec_vec = q.double()
        if not matrices_equal(rec_vec, exp_vec):
            output_str = matrix_mismatch_string_builder(
                rec_vec, exp_vec)
            self.fail(output_str)


if __name__ == '__main__':
    unittest.main()