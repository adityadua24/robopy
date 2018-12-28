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

if __name__ == '__main__':
    unittest.main()