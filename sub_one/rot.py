""" rot is the rotation about the x, y or z axis """
import math
import numpy as np

def x(t, deg= "radians"):
    """ rotx(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation of THETA radians about the x-axis
        rotx(THETA, "deg") represents a rotation of THETA degrees about the x-axis"""
    if deg == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.array([[1, 0, 0], [0, ct, -st], [0, st, ct]])

def y(t, deg= "radians"):
    """ roty(THETA) is an SO(3) rotation matrix (3x3) representing a
        rotation of THETA radians about the y-axis
        roty(THETA, "deg") represents a rotation of THETA degrees about the y-axis"""
    if deg == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.array([[ct, 0, st], [0, 1, 0], [-st, 0, ct]])

def z(t, deg= "radians"):
    """ rotz(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation of THETA radians about the z-axis
        rotz(THETA, "deg") represents a rotation of THETA degrees about the z-axis"""
    if deg == "deg":
        t = t *math.pi/180
    ct = math.cos(t)
    st = math.sin(t)
    return np.array([[ct, -st, 0], [st, ct, 0], [0, 0, 1]])