""" """
import math
import numpy as np
#---------------------------------------------------------------------------------------#
def rotx(t, units= "rad"):
    """ rotx(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation  of THETA radians about the x-axis
        rotx(THETA, "deg") represents a rotation of THETA degrees about the x-axis"""
    if units == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.matrix('1 0 0; 0 ct -st; 0 st ct')
#---------------------------------------------------------------------------------------#
def roty(t, units= "rad"):
    """ roty(THETA) is an SO(3) rotation matrix (3x3) representing a
        rotation of THETA radians about the y-axis
        roty(THETA, "deg") represents a rotation of THETA degrees about the y-axis"""
    if units == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.matrix('ct 0 st; 0 1 0; -st 0 ct')
#---------------------------------------------------------------------------------------#
def rotz(t, units= "rad"):
    """ rotz(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation of THETA radians about the z-axis
        rotz(THETA, "deg") represents a rotation of THETA degrees about the z-axis"""
    if units == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.matrix('ct -st 0; st ct 0; 0 0 1')
#---------------------------------------------------------------------------------------#
def trotx(t, units="rad"):
    """ T = trotx(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the x-axis.
        T = trotx(THETA, 'deg') as above but THETA is in degrees """
    tm = rotx(t,units)
    tm = np.r_[tm, np.zeros((1,3))]
    return np.c_[ tm, np.array([[0],[0],[0],[1]]) ]
#---------------------------------------------------------------------------------------#
def troty(t, units="rad"):
    """ T = troty(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the y-axis.
        T = troty(THETA, 'deg') as above but THETA is in degrees """
    tm = roty(t,units)
    tm = np.r_[tm, np.zeros((1,3))]
    return np.c_[ tm, np.array([[0],[0],[0],[1]]) ]

#---------------------------------------------------------------------------------------#
def trotz(t, units="rad"):
    """ T = trotz(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the z-axis.
        T = trotz(THETA, 'deg') as above but THETA is in degrees """
    tm = rotz(t,units)
    tm = np.r_[tm, np.zeros((1,3))]
    return np.c_[ tm, np.array([[0],[0],[0],[1]]) ]
#---------------------------------------------------------------------------------------#