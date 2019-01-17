#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: graphics_mpl.py
DATE: Tue Jan  9 11:53:00 2019

@author: garyd
"""

import sys
import pkg_resources
from abc import abstractmethod

# RoboPy modules
from robopy.base.tb_parseopts import *
from robopy.base.graphics import Graphics
from . import check_args
from . import transforms
from . import pose as Pose
from . import serial_link as SerialLink

# To load and handle STL mesh data
from stl import mesh
import copy

# Graphics rendering package
try:
    import matplotlib as mpl
except ImportError:
    print("* Error: matplotlib package required.")
    sys.exit()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

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

__all__ = ('GraphicsMPL', 'Mpl3dArtist',
           'rgb_named_colors')

###
### Utility routines which do not require Mpl3dArtist class instances.
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
    
class GraphicsMPL(Graphics):
    """ 
    Graphics rendering interface for the MPLrendering package.
      
    This class acts as the interface between RTB drawing and plotting
    routines and the Matplotlib (MPL) graphics library. Its attributes
    are private and its methods do not require access to RTB manipulator
    modeling object methods and data structures.
    """
    def __init__(self, fig):
                
        # Graphics environment properties
        
        self._dispMode = 'IPY'
        self._fig = fig
        
        # Instantiate a matplotlib pyplot figure.
        
        #self.setFigure()
        #self.setFigureAxis(self.getFigure())
        
        # plotting (graphing) properties
        
        self.getFigureAxis().set_aspect("equal")
        self.setAxesLimits(-1.5, 1.5, -1.5, 1.5, -1.5, 1.5)
        self.getFigureAxis().set_xlabel('X')
        self.getFigureAxis().set_ylabel('Y')
        self.getFigureAxis().set_zlabel('Z')
        
        # rendered artist properties
        
        self.mesh_list = []
        self.poly_list = []

        self.shapes = ['frame', 'box', 'beam', 'sphere', 
                       'cylinder', 'cone', 'disk', 'plane']
        return None
    
    def setGraphicsRenderer(self, gRenderer):
        """ Sets graphic renderer for this MPL 3dArtists.
        """
        super(GraphicsMPL, self).setGraphicsRenderer(gRenderer)
        
    def setGtransform(self, *args, **kwargs):
        """ Set graphics transform.
        """
        super(GraphicsMPL, self).setGtransform()
              
    ### Class properties and methods
       
    theDispModes = ['VTK','IPY','PIL']
          
    @classmethod
    def isDispMode(cls, dmode):
        return dmode in theDispModes 
       
    @staticmethod  # simply call a module scope routine
    def rgb_named_colors(cls, colors):           
        return rgb_named_colors
    
    ### Instance property setters/getters
    
    """
      _dispMode = property(fset=setDispMode, fget=getDispMode)
      _fig = property(fset=setFigure, fget=getFigure)
      _ax = property(fset=setFigureAxis, fget=getFiguresAxis)
      mesh_list = property(fset=setMeshes, fget=getMeshes, fdel=delMeshes)
      poly_list = property(fset=setPolys, fget=getPolys, fdel=delPolys)
    """
    
    def setDispMode(self, dispmode):
        self._dispMode = dispmode
        
    def getDispMode(self):
        return self._dispMode
    
    def setFigure(self):
        self._fig = plt.figure(figsize=(6,6), dpi=80)
        
    def getFigure(self):
        return self._fig
    
    def setFigureAxis(self, fig):
        self._ax = fig.add_subplot(111, projection='3d')
        ###self._ax = mplot3d.Axes3D(fig)
        self._ax.view_init(elev=2.0, azim=-35.0)  # a hardcoded dev convenience
        self._ax.set_frame_on(b=True)
        
    def getFigureAxis(self):
        return self._ax
    
    def setAxesLimits(self, xlim, *args):
        if (type(xlim) is list) and len(xlim) == 6:
            [xmin, xmax, ymin, ymax, zmin, zmax] = xlim[:]
        elif len(args) == 5:
            xmin = xlim
            [xmax, ymin, ymax, zmin, zmax] = args[:]
        else:
            return  # no warning given

        # Assume x and y ranges are equal, but z's range may be less
        self.getFigureAxis().set_aspect('auto')
        scale = math.fabs(xmax-xmin)/math.fabs(zmax-zmin)
        self.getFigureAxis().auto_scale_xyz(1.0, 1,0, scale)
        
        self.getFigureAxis().set_xlim([xmin, xmax])
        self.getFigureAxis().set_ylim([ymin, ymax])
        self.getFigureAxis().set_zlim([zmin, zmax])
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
    
    @staticmethod
    def parametric_frame(s):
        """ Parametric Cartesian coordinate frame
        """
        x = s * np.asmatrix([[0.0, 0.0, 0.0],[1.0, 0.0, 0.0],[0.0, 0.0, 0.0]])
        y = s * np.asmatrix([[0.0, 0.0, 0.0],[0.0, 1.0, 0.0],[0.0, 0.0, 0.0]])
        z = s * np.asmatrix([[0.0, 0.0, 0.0],[0.0, 0.0, 1.0],[0.0, 0.0, 0.0]])
        return (x, y, z)

    @staticmethod
    def parametric_box(s):
        """ Parametric box shape
        """
        r = s*np.sqrt(2.0)/2.
        h = s/2.
        u = np.linspace(0.25*np.pi, 2.25*np.pi, 5)
        v = np.linspace(-1.0, 1.0, 5)
        x = r * np.outer(np.cos(u), np.ones(np.size(v)))
        y = r * np.outer(np.sin(u), np.ones(np.size(v)))
        z = h * np.outer(np.ones(np.size(u)), v)
        return (x, y, z)

    @staticmethod
    def parametric_beam(d, l):
        """ Parametric beam shape
        """
        r = d*np.sqrt(2.0)/2.
        h = l/2.
        u = np.linspace(0.25*np.pi, 2.25*np.pi, 5)
        v = np.linspace(-1.0, 1.0, 5)
        x = r * np.outer(np.cos(u), np.ones(np.size(v)))
        y = r * np.outer(np.sin(u), np.ones(np.size(v)))
        z = h * np.outer(np.ones(np.size(u)), v)
        return (x, y, z)

    @staticmethod
    def parametric_sphere(d, dim):
        """ Parametric sphere shape
        """
        r = d/2.
        u = np.linspace(0.0, 2*np.pi, dim)
        v = np.linspace(0.0, np.pi, dim)
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        return (x, y, z)

    @staticmethod
    def parametric_cylinder(d, l, dim):
        """ Parametric cylinder shape
        """
        r = d/2.
        h = l/2.
        u = np.linspace(0.0, 2*np.pi, dim)
        v = np.linspace(-1.0, 1.0, dim)
        x = r * np.outer(np.cos(u), np.ones(np.size(v)))
        y = r * np.outer(np.sin(u), np.ones(np.size(v)))
        z = h * np.outer(np.ones(np.size(u)), v)
        return (x, y, z)

    @staticmethod
    def parametric_cone(d0, d1, l, dim):
        """ Parametric cone shape
        """
        r0 = d0/2.
        r1 = d1/2.
        f  = (r1-r0)/2.
        h  = l/2
        u  = np.linspace(0.0, 2*np.pi, dim)
        v  = np.linspace(-1.0, 1.0, dim)
        s  = r0 + f*(v+1.0)
        x  = s * np.outer(np.cos(u), np.ones(np.size(v)))
        y  = s * np.outer(np.sin(u), np.ones(np.size(v)))
        z  = h * np.outer(np.ones(np.size(u)), v)
        return (x, y, z)

    @staticmethod
    def parametric_disk(d, h, dim):
        """ Parametric disk shape
        """
        r = d/2.
        u = np.linspace(0.0, 2*np.pi, dim)
        v = np.linspace(0.0, 1.0, dim)
        x = r * np.outer(np.cos(u), v)
        y = r * np.outer(np.sin(u), v)
        z = h * np.outer(np.ones(np.size(u)), np.ones(np.size(v)))
        return (x, y, z)

    @staticmethod
    def parametric_plane(s, h, dim):
        """ Parametric plane shape
        """
        r = s/2.
        u = np.linspace(-1.0, 1.0, dim)
        v = np.linspace(-1.0, 1.0, dim)
        x = r * np.outer(u, np.ones(np.size(v)))
        y = r * np.outer(np.ones(np.size(u)), v)
        z = h * np.outer(np.ones(np.size(u)), np.ones(np.size(v)))
        return (x, y, z)

    def plot_parametric_shape(self, shape, solid=False, Tr=np.eye(4), **opts):
        """ Plot specified parametric shape
        """
        if shape == 'frame':
            dim = 3
        elif shape in ['box', 'beam']:
            dim = 5
        elif shape in ['sphere', 'cylinder', 'cone', 'disk', 'plane']:
            dim = 32
        else:
            print("*** error: invalid specified shape %s" % shape)
            print("           must be %s" % self.shapes)
            return

        # create parametric shape coordinates
        if shape == 'frame':
            s = 1.0
            if 's' in opts: s = opts['s']
            (x, y, z) = self.parametric_frame(s)
        elif shape == 'box':
            s = 1.0
            if 's' in opts: s = opts['s']
            (x, y, z) = self.parametric_box(s)
        elif shape == 'beam':
            d = 1.0
            if 'd' in opts: d = opts['d']
            l = 1.0
            if 'l' in opts: l = opts['l']
            (x, y, z) = self.parametric_beam(d, l)
        elif shape == 'sphere':
            d = 1.0
            if 'd' in opts: d = opts['d']
            (x, y, z) = self.parametric_sphere(d, dim)
        elif shape == 'cylinder':
            d = 1.0
            if 'd' in opts: d = opts['d']
            l = 1.0
            if 'l' in opts: l = opts['l']
            (x, y, z) = self.parametric_cylinder(d, l, dim)
        elif shape == 'cone':
            d0 = 1.0
            if 'd0' in opts: d0 = opts['d0']
            d1 = 0.5
            if 'd1' in opts: d1 = opts['d1']
            l  = 1.0
            if 'l' in opts: l = opts['l']
            (x, y, z) = self.parametric_cone(d0, d1, l, dim)
        elif shape == 'disk':
            d = 1.0
            if 'd' in opts: d = opts['d']
            h = 0.0
            if 'h' in opts: h = opts['h']
            (x, y, z) = self.parametric_disk(d, h, dim)
        elif shape == 'plane':
            s = 1.0
            if 's' in opts: s = opts['s']
            h = 0.0
            if 'h' in opts: h = opts['h']
            (x, y, z) = self.parametric_plane(s, h, dim)

        c = 'k'
        if 'c' in opts:
           c = opts['c']

        (xr, yr, zr) = self.shape_xform(x, y, z, Tr)

        ax = self.getFigureAxis()

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
               ax.plot_surface(xr, yr, zr, rstride=4, cstride=4, color=c)
            else:
               ax.plot_wireframe(xr, yr, zr, rstride=4, cstride=4, color=c)

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
        (x, y, z) = self.parametric_box(1.0, 5)
        self.getFigureAxis().plot_surface(x, y, z, rstride=1, cstride=1, color='b')
    
    def draw_sphere(self):
        (x, y, z) = self.parametric_sphere(1.0, 32)
        self.getFigureAxis().plot_surface(x, y, z, rstride=4, cstride=4, color='r')
    
    ### Rendering viewpoint methods
        
    
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

    def show(self):
        plt.show(block=True)
    
    def close(self):
        plt.close()

    ### Abstract methods
    
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
        
        
class Mpl3dArtist(GraphicsMPL):
    """ Matplotlib (MPL) rendering artists for RTB plotting and animation.
     
        This class acts as the interface between RTB plotting and animation
        routines and the RTB manipulator modeling and simulation code.
        Its methods must have access to the RTB manipulator model object
        methods and data structures.
    """
    def __init__(self, *args):
        
        if len(args) < 1 :  # crude method for handling type tests
            return None
        
        mpl.style.use('dark_background')
        
        self.setFigure()
        self.setFigureAxis(self.getFigure())
        
        super(Mpl3dArtist, self).__init__(self.getFigure())
        
        return None
    
    def getAxesLimits(self):
        return super(Mpl3dArtist, self).getAxesLimits()
    
    ### Class methods
    ###
    
    def draw_cube(self):
        super(Mpl3dArtist, self).draw_cube()
        
    def draw_sphere(self):
        super(Mpl3dArtist, self).draw_sphere()
    
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
        else:
            pass
        
    @staticmethod
    def fkine(obj, stances, unit='rad', apply_stance=False, mesh_list=None, timer=None):
        """
        Calculates forward kinematics for array of joint angles.
        :param stances: stances is a mxn array of joint angles.
        :param unit: unit of input angles (rad)
        :param apply_stance: If True, then applied tp actor_list.
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
        mesh_list = [0] * len(obj.stl_files)
        poly_list = [0] * len(obj.stl_files)
        for i in range(len(obj.stl_files)):
            loc = pkg_resources.resource_filename("robopy", '/'.join(('media', obj.name, obj.stl_files[i])))
            a_mesh = mesh.Mesh.from_file(loc)
            a_poly = mplot3d.art3d.Poly3DCollection(a_mesh.vectors)
            a_poly.set_facecolor(obj.colors[i])  # (R,G,B)
            mesh_list[i] = a_mesh
            poly_list[i] = a_poly
            
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
        
        white_tiles.z += position[1]
        a_poly = mplot3d.art3d.Poly3DCollection(white_tiles.vectors)
        a_poly.set_facecolor("white")
        a_poly.set_edgecolor("white")
        self.getFigureAxis().add_collection3d(a_poly)
        
        green_tiles.z += position[1]
        a_poly = mplot3d.art3d.Poly3DCollection(green_tiles.vectors)
        a_poly.set_facecolor("green")
        a_poly.set_edgecolor("green")
        self.getFigureAxis().add_collection3d(a_poly)
    
    def _render_stl_pose(self, obj, stance, unit, limits=None):
        """
        Renderes given SerialLink object defined as STL meshes in desired stance.
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
        for i in range(0, len(self.getMeshes())):
            a_mesh = self.getMeshI(i)
            a_mesh.rotate([1.,0.,0.], -np.pi/2)
            a_poly = mplot3d.art3d.Poly3DCollection(a_mesh.vectors)
            a_poly.set_facecolor(obj.colors[i])
            self.setPolyI(i, a_poly)
            self.getFigureAxis().add_collection3d(a_poly)
            mesh_poly3d.append(a_poly)
            
        # preserve reference pose
        self.setMeshes(copy.deepcopy(mesh_list))
        
        return(limits, mesh_list, mesh_poly3d)

    def qplot(self, obj, stance, unit='rad', dispMode='VTK', **kwargs):
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
    
    def animate(self, obj, stances, unit='rad', gif=None, frame_rate=25, **kwargs):
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
                 'gif'        : gif,
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
            
        # define animation callback function
        def _animFunc(nf, self, obj, stances, unit, fps, mesh_list, anim_text3d, mesh_poly3d):
            # apply stance to reference pose
            self.fkine(obj, stances, unit=unit, apply_stance=True, 
                      mesh_list=self.getMeshes(), timer=nf)
            
            # convert updated SerialLink meshes to artist poly3D collection
            ax = mesh_poly3d[0].axes 
            if ax is not None:
                for i in range(0,len(mesh_poly3d)):
                    mesh_poly3d[i].remove()
                for i in range(0, len(self.getMeshes())):
                    a_mesh = self.getMeshI(i)
                    a_mesh.rotate([1.,0.,0.], -np.pi/2)
                    a_poly = mplot3d.art3d.Poly3DCollection(a_mesh.vectors)
                    a_poly.set_facecolor(obj.colors[i])
                    self.setPolyI(i, a_poly)
                    ax.add_collection3d(a_poly)
                    mesh_poly3d[i] = a_poly
                    
            # preserve reference pose
            self.setMeshes(copy.deepcopy(mesh_list))
            
            # update rendered frame displayed time text
            time_str = 'time = %.3f' % (float(nf)/fps)
            anim_text3d.set_text(time_str)
            
            return [anim_text3d] + mesh_poly3d
        
        # Plot initial pose stance
        (limits, mesh_list, mesh_poly3d) = self._render_stl_pose(obj, stances, opt.unit, limits=opt.limits)
        
        # define text3D artist for rendered frame time display
        tx = limits[1]*1.2
        ty = limits[2]*1.2
        tz = limits[5]*1.2
        time_text = self.getFigureAxis().text3D(tx, ty, tz, '', ha='center', va='bottom')
        anim_text3d = time_text        

        # set animation parameters, then instantiate an animator
        nframes = stances.shape[0]
        fps = opt.frame_rate
        frame_step_msec = 1000.0 / opt.frame_rate
        
        self.anim = animation.FuncAnimation(self.getFigure(), _animFunc,
                                   fargs=(self, obj, stances, opt.unit, fps, 
                                          mesh_list, anim_text3d, mesh_poly3d),
                                   frames=nframes, blit=False,
                                   interval=frame_step_msec, repeat=False)
        
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
    