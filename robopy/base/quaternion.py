# Author: Aditya Dua
# 28 January, 2018
import numpy as np
from .common import isvec
from math import sqrt
from numpy import trace


class Quaternion:
    def __init__(self, s=None, v=None):
        """
        A quaternion is a compact method of representing a 3D rotation that has
        computational advantages including speed and numerical robustness.
        A quaternion has 2 parts, a scalar s, and a vector v and is typically written::
        q = s <vx vy vz>
        A unit quaternion is one for which M{s^2+vx^2+vy^2+vz^2 = 1}.
        A quaternion can be considered as a rotation about a vector in space where
        q = cos (theta/2) sin(theta/2) <vx vy vz>
        where <vx vy vz> is a unit vector.
        :param s: scalar
        :param v: vector
        """
        if v is None:
            self.v = np.matrix([[0, 0, 0]])
        else:
            assert isvec(v, 3)
            self.v = v
        if s is None:
            self.s = 0
        else:
            assert type(s) is float or type(s) is float
            self.s = s

    @classmethod
    def qt(cls, arg_in):
        assert type(arg_in) is Quaternion
        return cls(s=arg_in.s, v=arg_in.v)

    def conj(self):
        return Quaternion(s=self.s, v=-self.v)

    def inv(self):
        return 0

    def tr2q(self, t):
        """
        Converts a homogeneous rotation matrix to a Quaternion object
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        :param t: homogeneous matrix
        :return: quaternion object
        """
        qs = sqrt(trace(t) + 1) / 2.0
        kx = t[2, 1] - t[1, 2]  # Oz - Ay
        ky = t[0, 2] - t[2, 0]  # Ax - Nz
        kz = t[1, 0] - t[0, 1]  # Ny - Ox

        if (t[0, 0] >= t[1, 1]) and (t[0, 0] >= t[2, 2]):
            kx1 = t[0, 0] - t[1, 1] - t[2, 2] + 1  # Nx - Oy - Az + 1
            ky1 = t[1, 0] + t[0, 1]  # Ny + Ox
            kz1 = t[2, 0] + t[0, 2]  # Nz + Ax
            add = (kx >= 0)
        elif t[1, 1] >= t[2, 2]:
            kx1 = t[1, 0] + t[0, 1]  # Ny + Ox
            ky1 = t[1, 1] - t[0, 0] - t[2, 2] + 1  # Oy - Nx - Az + 1
            kz1 = t[2, 1] + t[1, 2]  # Oz + Ay
            add = (ky >= 0)
        else:
            kx1 = t[2, 0] + t[0, 2]  # Nz + Ax
            ky1 = t[2, 1] + t[1, 2]  # Oz + Ay
            kz1 = t[2, 2] - t[0, 0] - t[1, 1] + 1  # Az - Nx - Oy + 1
            add = (kz >= 0)

        if add:
            kx = kx + kx1
            ky = ky + ky1
            kz = kz + kz1
        else:
            kx = kx - kx1
            ky = ky - ky1
            kz = kz - kz1

        kv = np.matrix([[kx, ky, kz]])
        nm = np.linalg.norm(kv)
        if nm == 0:
            self.s = 1.0
            self.v = np.matrix([[0.0, 0.0, 0.0]])

        else:
            self.s = qs
            self.v = (sqrt(1 - qs ** 2) / nm) * kv

    def __mul__(self, other):
        assert isinstance(other, Quaternion), "Both objects should be of type: Quaternion"
        return 0

    def __add__(self, other):
        assert isinstance(other, Quaternion), "Both objects should be of type: Quaternion"
        return Quaternion(s=self.s+other.s, v=self.v+other.v)

    def __sub__(self, other):
        assert isinstance(other, Quaternion), "Both objects should be of type: Quaternion"
        return Quaternion(s=self.s-other.s, v=self.v-other.v)

    def __repr__(self):
        return "%f <%f, %f, %f>" % (self.s, self.v[0, 0], self.v[0, 1], self.v[0, 2])
