#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: mesh_geoms.py
DATE: Tue Jan 23 20:35:00 2019

@author: garyd
"""

import numpy as np


__all__ = ('cylinder',)


""" Geometric object defined as mesh grids
"""

def cylinder(center_x, center_y, radius, height_z):
    """
    Create a cylinder defined by 3 mesh arrays
    """
    z = np.linspace(0, height_z, 16)
    theta = np.linspace(0, 2*np.pi, 16)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return (x_grid,y_grid,z_grid)