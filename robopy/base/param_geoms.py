#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: param_geoms.py
DATE: Tue Jan 27 21:05:00 2019

@author: garyd
"""

import numpy as np

__all__ = ('apply_defaults_opts',
           'parametric_frame',
           'parametric_box',
           'parametric_beam',
           'parametric_sphere',
           'parametric_cylinder',
           'parametric_cone',
           'parametric_disk',
           'parametric_plane',
           'param_xyz_coord_arrays',)

""" Wrapper for parametric shape functions to allow defaults and
    optional values to be passed to functions as its arguments.
"""

def apply_defaults_opts(func, defaults, opts):
    """
    Apply defaults or opts values as arguments to given function.
    :param func: a function of the form f(*args)
    :param defaults: default argument keyword:value pairs dictionary
    :param opts: given optional argument keyword:value pairs dictionary
    :return: tuple of (x, y, z) square mesh arrays
    """
    if type(defaults) is dict and type(opts) is dict:
        arg_vals = []
        print("%s, %s" % (defaults, opts))
        for key, val in defaults.items():
            if key in opts:
                val = opts[key]
            arg_vals.append(val)
        if not arg_vals:
            return func()
        else:
            print(*arg_vals)
            return func(*arg_vals)
    else:
        print("*** Error: expected defaults and opts as dict for apply_default_opts.")
        return (0, 0, 0)

""" Geometric object defined as parametric meshes
"""

### Implementation Note:
###
### See mesh_geoms module for more efficient implementation of these
### parametric shape functions.

def parametric_frame(s):
    """ Parametric Cartesian coordinate frame
    """
    x = s * np.asmatrix([[0.0, 0.0, 0.0],[1.0, 0.0, 0.0],[0.0, 0.0, 0.0]])
    y = s * np.asmatrix([[0.0, 0.0, 0.0],[0.0, 1.0, 0.0],[0.0, 0.0, 0.0]])
    z = s * np.asmatrix([[0.0, 0.0, 0.0],[0.0, 0.0, 1.0],[0.0, 0.0, 0.0]])
    return (x, y, z)

def parametric_box(s):
    """ Parametric box shape
    """
    r = s*np.sqrt(2.0)/2.
    h = s/2.
    u = np.linspace(0.25*np.pi, 2.25*np.pi, 5)
    v = np.linspace(-1.0, 1.0, 5)
    x = r * np.outer(np.cos(u), np.ones(np.size(v)))
    y = r * np.outer(np.sin(u), np.ones(np.size(v)))
    z = h * np.outer(np.ones(np.size(u)), v)
    return (x, y, z)

def parametric_beam(d, l):
    """ Parametric beam shape
    """
    r = d*np.sqrt(2.0)/2.
    h = l/2.
    u = np.linspace(0.25*np.pi, 2.25*np.pi, 5)
    v = np.linspace(-1.0, 1.0, 5)
    x = r * np.outer(np.cos(u), np.ones(np.size(v)))
    y = r * np.outer(np.sin(u), np.ones(np.size(v)))
    z = h * np.outer(np.ones(np.size(u)), v)
    return (x, y, z)

def parametric_sphere(d, dim):
    """ Parametric sphere shape
    """
    r = d/2.
    u = np.linspace(0.0, 2*np.pi, dim)
    v = np.linspace(0.0, np.pi, dim)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))
    return (x, y, z)

def parametric_cylinder(d, l, dim):
    """ Parametric cylinder shape
    """
    r = d/2.
    h = l/2.
    u = np.linspace(0.0, 2*np.pi, dim)
    v = np.linspace(-1.0, 1.0, dim)
    x = r * np.outer(np.cos(u), np.ones(np.size(v)))
    y = r * np.outer(np.sin(u), np.ones(np.size(v)))
    z = h * np.outer(np.ones(np.size(u)), v)
    return (x, y, z)

def parametric_cone(d0, d1, l, dim):
    """ Parametric cone shape
    """
    r0 = d0/2.
    r1 = d1/2.
    f  = (r1-r0)/2.
    h  = l/2
    u  = np.linspace(0.0, 2*np.pi, dim)
    v  = np.linspace(-1.0, 1.0, dim)
    s  = r0 + f*(v+1.0)
    x  = s * np.outer(np.cos(u), np.ones(np.size(v)))
    y  = s * np.outer(np.sin(u), np.ones(np.size(v)))
    z  = h * np.outer(np.ones(np.size(u)), v)
    return (x, y, z)

def parametric_disk(d, h, dim):
    """ Parametric disk shape
    """
    r = d/2.
    u = np.linspace(0.0, 2*np.pi, dim)
    v = np.linspace(0.0, 1.0, dim)
    x = r * np.outer(np.cos(u), v)
    y = r * np.outer(np.sin(u), v)
    z = h * np.outer(np.ones(np.size(u)), np.ones(np.size(v)))
    return (x, y, z)

def parametric_plane(s, h, dim):
    """ Parametric plane shape
    """
    r = s/2.
    u = np.linspace(-1.0, 1.0, dim)
    v = np.linspace(-1.0, 1.0, dim)
    x = r * np.outer(u, np.ones(np.size(v)))
    y = r * np.outer(np.ones(np.size(u)), v)
    z = h * np.outer(np.ones(np.size(u)), np.ones(np.size(v)))
    return (x, y, z)

def param_xyz_coord_arrays(shape, **opts):
    """
    Returns parametric xyx coordinate arrays for named shape.
    :param shape: shape name
    :return: (x, y, z) tuple where each are NxN arrays.
    """
    shapes_list = ('frame', 'box', 'beam', 'sphere',
                   'cylinder', 'cone', 'disk', 'plane',)

    ### Implementation Note:
    ###
    ### The dim values for frame, box and beam must not be changed. The dim
    ### values for other shapes are based on a value of 1 for rstride and
    ### cstride in Matplotlib ax.plot_surface() and ax.plot_wireframe()
    ### functions called in Mpl3dArtist.plot_parametric_shape() method.

    if shape == 'frame':
        dim = 3
    elif shape in ['box', 'beam']:
        dim = 5
    elif shape in ['sphere', 'cylinder', 'cone', 'disk', 'plane']:
        dim = 16
    else:
        print('*** Error: invalid specified shape %s' % shape)
        print('           must be %s' % (list(shapes_list)))
        x = np.zeros((2, 2))
        y = np.zeros((2, 2))
        z = np.zeros((2, 2))
        return (x, y, z)

    if shape == 'frame':
        defaults = {'s': 1.0}
        (x, y, z) = apply_defaults_opts(parametric_frame, defaults, opts)
    elif shape == 'box':
        defaults = {'s': 1.0}
        (x, y, z) = apply_defaults_opts(parametric_box, defaults, opts)
    elif shape == 'beam':
        defaults = {'d': 1.0, 'l': 1.0}
        (x, y, z) = apply_defaults_opts(parametric_beam, defaults, opts)
    elif shape == 'sphere':
        defaults = {'d': 1.0, 'dim': dim}
        (x, y, z) = apply_defaults_opts(parametric_sphere, defaults, opts)
    elif shape == 'cylinder':
        defaults = {'d': 1.0, 'l': 1.0, 'dim': dim}
        (x, y, z) = apply_defaults_opts(parametric_cylinder, defaults, opts)
    elif shape == 'cone':
        defaults = {'d0': 1.0, 'dl': 0.5, 'l': 1.0, 'dim': dim}
        (x, y, z) = apply_defaults_opts(parametric_cone, defaults, opts)
    elif shape == 'disk':
        defaults = {'d': 1.0, 'h': 0.0, 'dim': dim}
        (x, y, z) = apply_defaults_opts(parametric_disk, defaults, opts)
    elif shape == 'plane':
        defaults = {'s': 1.0, 'h': 0.0, 'dim': dim}
        (x, y, z) = apply_defaults_opts(parametric_plane, defaults, opts)
    else:
        # processing should never get here.
        print("* Error: unknown shape %s in param_xyz_coord_arrays", shape)
        x = np.zeros((2,2))
        y = np.zeros((2,2))
        z = np.zeros((2,2))

    return (x, y, z)