#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Append path to robopy package to sys.path
#
# Note: For development, this is platform and user specific.
#
import os
import _robopy


# In[2]:


# import robopy GraphicsRenderer

from robopy.base.graphics import GraphicsRenderer


# In[3]:


# import robopy pose and model modules

import robopy.base.pose as pose
import robopy.base.model as model


# In[4]:


# Select a Graphics Rendering package to use.

gobj = GraphicsRenderer('VTK')  # this sets graphics.gRenderer


# In[5]:


# Define some GraphicsVTK parameters whcich will be used in draw()
# and plot() function calls in following cells.

dMode = 'IPY'
limits = [-4.0, 4.0, -4.0, 4.0, -4.0, 4.0]


# In[6]:


# Draw a red sphere using VTK and display below.

gobj.view(z_up=True, axes=True, limits=limits)
gobj.draw_sphere()
gobj.show(dispMode=dMode)


# In[7]:


# Plot SE3 pose using VTK and display below.

pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode=dMode, z_up=True, limits=limits)


# In[8]:


# Plot SE3 pose using VTK and display in PIL (Imagemagick) window

if 'BINDER_SERVICE_HOST' not in os.environ:
    # display this if not on MyBinder
    pose.SE3.Rx(theta=[45, 90], unit='deg').plot(dispMode='PIL', z_up=True, limits=limits)


# In[9]:


# Define a Puma506 robot model.
robot = model.Puma560()
    
# Puma560 manipulator arm pose plot using VTK and displayed below.
robot.plot(robot.qn, dispMode=dMode, z_up=False, limits=None)


# In[10]:


# Puma560 manipulator arm pose plot using VTK and displayed in PIL (Imagemagick) window

if 'BINDER_SERVICE_HOST' not in os.environ:
    # display this if not on MyBinder
    robot.plot(robot.qn, dispMode='PIL', z_up=False, limits=None)


# In[ ]:




