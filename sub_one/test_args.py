"""test_args module contains test for input arguments.
It checks if input argument passed by user is valid or not.
If any invalid data is found,
the called function in test_args returns false"""
import numpy as np


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
