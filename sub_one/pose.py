import numpy as np
import math
from sub_one.super_pose import SuperPose
import sub_one.test_args as test_args


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


# --------------------------------------------------------------------------------
class SO3(SuperPose):
    # -------------------------------------------------------------------------------
    pass


# ---------------------------------------------------------------------------------
class SE2(SuperPose):
    # ---------------------------------------------------------------------------------
    pass
# ------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------
class SE3(SuperPose):
    # ---------------------------------------------------------------------------------
    pass
# ------------------------------------------------------------------------------------
