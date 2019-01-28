#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: eval_graphics_vtk.py
DATE: Wed Jan  9 07:46:46 2019

@author: garyd
"""
###
### Run this in Spyder IDE IPython Console
###

import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.pose as pose
import robopy.base.model as model

import numpy as np


if __name__ == '__main__':
    
    ### Select a Graphics Rendering package to use.
    
    gobj = GraphicsRenderer('VTK')  # this sets graphics.gRenderer
    
    ### Define some GraphicsVTK parameters. 
    
    dMode = 'IPY'
    limits = [-4.0, 4.0, -4.0, 4.0, -4.0, 4.0]

    ### graphics_vtk.GraphicsVTK rendering base function example.
    
    # draw a red sphere in PIL (ImageMagick) window
    print("Draw a red sphere at the origin of XYZ reference system.")
    gobj.view(z_up=True, axes=True, limits=limits)
    gobj.draw_sphere()
    gobj.show(dispMode='PIL')
    
    # draw a red sphere in IPython output cell 
    print("Draw a red sphere at the origin of XYZ reference system.")
    gobj.view(z_up=True, axes=True, limits=limits)
    gobj.draw_sphere() 
    gobj.show(dispMode=dMode)
    
    ### RTB graphics examples using graphics_vtk.VtkPipeline.
    
    # SE2 pose plot
    print("Pose.SE2().plot(): one frame rotated 45 and 90 deg.")
    pose.SE2(theta=[45, 90], unit='deg').plot(dispMode=dMode,
                                              z_up=True,
                                              limits=limits)
    
    # SE3 pose plot in IPython output cell
    print("Pose.SE3().plot(): one frame rotated 45 and 90 deg about X-axis.")
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode=dMode, 
                                                 z_up=True,
                                                 limits=limits)
    
    # SE3 pose plot in PIL (ImageMagick) window
    print("Pose.SE3().plot(): one frame rotated 45 and 90 deg about X-axis.")
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode='PIL', 
                                                 z_up=True,
                                                 limits=limits)    
    
    # Define a Puma506 robot model.
    robot = model.Puma560()
    
    # Puma560 manipulator arm pose plot in IPython output cell
    print("SerialLink.plot(): Puma560 nominal pose.")
    robot.plot(robot.qn, dispMode=dMode, z_up=False, limits=None)

    # Puma560 manipulator arm pose plot in PIL window
    print("SerialLink.plot(): Puma560 nominal pose.")
    robot.plot(robot.qn, dispMode='PIL', z_up=False, limits=None)
