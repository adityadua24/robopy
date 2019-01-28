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
from random import uniform, randint

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

    def test_quaternion_conj(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q1 = Quaternion(s, v)
        q2 = q1.conj()
        self.assertEqual(s, q2.s)
        if not matrices_equal(-v, q2.v):
            output_str = matrix_mismatch_string_builder(
                q2.v, -v)
            self.fail(output_str)

    def test_quaternion_inv(self):
        vec = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        s = float(vec[0, 0])
        v = vec[0, 1:]
        q1 = Quaternion(s, v)
        q2 = q1.inv()
        exp_vec = vec / np.sum(np.multiply(vec, vec))
        np.testing.assert_almost_equal(exp_vec[0, 0], q2.s)
        if not matrices_equal(-exp_vec[0, 1:], q2.v):
            output_str = matrix_mismatch_string_builder(
                -exp_vec[0, 1:], q2.v)
            self.fail(output_str)

    def test_quaternion_double(self):
        exp_vec = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q = Quaternion(float(exp_vec[0, 0]), exp_vec[0, 1:])
        rec_vec = q.double()
        if not matrices_equal(rec_vec, exp_vec):
            output_str = matrix_mismatch_string_builder(
                rec_vec, exp_vec)
            self.fail(output_str)

    def test_quaternion_add_zero(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion()
        q3 = q1 + q2
        self.assertEqual(vec1[0, 0], q3.s)
        if not matrices_equal(q3.v, vec1[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q3.v, vec1[0, 1:])
            self.fail(output_str)

    def test_quaternion_add_random(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        vec2 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        exp_sum = vec1 + vec2
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion(float(vec2[0, 0]), vec2[0, 1:])
        q3 = q1 + q2
        self.assertEqual(exp_sum[0, 0], q3.s)
        if not matrices_equal(q3.v, exp_sum[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q3.v, exp_sum[0, 1:])
            self.fail(output_str)

    def test_quaternion_in_place_add_zero(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion()
        q1 += q2
        self.assertEqual(vec1[0, 0], q1.s)
        if not matrices_equal(q1.v, vec1[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q1.v, vec1[0, 1:])
            self.fail(output_str)

    def test_quaternion_in_place_add_random(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        vec2 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        exp_sum = vec1 + vec2
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion(float(vec2[0, 0]), vec2[0, 1:])
        q1 += q2
        self.assertEqual(exp_sum[0, 0], q1.s)
        if not matrices_equal(q1.v, exp_sum[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q1.v, exp_sum[0, 1:])
            self.fail(output_str)

    def test_quaternion_subtract_zero(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion()
        q3 = q1 - q2
        self.assertEqual(vec1[0, 0], q3.s)
        if not matrices_equal(q3.v, vec1[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q3.v, vec1[0, 1:])
            self.fail(output_str)

    def test_quaternion_subtract_random(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        vec2 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        exp_sum = vec1 - vec2
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion(float(vec2[0, 0]), vec2[0, 1:])
        q3 = q1 - q2
        self.assertEqual(exp_sum[0, 0], q3.s)
        if not matrices_equal(q3.v, exp_sum[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q3.v, exp_sum[0, 1:])
            self.fail(output_str)

    def test_quaternion_in_place_subtract_zero(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion()
        q1 -= q2
        self.assertEqual(vec1[0, 0], q1.s)
        if not matrices_equal(q1.v, vec1[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q1.v, vec1[0, 1:])
            self.fail(output_str)

    def test_quaternion_in_place_subtract_random(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        vec2 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        exp_sum = vec1 - vec2
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion(float(vec2[0, 0]), vec2[0, 1:])
        q1 -= q2
        self.assertEqual(exp_sum[0, 0], q1.s)
        if not matrices_equal(q1.v, exp_sum[0, 1:]):
            output_str = matrix_mismatch_string_builder(
                q1.v, exp_sum[0, 1:])
            self.fail(output_str)

    def test_quaternion_multiplication_by_zero_quaternion(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = Quaternion()
        q3 = q1 * q2
        self.assertEqual(q3.s, 0)
        exp_vec = np.matrix([[0, 0, 0]])
        if not matrices_equal(q3.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q3.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_multiplication_by_random_quaternion(self):
        s1 = uniform(-1, 1)
        v1 = np.matrix([[uniform(-1, 1) for _ in range(3)]])
        s2 = uniform(-1, 1)
        v2 = np.matrix([[uniform(-1, 1) for _ in range(3)]])
        q1 = Quaternion(s1, v1)
        q2 = Quaternion(s2, v2)
        q3 = q1 * q2
        exp_s = float(s1 * s2 - v1 * v2.T)
        exp_v = s1 * v2 + s2 * v1 + np.cross(v1, v2)
        self.assertEqual(q3.s, exp_s)
        if not matrices_equal(q3.v, exp_v):
            output_str = matrix_mismatch_string_builder(
                q3.v, exp_v)
            self.fail(output_str)

    def test_quaternion_multiplication_by_zero(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q2 = q1 * 0
        self.assertEqual(q2.s, 0)
        exp_vec = np.matrix([[0, 0, 0]])
        if not matrices_equal(q2.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q2.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_multiplication_by_random_int(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        num = randint(-100, 100)
        q1 = Quaternion(s, v)
        q2 = q1 * num
        exp_s = num * s
        exp_v = num * v
        self.assertEqual(q2.s, exp_s)
        if not matrices_equal(q2.v, exp_v):
            output_str = matrix_mismatch_string_builder(
                q2.v, exp_v)
            self.fail(output_str)

    def test_quaternion_multiplication_by_random_float(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        num = uniform(-100, 100)
        q1 = Quaternion(s, v)
        q2 = q1 * num
        exp_s = num * s
        exp_v = num * v
        self.assertEqual(q2.s, exp_s)
        if not matrices_equal(q2.v, exp_v):
            output_str = matrix_mismatch_string_builder(
                q2.v, exp_v)
            self.fail(output_str)

    def test_quaternion_in_place_multiplication_by_zero(self):
        vec1 = np.matrix([[uniform(-1, 1) for _ in range(4)]])
        q1 = Quaternion(float(vec1[0, 0]), vec1[0, 1:])
        q1 *= 0
        self.assertEqual(q1.s, 0)
        exp_vec = np.matrix([[0, 0, 0]])
        if not matrices_equal(q1.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q1.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_in_place_multiplication_by_random_int(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        num = randint(-100, 100)
        q1 = Quaternion(s, v)
        q1 *= num
        exp_s = s * num
        exp_v = v * num
        self.assertEqual(q1.s, exp_s)
        if not matrices_equal(q1.v, exp_v):
            output_str = matrix_mismatch_string_builder(
                q1.v, exp_v)
            self.fail(output_str)

    def test_quaternion_in_place_multiplication_by_random_float(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        num = uniform(-100, 100)
        q1 = Quaternion(s, v)
        q1 *= num
        exp_s = num * s
        exp_v = num * v
        self.assertEqual(q1.s, exp_s)
        if not matrices_equal(q1.v, exp_v):
            output_str = matrix_mismatch_string_builder(
                q1.v, exp_v)
            self.fail(output_str)

    def test_quaternion_unit(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q1 = Quaternion(s, v)
        q2 = q1.unit()
        np.testing.assert_almost_equal(q2.norm(), 1)

    def test_quaternion_division_by_itself(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q1 = Quaternion(s, v)
        q2 = q1 / q1
        np.testing.assert_almost_equal(q2.s, 1.0)
        exp_vec = np.matrix([[0, 0, 0]])
        if not matrices_equal(q2.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q2.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_division_by_unit_quaternion(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q1 = Quaternion(s, v)
        q2 = Quaternion(1)
        q3 = q1 / q2
        self.assertEqual(q1.s, q3.s)
        if not matrices_equal(q1.v, q3.v):
            output_str = matrix_mismatch_string_builder(
                q1.v, q3.v)
            self.fail(output_str)

    def test_quaternion_pow_zero(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q1 = Quaternion(s, v)
        q2 = q1**0
        self.assertEqual(q2.s, 1)
        exp_vec = np.matrix([[0, 0, 0]])
        if not matrices_equal(q2.v, exp_vec):
            output_str = matrix_mismatch_string_builder(
                q2.v, exp_vec)
            self.fail(output_str)

    def test_quaternion_pow_one(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q1 = Quaternion(s, v)
        q2 = q1**1
        self.assertEqual(q2.s, s)
        if not matrices_equal(q2.v, v):
            output_str = matrix_mismatch_string_builder(
                q2.v, v)
            self.fail(output_str)

    def test_quaternion_pow_negative_one(self):
        s = uniform(-1, 1)
        v = np.matrix([[uniform(-50, 50) for _ in range(3)]])
        q1 = Quaternion(s, v)
        q2 = q1**-1
        q3 = q1.inv();
        self.assertEqual(q2.s, q3.s)
        if not matrices_equal(q2.v, q3.v):
            output_str = matrix_mismatch_string_builder(
                q2.v, q3.v)
            self.fail(output_str)

class TestUnitQuaternion(unittest.TestCase):
    def test_unit_quaternion_constructor(self):
        pass


if __name__ == '__main__':
    unittest.main()