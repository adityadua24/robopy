""" Converting Matricies  """

import math
import numpy as np 

def r2t( rmat ):
    """ r2t, convert rotation matrix to a homogeneous transform """
    dim = np.ndarray.shape(rmat)
    if dim(0) != dim(1):
        raise ValueError(' Matrix Must be square ')
    elif dim(0) == 2:
        tmp = np.r_[rmat, np.zeros((1,2))]
        return np.c_[ tmp, np.array([[0],[0],[1]]) ]
    elif dim(0) == 3:  
        tmp = np.r_[rmat, np.zeros((1,3))]
        return np.c_[ tmp, np.array([[0],[0],[0],[1]]) ]
    else:
        raise ValueError(' Value must be a rotation matrix ')
def t2r( tmat ):
    """ t2r, convert homogeneous transform to a rotation matrix """