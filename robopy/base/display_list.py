#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: eval_displayList.py
DATE: Wed Jan 23 20:21:00 2019

@author: garyd
"""

### Implemention Note:
###
### Since these DisplayList classes deal exclusively with graphical entities,
### it may be more appropriate for them to be included with the Graphics class
### and associated components provided in the robopy/base/graphics.py file.
### This would put DisplayList within the 'graphics' namespace to permit such
### expressions as graphics.DisplayList() when the graphics module is imported
### as 'import robopy.base.graphics as graphics', or as DisplayList() when the
### graphics module is imported as 'from robopy.base.graphics import *'.

import copy
import numpy as np  # for array type methods

__all__ = ('DisplayList', 'DisplayListItem',)  # classes


class DisplayListItem:
    """
    Describes a single graphical entity that must be rendered at each animation step.
    """

    def __init__(self, type, name, data, args):
        self.type = type  # item type
        self.name = name  # item identifier

        if type == 'surface':
            # plot_surface data, 3 NxN meshes
            Xc = copy.deepcopy(data[0])  ### The use of deepcopy here may likely be
            Yc = copy.deepcopy(data[1])  ### superfluous, but this is being done to
            Zc = copy.deepcopy(data[2])  ### resolve DisplayList animation issues.

            self.shape = Xc.shape
            self.data = np.vstack((Xc.flatten(), Yc.flatten(), Zc.flatten()))  # create 3xN array
        elif type == 'command':
            self.command = name
        elif type == 'line':
            # TODO
            pass

        self.args = args                   # rendering function arguments
        self.transform = np.identity(4)    # homogeneous transform matrix
        self.gentity = None                # rendered graphical entity

    def reset(self):
        self.gentity = None

    def xform(self):
        ## transform the points

        R = self.transform[0:3, 0:3]
        t = self.transform[0:3, 3].reshape((3, 1))

        z = np.dot(R, self.data) + t  # rotate and translate

        # reshape the X,Y,Z components
        Xc = np.reshape(z[0, :], self.shape)
        Yc = np.reshape(z[1, :], self.shape)
        Zc = np.reshape(z[2, :], self.shape)

        return (Xc, Yc, Zc)


class DisplayList:
    """
    Is a list of Graphics DisplayListItems.
    """

    def __init__(self):
        self._displaylist = []

    def __iter__(self):
        return (each for each in self._displaylist)

    def add(self, type, name, data=None, **kwargs):
        """
        Add an entity to the display list, return a reference to the DisplayListItem
        that describes it, need this if we are going to apply a transformation to it
        """
        dli = DisplayListItem(type, name, data, kwargs)
        self._displaylist.append(dli)
        return dli

    def reset(self):
        """
        Reset graphics entities for each item in display list.
        :return:
        """
        for item in self._displaylist:
            item.reset()

    def clear(self):
        """
        Clear a display list.
        """
        self._displaylist = []
