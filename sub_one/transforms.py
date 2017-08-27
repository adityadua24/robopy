# Created by: Josh Carrigg Hudson, Aditya Dua
# 1 June, 2017

""" Contains all of the transforms that will be used within the toolbox"""
import math
import numpy as np
from . import check_args
from .tests import test_transforms
import unittest
import vtk


# ---------------------------------------------------------------------------------------#
def rotx(theta, unit="rad"):
    """ rotx(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation  of THETA radians about the x-axis
        rotx(THETA, "deg") represents a rotation of THETA degrees about the x-axis"""
    check_args.unit_check(unit)
    if unit == "deg":
        theta = theta * math.pi / 180
    ct = math.cos(theta)
    st = math.sin(theta)
    mat = np.matrix([[1, 0, 0], [0, ct, -st], [0, st, ct]])
    mat = np.asmatrix(mat.round(15))
    return mat


# ---------------------------------------------------------------------------------------#
def roty(theta, unit="rad"):
    """ roty(THETA) is an SO(3) rotation matrix (3x3) representing a
        rotation of THETA radians about the y-axis
        roty(THETA, "deg") represents a rotation of THETA degrees about the y-axis"""
    check_args.unit_check(unit)
    if unit == "deg":
        theta = theta * math.pi / 180
    ct = math.cos(theta)
    st = math.sin(theta)
    mat = np.matrix([[ct, 0, st], [0, 1, 0], [-st, 0, ct]])
    mat = np.asmatrix(mat.round(15))
    return mat


# ---------------------------------------------------------------------------------------#
def rotz(theta, unit="rad"):
    """ rotz(THETA) is an SO(3) rotation matrix (3x3) representing a 
        rotation of THETA radians about the z-axis
        rotz(THETA, "deg") represents a rotation of THETA degrees about the z-axis"""
    check_args.unit_check(unit)
    if unit == "deg":
        theta = theta * math.pi / 180
    ct = math.cos(theta)
    st = math.sin(theta)
    mat = np.matrix([[ct, -st, 0], [st, ct, 0], [0, 0, 1]])
    mat = np.asmatrix(mat.round(15))
    return mat


# ---------------------------------------------------------------------------------------#
def trotx(theta, unit="rad"):
    """ T = trotx(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the x-axis.
        T = trotx(THETA, 'deg') as above but THETA is in degrees """
    check_args.unit_check(unit)
    tm = rotx(theta, unit)
    tm = np.r_[tm, np.zeros((1, 3))]
    mat = np.c_[tm, np.array([[0], [0], [0], [1]])]
    mat = np.asmatrix(mat.round(15))
    return mat


# ---------------------------------------------------------------------------------------#
def troty(theta, unit="rad"):
    """ T = troty(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the y-axis.
        T = troty(THETA, 'deg') as above but THETA is in degrees """
    check_args.unit_check(unit)
    tm = roty(theta, unit)
    tm = np.r_[tm, np.zeros((1, 3))]
    mat = np.c_[tm, np.array([[0], [0], [0], [1]])]
    mat = np.asmatrix(mat.round(15))
    return mat


# ---------------------------------------------------------------------------------------#
def trotz(theta, unit="rad"):
    """ T = trotz(THETA) is a homogeneous transformation (4x4) representing a rotation 
        of THETA radians about the z-axis.
        T = trotz(THETA, 'deg') as above but THETA is in degrees """
    check_args.unit_check(unit)
    tm = rotz(theta, unit)
    tm = np.r_[tm, np.zeros((1, 3))]
    mat = np.c_[tm, np.array([[0], [0], [0], [1]])]
    mat = np.asmatrix(mat.round(15))
    return mat


# ---------------------------------------------------------------------------------------#
def r2t(rmat):
    """ r2t, convert rotation matrix to a homogeneous transform """
    assert isinstance(rmat, np.matrix)
    dim = rmat.shape
    if dim[0] != dim[1]:
        raise ValueError(' Matrix Must be square ')
    elif dim[0] == 2:
        tmp = np.r_[rmat, np.zeros((1, 2))]
        mat = np.c_[tmp, np.array([[0], [0], [1]])]
        mat = np.asmatrix(mat.round(15))
        return mat
    elif dim[0] == 3:
        tmp = np.r_[rmat, np.zeros((1, 3))]
        mat = np.c_[tmp, np.array([[0], [0], [0], [1]])]
        mat = np.asmatrix(mat.round(15))
        return mat
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
        tmp = np.delete(tmat, [2], axis=0)
        mat = np.delete(tmp, [2], axis=1)
        mat = np.asmatrix(mat.round(15))
        return mat
    elif dim[0] == 4:
        tmp = np.delete(tmat, [3], axis=0)
        mat = np.delete(tmp, [3], axis=1)
        mat = np.asmatrix(mat.round(15))
        return mat
    else:
        raise ValueError('Value must be a rotation matrix ')


# ---------------------------------------------------------------------------------------#
def rot2(theta, unit='rad'):
    check_args.unit_check(unit)
    if unit == "deg":
        theta = theta * math.pi / 180
    ct = math.cos(theta)
    st = math.sin(theta)
    mat = np.matrix([[ct, -st], [st, ct]])
    mat = np.asmatrix(mat.round(15))
    return mat


# ---------------------------------------------------------------------------------------#
def rpy2r(thetas, order='zyx', unit='rad'):
    check_args.unit_check(unit)
    check_args.rpy2r(theta=thetas, order=order)
    if type(thetas[0]) is float or type(thetas[0]) is int:
        # TODO
        # enforce if one element is list.
        # All are list. OR one element is int or float then all are either int or float
        thetas = [thetas]  # Put list in a list

    if unit == 'deg':
        thetas = [[(angles * math.pi / 180) for angles in each_rpy] for each_rpy in thetas]
    if type(thetas[0]) is list:
        roll = [theta[0] for theta in thetas]
        pitch = [theta[1] for theta in thetas]
        yaw = [theta[2] for theta in thetas]

        if order == 'xyz' or order == 'arm':
            x = [rotx(theta) for theta in yaw]
            y = [roty(theta) for theta in pitch]
            z = [rotz(theta) for theta in roll]
            xyz = [(x[i] * y[i] * z[i]) for i in range(len(thetas))]
            xyz = [np.asmatrix(each.round(15)) for each in xyz]
            return xyz
        if order == 'zyx' or order == 'vehicle':
            z = [rotz(theta) for theta in yaw]
            y = [roty(theta) for theta in pitch]
            x = [rotx(theta) for theta in roll]
            zyx = [(z[i] * y[i] * x[i]) for i in range(len(thetas))]
            zyx = [np.asmatrix(each.round(15)) for each in zyx]
            return zyx
        if order == 'yxz' or order == 'camera':
            y = [roty(theta) for theta in yaw]
            x = [rotx(theta) for theta in pitch]
            z = [rotz(theta) for theta in roll]
            yxz = [(y[i] * x[i] * z[i]) for i in range(len(thetas))]
            yxz = [np.asmatrix(each.round(15)) for each in yxz]
            return yxz
    else:
        raise TypeError('thetas must be a list of roll pitch yaw angles\n'
                        'OR a list of list of roll pitch yaw angles.')


# ---------------------------------------------------------------------------------------#
def np2vtk(mat):
    if mat.shape == (4, 4):
        obj = vtk.vtkMatrix4x4()
        for i in range(4):
            for j in range(4):
                obj.SetElement(i, j, mat[i, j])
        return obj


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
