#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: eval_display_list_mpl.py
DATE: Wed Jan 23 20:21:00 2019

@author: garyd
"""

# Import requisite robopy modules.
import _robopy                             # locates desired robopy module
import robopy.base.graphics as graphics    # to perform graphics
import robopy.base.display_list as dList   # to use display lists
import robopy.base.transforms as tr        # to apply transforms
from robopy.base.mesh_geoms import *       # to use mesh geometric shapes
import numpy as np                         # to use NumPy ndarray type

# Define an object.
cyl = cylinder(0.2,0.2,0.05,0.1)  # create a cylinder

# Create two transformation matrices.
Rx = np.array( [[1,0,0,0], [0,0,-1,0], [0,1,0,0],[0,0,0,1]])
Ry = np.array( [[0,0,1,0],[0,1,0,0],[-1,0,0,0],[0,0,0,1]] )

# Create a DisplayList with 3 instances of the cylinder,
# keep the DisplayListItem references
dl = dList.DisplayList()
dl1 = dl.add('surface', 'cyl1', cyl, color='blue')
dl2 = dl.add('surface', 'cyl2', cyl, color='red')
dl3 = dl.add('surface', 'cyl3', cyl, color='green')

# and 3 generic graphics commands.
##dl.add('command', "ax.set_xlabel('X')")
##dl.add('command', "ax.set_ylabel('Y')")
##dl.add('command', "ax.set_zlabel('Z')")

# Transform two of the cylinders by setting the transform field
dl2.transform = Rx
dl3.transform = Ry

### Implementation Note:
###
### The use of namespace qualifiers and global variables, such
### as graphics and gRenderer respectively, are artifacts of
### RTB for Python development work with graphics packages other
### than Matplotlib. These artifacts may change or be abstracted
### (hidden) from novice users of RTB for Python to reproduce the
### generally used MATLAB functions API by RTB for MATLAB and that
### which can be emulated using Matplotlib's defunct pylab API
### and current pyplot API. Developers and experienced users of
### RTB for Python may wish to work with an RTB for Python object
### -oriented API as can be currently done with Matplotlib.

# Obtain a robopy graphics renderer with utilizes ipyvolume.
graphics.GraphicsRenderer('IPV')  # sets graphics.gRenderer

# Resize the default figure
##graphics.gRenderer.getFigure().set_dpi(80)
##graphics.gRenderer.getFigure().set_size_inches((8,8), forward=True)

# Give graphics renderer the DisplayList to plot (gRenderer.plot()).
graphics.plot(dl, limits=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5])

# Define transform function to animate DisplayListItems.
def transFunc(t):
    """
    Sample transformation function to rotate display list
    'surface' items about their x-axis.
    :param t: time (sec)
    :return: a homogeneous transform matrix
    """
    return tr.trotx(2.0*t, unit="deg")

# Give graphics renderer the DisplayList to animate.
graphics.animate(dl, transFunc, duration=5.0, frame_rate=30, \
                     limits=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5])
