import unittest
from math import pi
from .. import transforms
import numpy as np


class TestRotx(unittest.TestCase):
    angle_rad = 0
    angle_deg = 0
    unit_rad = 'rad'
    unit_deg = 'deg'

    def setUp(self):
        self.angle_rad = pi

    def test_returns_npmatrix(self):
        self.assertTrue(isinstance(transforms.rotx(self.angle_rad), np.matrix))


if __name__ == "__main__":
    unittest.main()
