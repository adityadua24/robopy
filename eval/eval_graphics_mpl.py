#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: eval_graphics_mpl.py
DATE: Tue Jan  8 07:56:00 2019

@author: garyd
"""

import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.pose as pose
import robopy.base.model as model

import numpy as np

if __name__ == '__main__':
    
    gobj = GraphicsRenderer('MPL')
    dMode = 'IPY'
    
    # red sphere
    gobj.draw_sphere()
    gobj.show()
    gobj.close()
    
    # SE3 pose plot
    #pose.SE3.Rx(theta=[45, 90], unit='deg').plot()
    
    # SE2 pose.plot
    #pose.SE2(theta=[45, 90], unit='deg').plot()

    # Puma560 pose
    robot = model.Puma560()
    robot.plot(robot.qn)
    
    # Puma560 animation    
    robot = model.Puma560()
    
    a = np.transpose(np.asmatrix(np.linspace(1, -180, 500)))
    b = np.transpose(np.asmatrix(np.linspace(1, 180, 500)))
    c = np.transpose(np.asmatrix(np.linspace(1, 90, 500)))
    d = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))
    e = np.asmatrix(np.zeros((500, 1)))
    f = np.concatenate((d, b, a, e, c, d), axis=1)

    robot.animate(stances=f, unit='deg', timer_rate=60, gif="Puma560", 
                             frame_rate=30, dispMode='VTK', limits=None)