#!/usr/bin/env python
# coding: utf-8

# **Demonstration of RoboPy Pose.plot() and SerialLink.plot() rendering capability using MPL (Matplotlib.**

# In[1]:


import os  # for checking values of environment variables.

""" Matplotlib imports
"""
import matplotlib
matplotlib.use('Qt4Agg')
get_ipython().run_line_magic('matplotlib', 'notebook')

""" RoboPy imports
"""
import _robopy
from robopy.base.graphics import GraphicsRenderer
import robopy.base.pose as pose
import robopy.base.model as model


# In[2]:


# Select a Graphics Rendering package to use.

gobj = GraphicsRenderer('MPL')  # this sets graphics.gRenderer


# In[3]:


# Define some GraphicsVTK parameters whcich will be used in plot()
# method calls in following cells.

dMode = 'IPY'
limits = [-4.0, 4.0, -4.0, 4.0, -4.0, 4.0]


# In[4]:


# Plot SE3 pose using MPL and display below.

pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode=dMode, z_up=True, limits=limits)


# In[5]:


# Plot SE3 pose using VTK and display in PIL (Imagemagick) window

if 'BINDER_SERVICE_HOST' not in os.environ:
    # display this if not on MyBinder
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode='PIL', z_up=True, limits=limits)


# In[6]:


# Define a Puma506 robot model.
robot = model.Puma560()
    
# Puma560 manipulator arm pose plot using MPL and displayed below.
robot.plot(robot.qn, dispMode=dMode, z_up=False, limits=None)


# In[7]:


# Puma560 manipulator arm pose plot using MPL and displayed in PIL (Imagemagick) window

if 'BINDER_SERVICE_HOST' not in os.environ:
    # display this if not on MyBinder
    robot.plot(robot.qn, dispMode='PIL', z_up=False, limits=None)


# In[ ]:




