# Author: Aditya Dua
# 28 January, 2018
import numpy as np
from .common import isvec
from .common import ishomog
from math import sqrt
from numpy import trace
from .pose import SO3
from .pose import SE3
from .transforms import *


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
            assert type(s) is float or type(s) is int
            self.s = s

    @classmethod
    def qt(cls, arg_in):
        assert type(arg_in) is Quaternion
        return cls(s=arg_in.s, v=arg_in.v)

    def conj(self):
        return Quaternion(s=self.s, v=-self.v)

    def inv(self):
        return Quaternion(s=self.s, v=-self.v)

    def tr(self):
        return t2r(self.r())

    def norm(self):
        """Return the norm of this quaternion.
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        @rtype: number
        @return: the norm
        """
        return np.linalg.norm(self.double())

    def double(self):
        """Return the quaternion as 4-element vector.
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        @rtype: 4-vector
        @return: the quaternion elements
        """
        return np.concatenate((np.matrix(self.s), self.v), 1)

    def unit(self):
        """Return an equivalent unit quaternion
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        @rtype: quaternion
        @return: equivalent unit quaternion
        """
        qr = UnitQuaternion()
        nm = self.norm()
        qr.s = float(self.s / nm)
        qr.v = self.v / nm
        return qr

    def r(self):
        """Return an equivalent rotation matrix.
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        @rtype: 3x3 orthonormal rotation matrix
        @return: equivalent rotation matrix
        """
        s = self.s
        x = self.v[0, 0]
        y = self.v[0, 1]
        z = self.v[0, 2]

        return np.matrix([[1 - 2 * (y ** 2 + z ** 2), 2 * (x * y - s * z), 2 * (x * z + s * y)],
                          [2 * (x * y + s * z), 1 - 2 * (x ** 2 + z ** 2), 2 * (y * z - s * x)],
                          [2 * (x * z - s * y), 2 * (y * z + s * x), 1 - 2 * (x ** 2 + y ** 2)]])

    def __mul__(self, other):
        assert isinstance(other, Quaternion) or isinstance(other, int) or isinstance(other,
                                                                                     float), "Can be multiplied with " \
                                                                                             "Quaternion, " \
                                                                                             "int or a float "
        qr = Quaternion()
        if isinstance(other, Quaternion):
            qr.s = self.s * other.s - self.v * np.transpose(other.v)
            qr.v = self.s * other.v + other.s * self.v + np.cross(self.v, other.v)
        elif type(other) is int or type(other) is float:
            qr.s = self.s * other
            qr.v = self.v * other
        elif isvec(other, 3):
            # TODO
            pass
        return qr

    def __pow__(self, power, modulo=None):
        """
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        :param power:
        :param modulo:
        :return:
        """
        assert type(power) is int, "Power must be an integer"
        qr = Quaternion()
        q = Quaternion.qt(self)
        for i in range(0, abs(power)):
            qr = qr * q

        if power < 0:
            qr = qr.inv()

        return qr

    def __imul__(self, other):
        """
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        :param other:
        :return: self
        """
        if isinstance(other, Quaternion):
            s1 = self.s
            v1 = self.v
            s2 = other.s
            v2 = other.v

            # form the product
            self.s = s1 * s2 - v1 * v2.T
            self.v = s1 * v2 + s2 * v1 + np.cross(v1, v2)

        elif type(other) is int or type(other) is float:
            self.s *= other
            self.v *= other

        return self

    def __add__(self, other):
        assert isinstance(other, Quaternion), "Both objects should be of type: Quaternion"
        return Quaternion(s=self.s + other.s, v=self.v + other.v)

    def __sub__(self, other):
        assert isinstance(other, Quaternion), "Both objects should be of type: Quaternion"
        return Quaternion(s=self.s - other.s, v=self.v - other.v)

    def __truediv__(self, other):
        assert isinstance(other, Quaternion) or isinstance(other, int) or isinstance(other,
                                                                                     float), "Can be divided by a " \
                                                                                             "Quaternion, " \
                                                                                             "int or a float "
        qr = Quaternion()
        if type(other) is Quaternion:
            qr = self * other.inv()
        elif type(other) is int or type(other) is float:
            qr.s = self.s / other
            qr.v = self.v / other
        return qr

    def __repr__(self):
        return "%f <%f, %f, %f>" % (self.s, self.v[0, 0], self.v[0, 1], self.v[0, 2])


class UnitQuaternion(Quaternion):
    def __init__(self, s=None, v=None):
        if s is None:
            s = 1
        if v is None:
            v = np.matrix([[0, 0, 0]])
        super().__init__(s, v)

    @classmethod
    def rot(cls, arg_in):
        qr = cls()
        qr.tr2q(arg_in)
        return qr

    @classmethod
    def qt(cls, arg_in):
        if type(arg_in) is Quaternion:
            arg_in = arg_in.unit()
            print(type(arg_in.s))
        else:
            assert type(arg_in) is UnitQuaternion
        return cls(arg_in.s, arg_in.v)

    @classmethod
    def eul(cls, arg_in, unit='rad'):
        assert isvec(arg_in, 3)
        return cls.rot(eul2r(phi=arg_in, unit=unit))

    @classmethod
    def rpy(cls, arg_in, unit='rad'):
        return cls.rot(rpy2r(thetas=arg_in, unit=unit))  # rpy2r returns a list of matrices

    @classmethod
    def angvec(cls):
        pass

    @classmethod
    def omega(cls):
        pass

    @classmethod
    def Rx(cls, angle, unit='rad'):
        return cls.rot(rotx(angle, unit=unit))

    @classmethod
    def Ry(cls, angle, unit='rad'):
        return cls.rot(roty(angle, unit=unit))

    @classmethod
    def Rz(cls, angle, unit='rad'):
        return cls.rot(rotz(angle, unit=unit))

    @classmethod
    def vec(cls, arg_in):
        assert isvec(arg_in, 4)
        unit_qr = cls(float(arg_in[0, 0]), arg_in[0, 1:4])
        return unit_qr.unit()

    def plot(self):
        SO3.np(self.r()).plot()

    def matrix(self):
        pass

    def to_rpy(self):
        return tr2rpy(self.r())

    def to_angvec(self):
        pass

    def to_so3(self):
        return SO3.np(self.r())

    def to_se3(self):
        return SE3(so3=SO3.np(self.r()))

    def tr2q(self, t):
        """
        Converts a homogeneous rotation matrix to a Quaternion object
        Code retrieved from: https://github.com/petercorke/robotics-toolbox-python/blob/master/robot/Quaternion.py
        Original authors: Luis Fernando Lara Tobar and Peter Corke
        :param t: homogeneous matrix
        :return: quaternion object
        """
        assert ishomog(t, (3, 3)), "Argument must be 3x3 homogeneous numpy matrix"
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
