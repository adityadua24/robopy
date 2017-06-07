"""Common Module contains code shared by robotics and machine vision toolboxes"""
import numpy as np
from . import test_args


def ishomog(tr, dim, rtest=''):
    """ISHOMOG Test if SE(3) homogeneous transformation matrix.
    ISHOMOG(T) is true if the argument T is of dimension 4x4 or 4x4xN, else false.
    ISHOMOG(T, 'valid') as above, but also checks the validity of the rotation sub-matrix.
    See Also: isrot, ishomog2, isvec"""

    assert dim == [3, 3] or dim == [4, 4]
    is_valid = None
    if rtest == 'valid':
        is_valid = lambda matrix: abs(np.linalg.det(matrix) - 1) < np.spacing(1)
    flag = True
    if test_args.is_mat_list(tr):
        for matrix in tr:
            if not (matrix.shape[0] == dim[0] and matrix.shape[1] == dim[0]):
                flag = False
        # if rtest = 'valid'
        if flag and rtest == 'valid':
            flag = is_valid(tr[0])  # As in matlab code only first matrix is passed for validity test
            # TODO-Do we need to test all matrices in list for validity of rotation submatrix -- Yes
    elif isinstance(tr, np.matrix):
        if tr.shape[0] == dim[0] and tr.shape[1] == dim[0]:
            if flag and rtest == 'valid':
                flag = is_valid(tr)
        else:
            flag = False
    else:
        raise ValueError('Invalid data type passed to common.ishomog()')
    return flag


def isvec(v, l=3):
    """
    ISVEC Test if vector
    """
    d = v.shape
    h = d.size == 2 and min(v.shape) == 1 and v.size == l

    return h
