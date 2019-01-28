#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: eval_graphics_vtk.py
DATE: Wed Jan  9 07:46:46 2019

@author: garyd
"""

import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.pose as pose
import robopy.base.model as model

import numpy as np

if __name__ == '__main__':
    
    ### Select a Graphics Rendering package to use.
    
    gobj = GraphicsRenderer('VTK')  # this sets graphics.gRenderer
    
    ### Define some GraphicsVTK parameters. 
    
    dMode = 'VTK'
    limits = [-4.0, 4.0, -4.0, 4.0, -4.0, 4.0]

    ### graphics_vtk.GraphicsVTK rendering base function example.
    
    # draw a red sphere in default VTK window
    print("Draw a red sphere at the origin of XYZ reference system.")
    gobj.view(z_up=True, axes=True, limits=limits)
    gobj.draw_sphere()
    gobj.show(dispMode=dMode)
    
    # draw a red sphere in PIL (ImageMagick) window
    print("Draw a red sphere at the origin of XYZ reference system.")
    gobj.view(z_up=True, axes=True, limits=limits)
    gobj.draw_sphere() 
    gobj.show(dispMode='PIL')
    
    ### RTB graphics examples using graphics_vtk.VtkPipeline.
    
    # SE2 pose plot
    print("Pose.SE2().plot(): one frame rotated 45 and 90 deg.")
    pose.SE2(theta=[45, 90], unit='deg').plot(dispMode=dMode,
                                              z_up=True,
                                              limits=limits)
    
    # SE3 pose plot in VTL window
    print("Pose.SE3().plot(): one frame rotated 45 and 90 deg about X-axis.")
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode=dMode, 
                                                 z_up=True,
                                                 limits=limits)
    
    # SE3 pose plot in PIL (ImageMagick) window
    print("Pose.SE3().plot(): one frame rotated 45 and 90 deg about X-axis.")
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode='PIL', 
                                                 z_up=True,
                                                 limits=limits)
    
    # SE3 pose animation
    print("Pose.SO3().animate(): interpolation from 45 to 90 about X-axis.")
    print("Wait until animation is done before interaction with rendering.")
    other = pose.SO3.Rx(theta=90, unit='deg')
    pose.SO3.Rx(theta=45, unit='deg').animate(other=other,
                                              duration=5,
                                              gif="Pose_SO3",
                                              frame_rate=30,
                                              dispMode=dMode,
                                              z_up=False)
    
    
    # Define a Puma506 robot model.
    robot = model.Puma560()
    
    # Puma560 manipulator arm pose plot
    print("SerialLink.plot(): Puma560 nominal pose.")
    robot.plot(robot.qn, dispMode=dMode, z_up=False, limits=None)
    
    # Puma560 manipilator arm animation example.
    print("SerialLink.animate(): Puma560 stance matrix.")
    print("Wait until animation is done before interaction with rendering.")
    a = np.transpose(np.asmatrix(np.linspace(1, -180, 500)))
    b = np.transpose(np.asmatrix(np.linspace(1, 180, 500)))
    c = np.transpose(np.asmatrix(np.linspace(1, 90, 500)))
    d = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))
    e = np.asmatrix(np.zeros((500, 1)))
    f = np.concatenate((d, b, a, e, c, d), axis=1)
    robot.animate(stances=f, unit='deg', 
                  timer_rate=60, gif="Puma560", frame_rate=30)
    