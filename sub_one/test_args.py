"""test_args module contains test for input arguments.
It checks if input argument passed by user is valid or not.
If any invalid data is found,
the called function in test_args returns false"""
import numpy as np
from sub_one import pose


def is_mat_list(list_matrices):
    """is_mat_list checks(arg1) checks if arg1
    is a list containing numpy matrix data type elements or not.
    If not, False is returned."""
    flag = True
    if isinstance(list_matrices, list):
        for matrix in list_matrices:
            if not isinstance(matrix, np.matrix):
                flag = False
                # TODO Check for matrix dimensions?
    else:
        flag = False
    return flag


def unit_check(unit):
    if unit == 'rad' or unit == 'deg':
        pass
    else:
        raise ValueError("Invalid unit value passed. Must be 'rad' or 'deg' only.")


# ------------------------------------------------------
# ------------  SUPER POSE CHECKS-----------------------
def valid_pose(pose):
    # TODO -- IMPLEMENT THIS
    pass


def super_pose_appenditem(object, item):
    # TODO -- IMPLEMENT THIS
    pass


def super_pose_multiply_check(object, other):
    # assert type(object) is type(other)
    # assert valid_pose(object)
    # assert valid_pose(other)
    pass


# ----------------- POSE.SO2 CHECKS -------------------------
def so2_angle_list_check(ang_list):
    for each in ang_list:
        assert isinstance(each, int) or isinstance(each, float)


def so2_input_types_check(args_in):
    assert isinstance(args_in, np.matrix) \
           or isinstance(args_in, list) \
           or isinstance(args_in, int) \
           or isinstance(args_in, float) \
           or isinstance(args_in, pose.SO2)

# ----------------- POSE.SO2 CHECKS ----------------------------
# ----------------- SUPER POSE CHECKS ---------------------------
