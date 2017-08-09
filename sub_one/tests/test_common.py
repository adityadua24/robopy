# Created by: Aditya Dua
# 25 July, 2017
"""
This module contains all common helpful methods used in testing toolbox functionality
"""
import numpy as np
import numpy.testing as npt


def matrix_mismatch_string_builder(rec_mat, exp_mat):
    expected_mat_str = np.array2string(np.asarray(exp_mat))
    received_mat_str = np.array2string(np.asarray(rec_mat))
    output_str = str("\n----------------------\n"
                     + "    Expected Output    "
                     + "\n----------------------\n"
                     + expected_mat_str
                     + "\n----------------------\n"
                     + "    Received Output    "
                     + "\n----------------------\n"
                     + received_mat_str)
    return output_str


def matrices_equal(rec_mat, exp_mat, decimal=10):
    equal = True
    try:
        npt.assert_almost_equal(rec_mat, exp_mat, decimal=decimal)
    except AssertionError:
        equal = False
    return equal
