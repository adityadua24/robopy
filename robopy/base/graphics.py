#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: graphics.py
DATE: Tue Jan  8 17:34:00 2019

@author: garyd
"""

import sys
from abc import ABCMeta, abstractmethod

__all__ = ('Graphics', 'Gtransform', 'GraphicsRenderer',
           'rgb_named_colors',
           'plot', 'qplot', 'trplot', 'trplot2',
           'animate', 'panimate', 'qanimate', 'tranimate', 'tranimate2')

###
### MODULE CLASS DEFINITIONS
###

class Graphics(metaclass=ABCMeta):
    """ 
    Graphics interface for RTB.
    
    This Abstract Base Class (ABC) presents the graphical interface 
    between Robotics Toolbox (RTB) and graphics package(s) which 
    provide needed plotting, animation and rendering functionality.
    
    Implementation Notes:
        
      1) Graphics modules must provide, as a minimum, methods 
         denoted in this class.
         
      2) This class object should act as a factory for specific
         graphics rendering, animation and transform objects.
         
      3) Must be able to keep track of multiple rendering windows
         and in the case of Matplotlib, not block on show() and
         permit multiple poses rendered to a given figure.
    
    """
    def __init__(self):
        self._gRenderer = None
        self._gTransform = self._Gtransform()
    
    def _Gtransform(self):
        """ Instantiates and returns a graphics transform.
        """
        gxobj = Gtransform()
        return gxobj
    
    ### Instance property setters/getters
    
    """    
      _gRenderer = property(fset=setGraphicsRenderer, fget=getGraphicsRenderer)
      _gTransform = property(fset=None, fget=getGtransform)
    """
    
    def setGraphicsRenderer(self, gRenderer):
        self._gRenderer = gRenderer
        
    def getGraphicsRenderer(self):
        return self._gRenderer
        
    def getGtransform(self):
        return self._gTransform
    
    ### Graphics package interface methods (presented in alphabetical order)
           
    @abstractmethod
    def draw_axes2(self, *args, **kwargs):
        """ Graphics package draw plot axes for 2D space.
        """ 
        raise NotImplementedError('Need to define draw_axes2 emethod.')
        
    @abstractmethod
    def draw_axes3(self, *args, **kwargs):
        """ Graphics package draw plot axes for 3D space.
        """ 
        raise NotImplementedError('Need to define draw_axes3 emethod.')
        
    @abstractmethod
    def draw_cube(self):
        """ Graphics package draw a blue cube method.
        """
        raise NotImplementedError('Need to define draw_cube emethod.')
        
    @abstractmethod
    def draw_sphere(self):
        """ Graphics package draw a red sphere method.
        """
        raise NotImplementedError('Need to define draw_sphere emethod.')
        
    @abstractmethod  # forces definition of a graphics module scope routine
    def rgb_named_colors(cls, *args, **kwarg):
        """ Graphics package returns RGB values for named colors.
        """ 
        raise NotImplementedError('Need to define rgb_named_colors method.')
        
    @abstractmethod
    def setGtransform(self, *args, **kwargs):
        """ Graphics package set graphics transform method.
        """
        raise NotImplementedError('Need to define setGtransform emethod.')
        
    @abstractmethod
    def view(self, *args, **kwargs):
        """ Graphics package set view space method.
        """
        raise NotImplementedError('Need to define view emethod.')
        
    ## RTB interface methods (presented in alphabetical order)
    
    @abstractmethod
    def animate(self, *args, **kwargs):
        """ RTB interface method.
        """
        raise NotImplementedError('Need to define animate method.')
        
    @abstractmethod
    def plot(self, *args, **kwargs):
        """ RTB interface method.
        """
        raise NotImplementedError('Need to define plot method.')
        
    @abstractmethod
    def qplot(self, *args, **kwargs):
        """ RTB interface method. 
        """ 
        raise NotImplementedError('Need to define qplot method.')

    @abstractmethod
    def render(self, *args, **kwargs):
        """ VTk interface method
        """
        raise NotImplementedError('Need to define render method.')
    
    @abstractmethod
    def show(self, *args, **kwargs):
        """ Matplotlib interface method
        """
        raise NotImplementedError('Need to define show method.')
        
    @abstractmethod
    def tranimate(self, *args, **kwargs):
        """ RTB interface method.
        """
        raise NotImplementedError('Need to define tranimate method.')
        
    @abstractmethod
    def tranimate2(self, *args, **kwargs):
        """ RTB interface method.
        """
        raise NotImplementedError('Need to define tranimate2 method.')
        
    @abstractmethod
    def trplot(self, *args, **kwargs):
        """ RTB interface method.
        """
        raise NotImplementedError('Need to define trplot method.')
        
    @abstractmethod        
    def trplot2(self, *args, **kwargs):
        """ RTB interface method.
        """ 
        raise NotImplementedError('Need to define trplot2 method.')

    # Display List Interface - These methods must be defined in Graphics Rendering Classes

    @abstractmethod
    def renderDisplayListItem(self, *args, **kwargs):
        """ Graphics package renderDisplayListItem
        """
        raise NotImplementedError('Need to define renderDisplayListItem method.')

    @abstractmethod
    def renderDisplayList(self, *args, **kwargs):
        """ Graphics package renderDisplayList
        """
        raise NotImplementedError('Need to define renderDisplayList method.')

    @abstractmethod
    def plotDisplayList(self, *args, **kwargs):
        """ Graphics package plotDisplayList
        """
        raise NotImplementedError('Need to define plotDisplayList method.')

    @abstractmethod
    def animateDisplayList(self, *args, **kwargs):
        """ Graphics package animateDisplayList
        """
        raise NotImplementedError('Need to define animateDisplayList method.')


class Gtransform(Graphics):
    """
    Graphics transform for RTB.
    
    This Abstract Base Class (ABC) presents the graphical interface 
    between Robotics Toolbox (RTB) and graphics package(s) which 
    provide needed graphics transform functionality.
    
    Graphics modules must provide, as a minimum, methods denoted 
    in this class
    """
    def __init__(self):
        super(Graphics,self).__init__()
    
    def setGtransform(self, *args, **kwargs):
        """ Set graphics transform.
        """
        raise NotImplementedError('Need to define setGtransform emethod.')
        
###
### MODULE PUBLIC INTERFACE ROUTINES
###

""" These routines comprise the external interface to RTB plotting and 
    animation functions. They preclude the need to instantiate graphics 
    objects in the RTB manipulator and math modules such as pose, 
    serial_link, quaternion and transforms.

    Implementation Notes:
        
      1) These functions are generally not invoked by the user, but 
         by the corresponding calling function in RTB modules which 
         are exposed to the user.

      2) The header documentation for called functions herein should
         match that of corresponding calling functions in RTB modules. 
         See graphics_vtk.VtkPipeline.animate(), animate() below and 
         serial_link.SerialLink.animate() as a pertinent example.
         
      3) The function argument list keyword/value validity checking
         of RTB specific parameters should be done in the RTB modules
         before these functions are called. While graphing, rendering
         and plotting parameters validity should be checked in this
         graphics module, or dedicated submodules, with exceptions
         returned to RTB for resolution. It is possible that all data
         unit conversion could be done in RTB before the values are
         passed here (i.e., use only 'rad' herein for numerical 
         computation, but allow for user's desire for data values to
         be graphically displayed in 'deg' units).
         
      4) Though there may be historical and mathematical precedence
         involved in the preservation of RTB for MATLAB matrix data
         structures, there is no meaningful reason to force the NumPy
         matrix type class on graphics processing. The more appropriate
         data type class commonly used is the NumPy ndarray. Note the 
         effort to convert x, y & z bounds from matrices to arrays which 
         can then be accessed using just one index as in VtkPipeline
         qplot() and animate() methods in the graphics_vtk module.
"""

from . import tb_parseopts as tbpo
from . import graphics_vtk as gVtk
from . import graphics_mpl as gMpl
from . import graphics_ipv as gIpv

gRenderer = None  # the instantiated graphics rendering object

def GraphicsRenderer(renderer):
    """ 
    Instantiates and returns a graphics renderer.
    
    :param renderer: renderer descriptor string
    :return gRenderer: graphics rendering object      
    """
    global gRenderer
    
    if renderer == 'VTK':
        gRenderer = gVtk.VtkPipeline()
    elif renderer == 'MPL':
        gRenderer = gMpl.Mpl3dArtist(0)
    elif renderer == 'IPV':
        gRenderer = gIpv.Ipv3dVisual(1)
    else:
        print("The %s renderer is not supported." % renderer)
        print("Renderer must be VTK or MPL (Matplotlib).")
        sys.exit()
    return gRenderer
    
def rgb_named_colors(colors):
    global gRenderer
    if type(gRenderer) is type(gVtk.VtkPipeline()):
        return gVtk.rgb_named_colors(colors)
    elif type(gRenderer) is type(gMpl.Mpl3dArtist()):
        return gMpl.rgb_named_colors(colors)
    elif type(gRenderer) is type(gIpv.Ipv3dVisual()):
        return gIpv.rgb_named_colors(colors)

def plot(obj, **kwargs):
    global gRenderer
    if type(gRenderer) is type(gVtk.VtkPipeline()):
        opts = { 'dispMode' : 'VTK',
               }
        opt = tbpo.asSimpleNs(opts)
        (opt, args) = tbpo.tb_parseopts(opt, **kwargs)
        pobj = gVtk.VtkPipeline(dispMode=opt.dispMode)
        pobj.plot(obj, **args)
    elif type(gRenderer) is type(gMpl.Mpl3dArtist()):
        pobj = gMpl.Mpl3dArtist(1)
        pobj.plot(obj, **kwargs)
    elif type(gRenderer) is type(gIpv.Ipv3dVisual()):
        pobj = gIpv.Ipv3dVisual(1)
        pobj.plot(obj, **kwargs)

def qplot(obj, stance, unit='rad', dispMode='VTK', **kwargs):
    global gRenderer
    if type(gRenderer) is type(gVtk.VtkPipeline()):
        opts = { 'dispMode' : 'VTK',
               }
        opt = tbpo.asSimpleNs(opts)
        (opt, args) = tbpo.tb_parseopts(opt, **kwargs)
        gobj = gVtk.VtkPipeline(dispMode=dispMode)
        gobj.qplot(obj, stance, unit='rad', dispMode=dispMode, **kwargs)
    elif type(gRenderer) is type(gMpl.Mpl3dArtist()):
        gobj = gMpl.Mpl3dArtist(1)
        gobj.qplot(obj, stance, unit='rad', **kwargs)
    elif type(gRenderer) is type(gIpv.Ipv3dVisual()):
        gobj = gIpv.Ipv3dVisual(1)
        gobj.qplot(obj, stance, unit='rad', **kwargs)
    
def tranimate(T):
    global gRenderer
    pass 

def tranimate2(R):
    global gRenderer
    pass
    
def trplot(T, handle=None, dispMode='VTK'):
    global gRenderer
    if handle is not None:
        if type(handle) is type(gVtk.VtkPipeline()):
             handle.trplot(T)
        elif type(handle) is type(super(gVtk).Hgtransform()):
             pass  # do Hgtransform stuff
        else:
             pass  # do error stuff   
    pobj = gVtk.VtkPipeline(dispMode=dispMode)
    pobj.trplot(T)

def trplot2(T, handle=None, dispMode='VTk'):
    global gRenderer
    if handle is not None:
        if type(handle) is type(gVtk.VtkPipeline()):
            handle.trplot2(T)
        elif type(handle) is type(super(gVtk).Hgtransform()):
            pass  # do Hgtransform stuff
        else:
            pass  # do error stuff
    gobj = gVtk.VtkPipeline(dispMode=dispMode)
    gobj.trplot2(T)

### Implementation Note:
###
### To much detail about a SerialLink or DisplayList has been brought into
### this interface. The Graphics class should just call the appropriate
### Graphics Renderer animate() method and let that class determine how to
### handle the details. See how plot() is handled in Mpl3dArtist.

def animate(obj, stances, 
                 unit='rad', timer_rate=60, gif=None, frame_rate=30, 
                 dispMode='VTK', **kwargs):
    """
    Animates SerialLink object over nx6 dimensional input matrix, with each row representing list of 6 joint angles.
    :param obj: a SerialLink object.
    :param stances: nx6 dimensional input matrix.
    :param unit: unit of input angles. Allowed values: 'rad' or 'deg'
    :param timer_rate: time_rate for motion. Could be any integer more than 1. Higher value runs through stances faster.
    :param gif: name for the written animated GIF image file.
    :param frame_rate: frame_rate for animation.
    :dispMode: display mode; one of ['VTK', 'IPY', 'PIL'].
    :return: null
    """
    global gRenderer
    
    opts = { 'unit'       : unit,
             'timer_rate' : timer_rate,
             'gif'        : gif,
             'frame_rate' : frame_rate,
             'dispMode'   : dispMode,
           }
    
    opt = tbpo.asSimpleNs(opts)
    
    (opt, args) = tbpo.tb_parseopts(opt, **kwargs)
    
    if type(gRenderer) is type(gVtk.VtkPipeline()):
        gobj = gVtk.VtkPipeline(dispMode=opt.dispMode,
                                total_time_steps= stances.shape[0] - 1,
                                timer_rate=opt.timer_rate,
                                gif_file=opt.gif,
                                frame_rate=opt.frame_rate)
        gobj.animate(obj, stances, 
                          unit=opt.unit, frame_rate=opt.frame_rate, gif=opt.gif, 
                          dispMode=opt.dispMode, **args)
    elif type(gRenderer) is type(gMpl.Mpl3dArtist()):
        gobj = gMpl.Mpl3dArtist(1)
        gobj.animate(obj, stances, 
                          unit=opt.unit, frame_rate=opt.frame_rate, gif=opt.gif, 
                          dispMode=opt.dispMode, **args)
    elif type(gRenderer) is type(gIpv.Ipv3dVisual()):
        gobj = gIpv.Ipv3dVisual(1)
        gobj.animate(obj, stances,
                          unit=opt.unit, frame_rate=opt.frame_rate, gif=opt.gif,
                          dispMode=opt.dispMode, **args)

def panimate(pose, other=None, duration=5, timer_rate=60, 
                   gif=None, frame_rate=10, **kwargs):
    global gRenderer
    
    opts = { 'other'      : other,
             'duration'   : duration,
             'timer_rate' : timer_rate,
             'gif'        : gif,
             'frame_rate' : frame_rate,
             'dispMode'   : 'VTK',
           }
    
    opt = tbpo.asSimpleNs(opts)
    
    (opt, args) = tbpo.tb_parseopts(opt, **kwargs)
    
    if type(gRenderer) is type(gVtk.VtkPipeline()):
        gobj = gVtk.VtkPipeline(dispMode=opt.dispMode,
                  total_time_steps=opt.duration*opt.timer_rate,
                  timer_rate = opt.timer_rate,
                  gif_file=opt.gif, 
                  frame_rate=opt.frame_rate)
        gobj.panimate(pose, other=opt.other, duration=opt.duration, **args)
    elif type(gRenderer) is type(gMpl.Mpl3dArtist()):
        gobj = gMpl.Mpl3dArtist(1)
        gobj.panimate(pose, other=opt.other, duration=opt.duration, **args)
    elif type(gRenderer) is type(gIpv.Ipv3dVisual()):
        gobj = gIpv.Ipv3dVisual(1)
        gobj.panimate(pose, other=opt.other, duration=opt.duration, **args)

def qanimate(obj, stances, unit='rad', dispMode='VTK', frame_rate=25, gif=None, **kwargs):
    global gRenderer
    gobj = gVtk.VtkPipeline(dispMode=dispMode)
    gobj.qanimate(obj, stances, unit=unit, frame_rate=frame_rate, gif=gif)
    
def tranimate(obj, stances, unit='rad', dispMode='VTK', frame_rate=25, gif=None, **anim_params):
    global gRenderer
    gobj = gVtk.VtkPipeline(dispMode=dispMode)
    gobj.tranimate(obj, stances, unit=unit, frame_rate=frame_rate, gif=gif, **anim_params)
    
def tranimate2(obj, stances, unit='rad', dispMode='VTK', frame_rate=25, gif=None, **anim_params):
    global gRenderer
    gobj = gVtk.VtkPipeline(dispMode=dispMode)
    gobj.tranimate2(obj, stances, unit=unit, frame_rate=frame_rate, gif=gif, **anim_params)
