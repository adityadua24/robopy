# Author - Aditya Dua, Josh Carrigg Hudson - 1 June, 2017

""" Contains all of the transforms that will be used within the toolbox"""
import math
import numpy as np
from . import test_args
from .tests import test_transforms
import unittest


# ---------------------------------------------------------------------------------------#
def rotx(t, unit="rad"):
    """ rotx(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation  of THETA radians about the x-axis
        rotx(THETA, "deg") represents a rotation of THETA degrees about the x-axis"""
    test_args.unit_check(unit)
    if unit == "deg":
        t = t * math.pi / 180
    ct = math.cos(t)
    st = math.sin(t)
    return np.matrix([[1, 0, 0], [0, ct, -st], [0, st, ct]])


# ---------------------------------------------------------------------------------------#
def roty(t, unit="rad"):
    """ roty(THETA) is an SO(3) rotation matrix (3x3) representing a
        rotation of THETA radians about the y-axis
        roty(THETA, "deg") represents a rotation of THETA degrees about the y-axis"""
    test_args.unit_check(unit)
    if unit == "deg":
        t = t * math.pi / 180
    ct = math.cos(t)
    st = math.sin(t)
    return np.matrix([[ct, 0, st], [0, 1, 0], [-st, 0, ct]])


# ---------------------------------------------------------------------------------------#
def rotz(t, unit="rad"):
    """ rotz(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation of THETA radians about the z-axis
        rotz(THETA, "deg") represents a rotation of THETA degrees about the z-axis"""
    test_args.unit_check(unit)
    if unit == "deg":
        t = t * math.pi / 180
    ct = math.cos(t)
    st = math.sin(t)
    return np.matrix([[ct, -st, 0], [st, ct, 0], [0, 0, 1]])


# ---------------------------------------------------------------------------------------#
def trotx(t, unit="rad"):
    """ T = trotx(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the x-axis.
        T = trotx(THETA, 'deg') as above but THETA is in degrees """
    test_args.unit_check(unit)
    if unit == "deg":
        t = t * math.pi / 180
    tm = rotx(t, unit)
    tm = np.r_[tm, np.zeros((1, 3))]
    return np.c_[tm, np.array([[0], [0], [0], [1]])]


# ---------------------------------------------------------------------------------------#
def troty(t, unit="rad"):
    """ T = troty(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the y-axis.
        T = troty(THETA, 'deg') as above but THETA is in degrees """
    test_args.unit_check(unit)
    if unit == "deg":
        t = t * math.pi / 180
    tm = roty(t, unit)
    tm = np.r_[tm, np.zeros((1, 3))]
    return np.c_[tm, np.array([[0], [0], [0], [1]])]


# ---------------------------------------------------------------------------------------#
def trotz(t, unit="rad"):
    """ T = trotz(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the z-axis.
        T = trotz(THETA, 'deg') as above but THETA is in degrees """
    test_args.unit_check(unit)
    if unit == "deg":
        t = t * math.pi / 180
    tm = rotz(t, unit)
    tm = np.r_[tm, np.zeros((1, 3))]
    return np.c_[tm, np.array([[0], [0], [0], [1]])]


# ---------------------------------------------------------------------------------------#
def r2t(rmat):
    """ r2t, convert rotation matrix to a homogeneous transform """
    assert isinstance(rmat, np.matrix)
    dim = rmat.shape
    if dim[0] != dim[1]:
        raise ValueError(' Matrix Must be square ')
    elif dim[0] == 2:
        tmp = np.r_[rmat, np.zeros((1, 2))]
        return np.c_[tmp, np.array([[0], [0], [1]])]
    elif dim[0] == 3:
        tmp = np.r_[rmat, np.zeros((1, 3))]
        return np.c_[tmp, np.array([[0], [0], [0], [1]])]
    else:
        raise ValueError(' Value must be a rotation matrix ')


# ---------------------------------------------------------------------------------------#
def t2r(tmat):
    """ t2r, convert a given homogeneous transform to a rotation matrix """
    assert isinstance(tmat, np.matrix)
    dim = tmat.shape
    if dim[0] != dim[1]:
        raise ValueError(' Matrix Must be square ')
    elif dim[0] == 3:
        tmp = np.delete(tmat, (2), axis=0)
        return np.delete(tmp, (2), axis=1)
    elif dim[0] == 4:
        tmp = np.delete(tmat, (3), axis=0)
        return np.delete(tmp, (3), axis=1)
    else:
        raise ValueError('Value must be a rotation matrix ')


# ---------------------------------------------------------------------------------------#
def rot2(t, unit='deg'):
    test_args.unit_check(unit)
    if unit == "deg":
        t = t * math.pi / 180
    ct = math.cos(t)
    st = math.sin(t)
    return np.matrix([[ct, -st], [st, ct]])


# ---------------------------------------------------------------------------------------#
if __name__ == '__main__':
    # When run as main, initialise test cases in test_classes_to_tun and runs them
    # Refer
    # https://stackoverflow.com/questions/5360833/how-to-run-multiple-classes-in-single-test-suite-in-python-unit-testing
    test_classes_to_run = [test_transforms.TestRotx]

    loader = unittest.TestLoader()

    suits_list = []
    for test_class in test_classes_to_run:
        suits_list.append(loader.loadTestsFromTestCase(test_class))

    big_suite = unittest.TestSuite(suits_list)

    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(big_suite)
