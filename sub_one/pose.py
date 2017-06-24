# Author - Aditya Dua - 13 June, 2017
# Pose module has class implementations of SO2, SO3, SE2 and SE3 type matrices

import numpy as np
import math
from sub_one.super_pose import SuperPose
import sub_one.test_args as test_args
from sub_one import transforms


# -----------------------------------------------------------------------------------------
class SO2(SuperPose):
    # --------------------------------------------------------------------------------------

    def __init__(self, args_in=None, unit='rad'):

        test_args.unit_check(unit)
        test_args.so2_input_types_check(args_in)
        self._unit = unit
        self._list = []
        angles_deg = []

        if args_in is None:
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
            # test_args.so2_input_matrix(args_in)
            # 2x2 and det == 1
            self._list.append(args_in)
        elif isinstance(args_in, list):
            test_args.so2_angle_list_check(args_in)
            if unit == "deg":
                for each_angle in args_in:
                    angles_deg.append(each_angle * math.pi / 180)
            for each_angle in angles_deg:
                self._list.append(np.matrix([[math.cos(each_angle), -math.sin(each_angle)],
                                             [math.sin(each_angle), math.cos(each_angle)]]))
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
class SE2(SuperPose):
    # ---------------------------------------------------------------------------------
    def __init__(self, x=None, y=None, z=None, rot=None, theta=None, unit='rad'):
        test_args.unit_check(unit)
        test_args.se2_inputs_check(x, y, z, rot, theta)
        self._list = []
        if x is not None and y is not None and theta is None and rot is None:
            pass
        elif x is not None and y is not None and theta is not None and rot is None:
            pass
        elif x is not None and y is not None and theta is None and rot is not None:
            pass
        elif x is None and y is None and theta is not None and rot is None:
            pass
        elif x is None and y is None and theta is None and rot is not None:
            pass
        elif x in None and y is None and theta is None and rot is None:
            self._list.append(np.asmatrix(np.eye(3, 3)))
        else:
            raise AttributeError("Valid Scenarios")


# ------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------
class SE3(SuperPose):
    # ---------------------------------------------------------------------------------
    pass

# ------------------------------------------------------------------------------------
