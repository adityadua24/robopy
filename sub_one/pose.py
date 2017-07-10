# Author - Aditya Dua - 13 June, 2017
# Pose module has class implementations of SO2, SO3, SE2 and SE3 type matrices

import numpy as np
import math
from . import test_args
from . import transforms
from .super_pose import SuperPose


# -----------------------------------------------------------------------------------------
class SO2(SuperPose):
    # --------------------------------------------------------------------------------------

    def __init__(self, args_in=None, unit='rad', null=False):

        test_args.unit_check(unit)
        test_args.so2_input_types_check(args_in)
        self._unit = unit
        self._list = []
        angles_deg = []

        if null:  # Usually only internally used to create empty objects
            pass
        elif args_in is None:
            self._list.append(np.asmatrix(np.eye(2, 2)))
        elif isinstance(args_in, int) or isinstance(args_in, float):
            if unit == 'deg':
                args_in = args_in * math.pi / 180
            self._list.append(np.matrix([[math.cos(args_in), -math.sin(args_in)],
                                         [math.sin(args_in), math.cos(args_in)]]))
        elif isinstance(args_in, SO2):
            test_args.so2_valid(args_in)
            for each_matrix in args_in:
                self._list.append(each_matrix)
        elif isinstance(args_in, np.matrix):
            # TODO
            test_args.so2_input_matrix(args_in)
            # 2x2 and det == 1
            self._list.append(args_in)
        elif isinstance(args_in, list):
            test_args.so2_angle_list_check(args_in)
            if unit == "deg":
                for each_angle in args_in:
                    angles_deg.append(each_angle * math.pi / 180)
            for each_angle in angles_deg:
                self._list.append(transforms.rot2(each_angle))
        else:
            pass

    @property
    def angle(self):
        angles = []
        for each_matrix in self:
            angles.append(math.atan2(each_matrix[1, 0], each_matrix[0, 0]))
        if len(angles) == 1:
            return angles[0]
        elif len(angles) > 1:
            return angles

    @property
    def det(self):
        det_list = []
        for each_matrix in self:
            det_list.append(np.linalg.det(each_matrix))
        if len(det_list) == 1:
            return det_list[0]
        elif len(det_list) > 1:
            return det_list

    def SE2(self):
        for each_matrix in self:
            transforms.r2t(each_matrix)

    def inv(self):
        inv_list = []
        for each_matrix in self:
            inv_list.append(np.matrix.transpose(each_matrix))
        if len(inv_list) == 1:
            return inv_list[0]
        elif len(inv_list) > 1:
            return inv_list


# --------------------------------------------------------------------------------
class SO3(SuperPose):
    # -------------------------------------------------------------------------------
    pass


# ---------------------------------------------------------------------------------
class SE2(SO2):
    # ---------------------------------------------------------------------------------
    def __init__(self, unit='rad', x=None, y=None, theta=None, rot=None, so2=None, se2=None, null=False):
        test_args.unit_check(unit)
        test_args.se2_inputs_check(x, y, rot, theta, so2, se2)
        self._list = []
        self._transl = []
        self._unit = unit
        if theta is None:
            theta = 0
        if unit == 'deg':
            if isinstance(theta, list):
                for i in range(len(theta)):
                    theta[i] = theta[i] * math.pi / 180
            else:
                theta = theta * math.pi / 180

        if null:
            pass
        elif x is not None and y is not None and rot is None and se2 is None and so2 is None:
            if isinstance(x, list) and isinstance(y, list):
                for i in range(len(x)):
                    self._transl.append((x[i], y[i]))
                    angle = 0
                    if isinstance(theta, list):
                        angle = theta[i]
                    else:
                        angle = theta
                    mat = transforms.rot2(angle)
                    mat = SE2.form_trans_matrix(mat, (x[i], y[i]))
                    self._list.append(mat)
            else:
                self._transl.append((x, y))
                mat = transforms.rot2(theta)
                mat = SE2.form_trans_matrix(mat, (x, y))
                self._list.append(mat)
        elif x is not None and y is not None and rot is not None and se2 is None and so2 is None:
            if isinstance(x, list) and isinstance(y, list) and isinstance(rot, list):
                for i in range(len(x)):
                    self._transl.append((x[i], y[i]))
                    mat = SE2.form_trans_matrix(rot[i], (x[i], y[i]))
                    self._list.append(mat)
            else:
                self._transl.append((x, y))
                mat = SE2.form_trans_matrix(rot, (x, y))
                self._list.append(mat)
        elif x is None and y is None and rot is not None and se2 is None and so2 is None:
            if isinstance(rot, list):
                for i in range(len(rot)):
                    self._transl.append((0, 0))
                    mat = SE2.form_trans_matrix(rot[i], (0, 0))
                    self._list.append(mat)
            else:
                self._transl.append((0, 0))
                mat = SE2.form_trans_matrix(rot, (0, 0))
                self._list.append(mat)
        elif x is None and y is None and rot is None and se2 is not None and so2 is None:
            self._transl = se2.transl
            for each_matrix in se2:
                self._list.append(each_matrix)
        elif x is None and y is None and rot is None and se2 is None and so2 is not None:
            for i in range(so2.length):
                self._transl.append((0, 0))
            for each_matrix in so2:
                mat = SE2.form_trans_matrix(each_matrix, (0, 0))
                self._list.append(mat)
        elif x is None and y is None and rot is None and se2 is None and so2 is None and isinstance(theta, list):
            for i in range(len(theta)):
                mat = transforms.rot2(theta[i])
                mat = SE2.form_trans_matrix(mat, (0, 0))
                self._list.append(mat)
        elif x is None and y is None and rot is None and se2 is None and so2 is None and theta != 0:
            mat = transforms.rot2(theta)
            mat = SE2.form_trans_matrix(mat, (0, 0))
            self._list.append(mat)
        elif x is None and y is None and rot is None and se2 is None and so2 is None and theta == 0:
            self._list.append(np.asmatrix(np.eye(3, 3)))
            self._transl.append((0, 0))
        else:
            raise AttributeError("\nINVALID instantiation. Valid scenarios:-\n"
                                 "SE2(x, y)\n"
                                 "SE2(x, y, rot)\n"
                                 "SE2(x, y, theta)\n"
                                 "SE2(se2)\n"
                                 "SE2(so2)\n"
                                 "SE2(theta)"
                                 "SE2(rot)")

    @staticmethod
    def form_trans_matrix(rot, transl):
        rot = np.r_[rot, np.matrix([0, 0])]
        rot = np.c_[rot, np.matrix([[transl[0]], [transl[1]], [1]])]
        return rot

    @property  # transl_vec is dependent on this !
    def transl(self):
        return self._transl

    @transl.setter
    def transl(self, value):
        assert isinstance(value, tuple) and len(value) == 2
        self._transl = value

    @property
    def transl_vec(self):
        return np.matrix([[self.transl[0]], [self.transl[1]]])

    def SE3(self):
        # TODO
        pass


# ------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
class SE3(SuperPose):
    # ---------------------------------------------------------------------------------
    pass

# ------------------------------------------------------------------------------------
