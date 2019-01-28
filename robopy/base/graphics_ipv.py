#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: graphics_ipv.py
DATE: Tue Jan 26 08:23:00 2019

@author: garyd
"""

import sys
import pkg_resources
from types import *
from abc import abstractmethod

# RoboPy modules
from robopy.base.tb_parseopts import *
from robopy.base.graphics import Graphics
from robopy.base.display_list import *
from robopy.base.param_geoms import *

from . import check_args
from . import transforms
from . import pose as Pose
from . import serial_link as SerialLink

# To load and handle STL mesh data
from stl import mesh
import copy

# Graphics rendering package
try:
    import ipyvolume.pylab as p3
    import ipyvolume as ipv
except ImportError:
    print("* Error: ipyvolume package required.")
    sys.exit()

import matplotlib as mpl  # for color map
'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
'''
# To produce animated GIFs
###import imageio
from . import images2gif as img2gif

# Support for IPython use in Jupyter Notebooks
# and Spyder IDE
import IPython.display
import PIL.Image

# Numerical packages
import math
import numpy as np

__all__ = ('GraphicsIPV', 'Ipv3dVisual',  # classes
           'rgb_named_colors',)           # functions

###
### Utility routines which do not require Ipv3dVisual class instances.
###

def rgb_named_colors(colors):
        """
        Returns a list of Matplotlib colors.
        :param colors: list of color names supported by Matplotlib
        :return rgb_colors: list of corresponding rgb color values
        """        
        if type(colors) is not list:
            colors = [colors]
            
        rgb_colors = [0] * len(colors)
        for i in range(len(colors)):
            rgb_colors[i] = mpl.colors.to_rgb(colors[i])
            
        return rgb_colors
    
###
### MODULE CLASS DEFINITIONS
###
    
class GraphicsIPV(Graphics):
    """ 
    Graphics rendering interface for the IPV rendering package.
      
    This class acts as the interface between RTB drawing and plotting
    routines and the ipyvolume (IPV) graphics library. Its attributes
    are private and its methods do not require access to RTB manipulator
    modeling object methods and data structures.
    """
    def __init__(self, fig):

        ##super(Graphics, self).__init__()

        # Graphics environment properties
        
        self._dispMode = 'IPY'
        self._fig = fig
        
        # Instantiate a matplotlib pyplot figure.
        
        #self.setFigure()
        #self.setFigureAxes(self.getFigure())
        
        # plotting (graphing) properties

        self.setAxesLimits(-1.5, 1.5, -1.5, 1.5, -1.5, 1.5)

        p3.xlabel('X')
        p3.ylabel('Y')
        p3.zlabel('Z')
        
        # rendered artist properties
        
        self.mesh_list = []  # list of numpy-stl.mesh.Mesh from STL files
        self.poly_list = []  # list of mpl_toolkit.mplot3d.art3d.Poly3DCollection(Mesh.vectors)
        self.item_list = []  # list of items plotted

        self.shapes = ['frame', 'box', 'beam', 'sphere', 
                       'cylinder', 'cone', 'disk', 'plane']
    
    def setGraphicsRenderer(self, gRenderer):
        """ Sets graphic renderer for this IPV 3dVisuals.
        """
        super(GraphicsIPV, self).setGraphicsRenderer(gRenderer)
        
    def setGtransform(self, *args, **kwargs):
        """ Set graphics transform.
        """
        super(GraphicsIPV, self).setGtransform()
              
    ### Class properties and methods
       
    theDispModes = ['VTK','IPY','PIL']
          
    @classmethod
    def isDispMode(cls, dmode):
        return dmode in cls.theDispModes
       
    @staticmethod  # simply call a module scope routine
    def rgb_named_colors(cls, colors):           
        return rgb_named_colors
    
    ### Instance property setters/getters

    """
      _dispMode = property(fset=setDispMode, fget=getDispMode)
      _fig = property(fset=setFigure, fget=getFigure)
      _ax = property(fset=setFigureAxes, fget=getFiguresAxis)
      mesh_list = property(fset=setMeshes, fget=getMeshes, fdel=delMeshes)
      poly_list = property(fset=setPolys, fget=getPolys, fdel=delPolys)
    """
    
    def setDispMode(self, dispmode):
        self._dispMode = dispmode
        
    def getDispMode(self):
        return self._dispMode
    
    def setFigure(self, fign):
        if fign is None:
           self._fig = p3.figure(key=fign, width=480, height=480)

           p3.style.background_color('black')
           p3.style.box_off()
           p3.style.use("dark")

        else:
           self._fig = p3.figure(key=fign)
        
    def getFigure(self):
        return self._fig
    
    def setFigureAxes(self, fig):
        '''
        ##self._ax = fig.add_subplot(111, projection='3d')
        ##self._ax = mplot3d.Axes3D(fig)
        ##self._ax.view_init(elev=2.0, azim=-35.0)  # a hardcoded dev convenience
        ##self._ax.set_frame_on(b=True)
        '''
        p3.view(0.0, -120.0)
        self._ax = fig
        
    def getFigureAxes(self):
        return self._ax
    
    def setAxesLimits(self, xlim, *args):
        if (type(xlim) is list) and len(xlim) == 6:
            [xmin, xmax, ymin, ymax, zmin, zmax] = xlim[:]
        elif len(args) == 5:
            xmin = xlim
            [xmax, ymin, ymax, zmin, zmax] = args[:]
        else:
            return  # no warning given

        p3.xlim(xmin, xmax)
        p3.ylim(ymin, ymax)
        p3.zlim(zmin, zmax)
        self._axesLimits = [xmin, xmax, ymin, ymax, zmin, zmax]
    
    def getAxesLimits(self):
        return self._axesLimits
    
    def setMeshes(self, meshes):
        self.mesh_list = meshes
        
    def setMeshI(self, i, mesh):
        if i in range(len(self.mesh_list)):
            self.mesh_list[i] = mesh
            
    def getMeshes(self):
        return self.mesh_list
    
    def getMeshI(self, i):
        if i in range(len(self.mesh_list)):
            return self.mesh_list[i]
        
    def delMeshes(self):
        self.mesh_list = []
        
    def addMeshes(self, meshes):
        self.mesh_list.append(meshes)
        
    def setPolys(self, polys):
        self.poly_list = polys
        
    def setPolyI(self, i, poly):
        if i in range(len(self.poly_list)):
            self.poly_list[i] = poly
    
    def getPolys(self):
        return self.poly_list
    
    def getPolyI(self, i):
        if i in range(len(self.poly_list)):
            return self.poly_list[i]
        
    def delPolys(self):
        self.poly_list = []
 
    def addPolys(self, polys):
        self.poly_list.append(polys)
        
    ### Class methods (presented by functional group)
        
    ## Plot elements methods
    

    def plot_parametric_shape(self, shape, solid=False, Tr=np.eye(4), **opts):
        """ Plot specified parametric shape
        """

        # create parametric shape xyz coordinate arrays

        (x, y, z) = param_xyz_coord_arrays(shape, **opts)

        c = 'k'  # black
        if 'c' in opts:
           c = opts['c']

        # apply homogeneous transform to xyz coordinate arrays

        (xr, yr, zr) = self.shape_xform(x, y, z, Tr)

        # plot the transformed xyz coordinate arrays as meshes

        ax = self.getFigureAxes()

        if shape == 'frame':
            tail = 0
            head = 1
            vxr = xr[head,:] - xr[tail,:]
            vyr = yr[head,:] - yr[tail,:]
            vzr = zr[head,:] - zr[tail,:]
            ax.quiver(xr[tail,:], yr[tail,:], zr[tail,:],
                      vxr[:], vyr[:], vzr[:], 
                      arrow_length_ratio=0.1, normalize=False, color='k')
            ax.text3D(xr[head,0], yr[head,0], zr[head,0], 'X', ha='left', va='center', color='r')
            ax.text3D(xr[head,1], yr[head,1], zr[head,1], 'Y', ha='left', va='center', color='g')
            ax.text3D(xr[head,2], yr[head,2], zr[head,2], 'Z', ha='left', va='center', color='b')
        elif shape in ['box', 'beam']:
            if solid:
               ax.plot_surface(xr, yr, zr, rstride=1, cstride=5, color=c)
            else:
               ax.plot_wireframe(xr, yr, zr, rstride=1, cstride=5, color=c)
        else:
            if solid:
               ax.plot_surface(xr, yr, zr, rstride=1, cstride=1, color=c)
            else:
               ax.plot_wireframe(xr, yr, zr, rstride=1, cstride=1, color=c)

    @staticmethod
    def shape_xform(x, y, z, Tr):
        """ Shape coordinates transformation
        """
        # get dimensions of parametric space (assumed square)
        dim = x.shape[0]

        # pack homogeneous shape coordinates
        xyz1 = np.vstack([x.reshape((1,dim*dim)), 
                          y.reshape((1,dim*dim)),
                          z.reshape((1,dim*dim)),
                          np.ones((1,dim*dim))])

        # apply transform to packed shape coordinates
        Vtr = np.dot(Tr, xyz1)
        """ NumPy matrix type work with Matplotlib's plot routines, but not ipyvolume's.
            xr = Vtr[0,:].reshape((dim,dim))
            yr = Vtr[1,:].reshape((dim,dim))
            zr = Vtr[2,:].reshape((dim,dim))
        """
        xr = np.asarray(Vtr[0,:].reshape((dim,dim)))
        yr = np.asarray(Vtr[1,:].reshape((dim,dim)))
        zr = np.asarray(Vtr[2,:].reshape((dim,dim)))

        return (xr, yr, zr)
    
    def draw_axes2(self, *args, **kwargs):
        """ Graphics package draw plot axes for 2D space.
        """ 
        print("* Not yet implemented.")
        return None
        
    def draw_axes3(self, *args, **kwargs):
        """ Graphics package draw plot axes for 3D space.
        """ 
        print("* Not yet implemented.")
        return None
        
    def draw_cube(self):
        (x, y, z) = parametric_box(1.0, 5)
        self.getFigureAxes().plot_surface(x, y, z, rstride=1, cstride=1, color='b')
    
    def draw_sphere(self):
        (x, y, z) = parametric_sphere(1.0, 32)
        self.getFigureAxes().plot_surface(x, y, z, rstride=1, cstride=1, color='r')
    
    ### Rendering viewpoint methods

    ### ...
    
    ### Animation display methods
    
    def render(self, ui=True):
        """
        Renderers current artists in ready render window.
        """
        print("* Not yet implemented.")
        return None
    
    def mpl_animate(self, *args, **kwargs):
        """
        Creates animation of current actors in ready render window.
        """
        raise NotImplementedError('Need to define animate method.')

    def show(self, *args):
        if len(args) > 0:
            p3.show(extra_widgets=args)
        else:
            p3.show()

    def clear(self):
        p3.clear()

    def close(self):
        p3.close()

    ### Abstract methods for RTB interface
    
    @abstractmethod
    def view(self, *args, **kwargs):
        raise NotImplementedError('Need to define view method.')
        
    @abstractmethod
    def animate(self, *args, **kwargs):
        raise NotImplementedError('Need to define animate method.')

    @abstractmethod
    def fkine(*args, **kwargs):
        raise NotImplementedError('Need to define fkine method.')

    @abstractmethod
    def plot(self, *args, **kwargs):
        raise NotImplementedError('Need to define plot method!')

    @abstractmethod
    def qplot(self, *args, **kwargs):
        raise NotImplementedError('Need to define qplot method.')
    
    @abstractmethod
    def trplot(self, *args, **kwargs):
        raise NotImplementedError('Need to define trplot method.')
    
    @abstractmethod    
    def trplot2(self, *args, **kwargs):
        raise NotImplementedError('Need to define trplot2 method.')
    
    @abstractmethod
    def tranimate(self, *args, **kwargs):
        raise NotImplementedError('Need to define tranimate method.')
        
    @abstractmethod
    def tranimate2(self, *args, **kwargs):
        raise NotImplementedError('Need to define tranimate2 method.')

    # DisplayList rendering, plotting and animation methods

    def renderDisplayListItem(self, item):
        if item.type == 'surface':
            data = item.xform()  # get the transformed coordinates
            x = data[0].reshape((1, data[0].shape[0], data[0].shape[1]))
            y = data[1].reshape((1, data[1].shape[0], data[1].shape[1]))
            z = data[2].reshape((1, data[2].shape[0], data[2].shape[1]))
            if item.gentity is None:
                item.gentity =  [np.ndarray((1, data[0].shape[0], data[0].shape[1])),
                                 np.ndarray((1, data[1].shape[0], data[1].shape[1])),
                                 np.ndarray((1, data[2].shape[0], data[2].shape[1]))]
                item.gentity[0] = x
                item.gentity[1] = y
                item.gentity[2] = z
            else:
                item.gentity = (np.vstack((item.gentity[0], x)),
                                np.vstack((item.gentity[1], y)),
                                np.vstack((item.gentity[2], z)))
            self.item_list.append(item)  # save each item plotted
        elif item.type == 'command':
            eval(item.command, globals())  # eval the command in global context
        elif item.type == 'line':
            # TODO
            pass

    def renderDisplayList(self, displayList):
        ### print("renderDisplayList")
        for item in displayList:
            self.renderDisplayListItem(item)

    def plotDisplayList(self, dList, dispMode='IPY', **kwargs):
        """
        Plots the DisplayList graphic entities.
        :param dList: a DisplayList object
        :param: dispMode: display mode, one of ['VTK', 'IPY', 'PIL'].
        :return: None.
        """
        # parse argument list options
        opts = {'dispMode': dispMode,  # holdover from GraphicsVTK
                'z_up': True,          # holdover from GraphicsVTK
                'limits': self.getAxesLimits(),
                }

        opt = asSimpleNs(opts)

        (opt, args) = tb_parseopts(opt, **kwargs)

        self.setAxesLimits(opt.limits)
        self.renderDisplayList(dList)

        # plot surface on the same figure axes as in MATLAB with 'hold on'
        S = []
        for item in self.item_list:
            (x, y, z) = item.gentity
            if item.type == "surface":
                S.append(ipv.plot_surface(x, y, z, **item.args))

        self.show()

    ### Implementation Note:
    ###
    ### Use of transFunc as FunctionType is merely a development convenience and
    ### its type could also be np.matrix, where each column would associate with
    ### a 'surface' or 'line' item in the DisplayList just as columns of stances
    ### passed to animateSerialLink associate with joints in a SerialLink.

    def animateDisplayList(self, displayList, transFunc, unit='rad', gif=None,
                                 duration=5.0, frame_rate=30, **kwargs):
        """
        Animates DisplayList object through transformations as a function of time.
        :param transFunc: homogeneous transformation function of the form Tr(time)
        :param duration: duration of animation in seconds
        :param unit: unit of input angles. Allowed values: 'rad' or 'deg'
        :param gif: name for the written animated GIF image file.
        :param frame_rate: frame_rate for animation.
        :return: None
        """
        # parse argument list options
        opts = {'unit'      : unit,                  # holdover from animateSerialLink
                'gif'       : gif,                   # holdover from GraphicsVTK
                'duration'  : duration,
                'frame_rate': frame_rate,
                'dispMode'  : self.getDispMode(),    # holdover from GraphicsVTK
                'z_up'      : False,                 # holdover from GraphicsVTK
                'limits'    : self.getAxesLimits(),
                }

        opt = asSimpleNs(opts)

        (opt, args) = tb_parseopts(opt, **kwargs)

        # verify transFunc
        assert type(transFunc) is FunctionType

        self.setAxesLimits(opt.limits)

        # calculate framing timing parameters
        tstep = 1.0 / opt.frame_rate
        nframes = int(opt.duration * opt.frame_rate) + 1

        displayList.reset()

        # render remaining frames
        for n in range(0, nframes):
            # update time
            t = n * tstep
            # update display list item's transforms
            Tr = np.asarray(transFunc(t))
            for item in displayList:
                item.transform = np.dot(item.transform, Tr)
            # clear plotted items list
            self.item_list.clear()
            # render display list graphics entities
            self.renderDisplayList(displayList)

        S = []
        for item in self.item_list:
            (x, y, z) = item.gentity
            if item.type == "surface":
                S.append(ipv.plot_surface(x, y, z, **item.args))

        frame_step_msec = int(1000.0 / opt.frame_rate)

        self.HBox = p3.animation_control(S,sequence_length=nframes,
                                           interval=frame_step_msec)

        # initiate display list animation
        self.show()


### Implementation Note:
###
### Some components of this class still exhibit non-traditional coupling
### between graphics providers and clients due to preservation of existing
### RoboPy code base. This coupling can be mitigated or eliminated in some
### instances by utilizing callback mechanisms as done in most graphical
### rendering and user interface toolkits. A specific example would be the
### RTB fkine function that should be passed to animateSerialLink() method
### as a callback routine as one would pass animation update functions to
### an animator, or keypress and mouse event handlers to a GUI manager.

class Ipv3dVisual(GraphicsIPV):
    """
    ipyvolume (IPV) rendering visuals for RTB plotting and animation.
     
    This class acts as the interface between RTB plotting and animation
    routines and the RTB manipulator modeling and simulation code.
    Its methods must have access to the RTB manipulator model object
    methods and data structures.
    """
    def __init__(self, *args):
        
        if len(args) < 1 :  # crude method for handling type tests
            return None

        ### fignums = plt.get_fignums() # Matplotlib specific
        fignums = []

        if fignums != [] \
            and args[0] in fignums :
            # use existing figure
            self.setFigure(args[0])   ### Developers's convenience
            ### self.setFigure(None)  ### User's convenience

        else:
            self.setFigure(None)

        self.setFigureAxes(self.getFigure())
        
        super(Ipv3dVisual, self).__init__(self.getFigure())

        return None
    
    def getAxesLimits(self):
        return super(Ipv3dVisual, self).getAxesLimits()
    
    ### Class methods
    ###
    
    def draw_cube(self):
        super(Ipv3dVisual, self).draw_cube()
        
    def draw_sphere(self):
        super(Ipv3dVisual, self).draw_sphere()
    
    ### Plotting methods
    
    def view(self, *args, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def pose_plot2(self, pose, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def pose_plot3(self, pose, **kwargs):
        print("* Not yet implemented.")
        return None
        
    def plot(self, obj, **kwargs):
        if type(obj) in [type(Pose.SO2()), type(Pose.SE2())]:
            self.pose_plot2(obj, **kwargs)
        elif type(obj) in [type(Pose.SO3()), type(Pose.SE3())]:
            self.pose_plot3(obj, **kwargs)
        elif type(obj) is type(DisplayList()):
            self.plotDisplayList(obj, **kwargs)
        else:
            pass

    def animate(self, obj, stances, **kwargs):
        if isinstance(obj, SerialLink.SerialLink):
            self.animateSerialLink(obj, stances, **kwargs)
        elif isinstance(obj, DisplayList):
            self.animateDisplayList(obj, stances, **kwargs)
        else:
            pass
        
    @staticmethod
    def fkine(obj, stances, unit='rad', apply_stance=False, mesh_list=None, timer=None):
        """
        Calculates forward kinematics for array of joint angles.
        :param stances: stances is a mxn array of joint angles.
        :param unit: unit of input angles (rad)
        :param apply_stance: If True, then applied to actor_list.
        :param mesh_list: list of meshes for given SerialLink object
        :param timer: used only (for animation).
        :return T: list of n+1 homogeneous transformation matrices.
        """
            
        T = obj.fkine(stances, unit=unit, timer=timer)
        
        if apply_stance and mesh_list is not None \
                        and len(mesh_list) >= len(T):
            for i in range(0,len(T)):
                mesh_list[i].transform(T[i])
                
        return T
    
    def _setup_mesh_objs(self, obj):   
        """
        Internal function to initialise mesh objects.
        :return: mesh_list, poly_list
        """
        mesh_list = []
        poly_list = []
        '''
        ### Plotting STL meshes requires matplotlib.plot3d
        mesh_list = [0] * len(obj.stl_files)
        poly_list = [0] * len(obj.stl_files)
        for i in range(len(obj.stl_files)):
            loc = pkg_resources.resource_filename("robopy", '/'.join(('media', obj.name, obj.stl_files[i])))
            a_mesh = mesh.Mesh.from_file(loc)
            a_poly = mplot3d.art3d.Poly3DCollection(a_mesh.vectors)
            a_poly.set_facecolor(obj.colors[i])  # (R,G,B)
            a_poly.set_rasterized(True)
            a_poly.set_zorder(2.0)
            mesh_list[i] = a_mesh
            poly_list[i] = a_poly
        '''

        loc = pkg_resources.resource_filename("robopy", "/media/stl/floor/white_tiles.stl")
        white_tiles = mesh.Mesh.from_file(loc)
        loc = pkg_resources.resource_filename("robopy", "/media/stl/floor/green_tiles.stl")
        green_tiles = mesh.Mesh.from_file(loc)
        
        return (mesh_list, poly_list, white_tiles, green_tiles)
    
    ### Stub for pose rendered as stick figure.
    def _render_stick_pose(self, obj, stance, unit, **kwargs):
        """
        Renders given SerialLink object as stick figure desired in stance.
        :param obj: a SerialLink object.
        :param stance: list of joint angles for SerialLink object.
        :param unit: unit of input angles.
        :return: None.
        """ 
        pass
    
    ### Stub for pose rendered as notional body solids. 
    def _render_body_pose(self, obj, stance, unit, **kwargs):
        """
        Renders given SerialLink object as notional body solids in desired stance.
        :param obj: a SerialLink object.
        :param stance: list of joint angles for SerialLink object.
        :param unit: unit of input angles.
        :return: None.
        """ 
        pass
    
    ### Implementation Note:
    ###
    ### Rendering environment objects should be decoupled from rendering
    ### pose objects.
    
    def _render_body_floor(self, obj, limits):
        """ Render floor as paramatric plane surface
        """
        ### NOTE: cannot do hidden surface plots with parametric shapes
        
        # get floor's position
        position = np.asarray(obj.param.get("floor_position")).flatten()
        
        # plot floor plane
        s = math.fabs(limits[1] - limits[0])  # assumes square plane
        h = position[1]
        params = {'s':s, 'h':h, 'c':'lightgrey'}
        self.plot_parametric_shape('plane', solid=True, Tr=np.eye(4), **params)
        params = {'s':s, 'h':h, 'c':'black'}
        self.plot_parametric_shape('plane', solid=False, Tr=np.eye(4), **params)

    def _render_stl_floor(self, obj, white_tiles, green_tiles):
        """ Render floow as white and green STL mesh tiles.
        """
        ### NOTE: cannot do hidden surface plots with poly3D collections
        
        # get floor's position
        position = np.asarray(obj.param.get("floor_position")).flatten()
        
        # render floor tiles

        '''
        ### plotting STL meshes requires mplot3d
        white_tiles.z += position[1]
        a_poly = mplot3d.art3d.Poly3DCollection(white_tiles.vectors)
        a_poly.set_facecolor("white")
        a_poly.set_edgecolor("white")
        a_poly.set_rasterized(True)
        a_poly.set_zorder(1.0)
        self.getFigureAxes().add_collection3d(a_poly)
        
        green_tiles.z += position[1]
        a_poly = mplot3d.art3d.Poly3DCollection(green_tiles.vectors)
        a_poly.set_facecolor("green")
        a_poly.set_edgecolor("green")
        a_poly.set_rasterized(True)
        a_poly.set_zorder(1.0)
        self.getFigureAxes().add_collection3d(a_poly)
        '''
    def _render_stl_pose(self, obj, stance, unit, limits=None):
        """
        Renders given SerialLink object defined as STL meshes in desired stance.
        :param obj: a SerialLink object.
        :param stance: list of joint angles for SerialLink object.
        :param unit: unit of input angles.
        :param limits; plot x, y, z limits
        :return: tuple = (limits, mesh_list, mesh_poly3d)  # used for animation
        """                
        # load SerialLink mesh definition from STL files.
        (mesh_list, poly_list, white_tiles, green_tiles) = self._setup_mesh_objs(obj)

        self.setMeshes(copy.deepcopy(mesh_list))
        self.setPolys(poly_list)
        
        # if necessary, apply plot axes limits
        if limits is None:
            # NOTE: adjust for VTK world coordinate system with Y-axis up
            xlims = np.asarray(obj.param.get("cube_axes_x_bounds")).flatten()
            ylims = np.asarray(obj.param.get("cube_axes_y_bounds")).flatten()
            zlims = np.asarray(obj.param.get("cube_axes_z_bounds")).flatten()
            limits = [zlims[0], zlims[1], xlims[0], xlims[1], ylims[0], ylims[1]]
            
        self.setAxesLimits(limits)
        
        # render floor
        self._render_stl_floor(obj, white_tiles, green_tiles)
            
        # apply stance to reference pose
        self.fkine(obj, stance, unit=unit, apply_stance=True, 
                   mesh_list=self.getMeshes())
        
        # render SerialLink object; save and return poly3d artists
        mesh_poly3d = []
        '''
        ### Plotting STL meshes requires mplotlib.mplot3d
        for i in range(0, len(self.getMeshes())):
            a_mesh = self.getMeshI(i)
            a_mesh.rotate([1.,0.,0.], -np.pi/2)
            a_poly = mplot3d.art3d.Poly3DCollection(a_mesh.vectors)
            a_poly.set_facecolor(obj.colors[i])
            a_poly.set_rasterized(True)
            a_poly.set_zorder(2.0)
            self.setPolyI(i, a_poly)
            self.getFigureAxes().add_collection3d(a_poly)
            mesh_poly3d.append(a_poly)
        '''
        # preserve reference pose
        self.setMeshes(copy.deepcopy(mesh_list))
        
        return(limits, mesh_list, mesh_poly3d)

    def qplot(self, obj, stance, unit='rad', dispMode='IPY', **kwargs):
        """
        Plots the SerialLink object in a desired stance.
        :param stance: list of joint angles for SerialLink object.
        :param unit: unit of input angles.
        :param: dispMode: display mode, one of ['VTK', 'IPY', 'PIL'].
        :return: None.
        """
        # parse argument list options
        opts = { 'unit'     : unit,
                 'dispMode' : dispMode,  # holdover from GraphicsVTK
                 'z_up'     : False,     # holdover from GraphicsVTK
                 'limits'   : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        # verify stance type
        assert type(stance) is np.matrix

        # check for stance angle unit conversion
        if opt.unit == 'deg':
            stance = stance * (np.pi / 180)
            opt.unit = 'rad'
        
        self._render_stl_pose(obj, stance, opt.unit, limits=opt.limits)
         
        # Display pose
        
        self.show()        
    
    def trplot(self, *args, **kwargs):
        print("* Not yet implemented.")
        return None
       
    def trplot2(self, *args, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def animateSerialLink(self, obj, stances, unit='rad', gif=None, frame_rate=25, **kwargs):
        """
        Animates SerialLink object over mx6 dimensional input matrix, with each row representing list of 6 joint angles.
        :param stances: mx6 dimensional input matrix.
        :param unit: unit of input angles. Allowed values: 'rad' or 'deg'
        :param gif: name for the written animated GIF image file.
        :param frame_rate: frame_rate for animation.
        :return: None
        """       
        # parse argument list options
        opts = { 'unit'       : unit,
                 'gif'        : gif,                 # holdover from GraphicsVTK
                 'frame_rate' : frame_rate,
                 'dispMode'   : self.getDispMode(),  # holdover from GraphicsVTK
                 'z_up'       : False,               # holdover from GraphicsVTK
                 'limits'     : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        # verify stance type
        assert type(stances) is np.matrix
        
        # check for stance angle unit conversion
        if opt.unit == 'deg':
            stances = stances * (np.pi / 180)
            opt.unit = 'rad'
        
        # Plot initial pose stance
        (limits, mesh_list, mesh_poly3d) = self._render_stl_pose(obj, stances, opt.unit, limits=opt.limits)
        
        # define text3D artist for rendered frame time display
        tx = limits[1]*1.2
        ty = limits[2]*1.2
        tz = limits[5]*1.2
        time_text = self.getFigureAxes().text3D(tx, ty, tz, '', ha='center', va='bottom')
        anim_text3d = time_text        

        # set animation parameters, then instantiate an animator
        nframes = stances.shape[0]
        fps = opt.frame_rate
        frame_step_msec = 1000.0 / opt.frame_rate

        self.HBox = p3.animation_control([], sequence_length=nframes,
                                             interval=frame_step_msec)

        # initiate pose animation
        
        self.show()

        return None
    
    def panimate(self, obj, stances, unit='rad', frame_rate=25, gif=None, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def qanimate(self, obj, stances, unit='rad', frame_rate=25, gif=None, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def tranimate(self, T, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def tranimate2(self, R, **kwargs):
        print("* Not yet implemented.")
        return None