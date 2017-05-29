""" """
import math
import numpy as np
#---------------------------------------------------------------------------------------#
def rotx(t, units= "rad"):
    """ rotx(THETA) or rotx(THETA, "rad") is an SO(3) rotation matrix (3x3) representing a 
        rotation  of THETA radians about the x-axis
        rotx(THETA, "deg") represents a rotation of THETA degrees about the x-axis"""
    if units != "deg" and units != "rad":
        raise ValueError(' Invalid input. Enter "deg" or "rad" ')
    if units == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.array([[1, 0, 0], [0, ct, -st], [0, st, ct]])
#---------------------------------------------------------------------------------------#
def roty(t, units= "rad"):
    """ roty(THETA) or roty(THETA, "rad") is an SO(3) rotation matrix (3x3) representing a
        rotation of THETA radians about the y-axis
        roty(THETA, "deg") represents a rotation of THETA degrees about the y-axis"""
    if units != "deg" and units != "rad":
        raise ValueError(' Invalid input. Enter "deg" or "rad" ')
    if units == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.array([[ct, 0, st], [0, 1, 0], [-st, 0, ct]])
#---------------------------------------------------------------------------------------#
def rotz(t, units= "rad"):
    """ rotz(THETA) or rotz(THETA, "rad") is an SO(3) rotation matrix (3x3) representing a 
        rotation of THETA radians about the z-axis
        rotz(THETA, "deg") represents a rotation of THETA degrees about the z-axis"""
    if units != "deg" and units != "rad":
        raise ValueError(' Invalid input. Enter "deg" or "rad" ')
    if units == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.array([[ct, -st, 0], [st, ct, 0], [0, 0, 1]])
#---------------------------------------------------------------------------------------#
def trotx(t, units="rad"):
    """ trotx(THETA) or trotx(THETA, "rad") is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the x-axis.
        trotx(THETA, 'deg') as above but THETA is in degrees """
    tm = rotx(t,units)
    tm = np.r_[tm, np.zeros((1,3))]
    return np.c_[ tm, np.array([[0],[0],[0],[1]]) ]
#---------------------------------------------------------------------------------------#
def troty(t, units="rad"):
    """ troty(THETA) or troty(THETA, "rad") is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the y-axis.
        troty(THETA, 'deg') as above but THETA is in degrees """
    tm = roty(t,units)
    tm = np.r_[tm, np.zeros((1,3))]
    return np.c_[ tm, np.array([[0],[0],[0],[1]]) ]

#---------------------------------------------------------------------------------------#
def trotz(t, units="rad"):
    """ trotz(THETA) or trotz(THETA, "rad") is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the z-axis.
        trotz(THETA, 'deg') as above but THETA is in degrees """
    tm = rotz(t,units)
    tm = np.r_[tm, np.zeros((1,3))]
    return np.c_[ tm, np.array([[0],[0],[0],[1]]) ]
#---------------------------------------------------------------------------------------#
def r2t( rmat ):
    """ r2t, convert rotation matrix to a homogeneous transform """
    dim = np.ndarray.shape(rmat)
    if dim(0) != dim(1):
        raise ValueError(' Matrix Must be square ')
    elif dim(0) == 2:
        tmp = np.r_[rmat, np.zeros((1,2))]
        return np.c_[ tmp, np.matrix([[0],[0],[1]]) ]
    elif dim(0) == 3:  
        tmp = np.r_[rmat, np.zeros((1,3))]
        return np.c_[ tmp, np.matrix([[0],[0],[0],[1]]) ]
    else:
        raise ValueError(' Value must be a rotation matrix ')