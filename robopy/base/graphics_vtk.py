#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: graphics_vtk.py
DATE: Tue Jan  9 07:55:00 2019

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

# Graphics rendering package
try:
    import vtk
except ImportError:
    print("* Error: vtk package required.")
    sys.exit()

#### To support X server virtual framebuffer
###
###from xvfbwrapper import Xvfb

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

__all__ = ('GraphicsVTK', 'VtkPipeline', 
           'np2vtk', 'rgb_named_colors')

###
### Utility routines which do not require VtkPipeline class instances.
###

def np2vtk(mat):
    """
    Returns given RTB transform NumPy matrix as a VTK 4x4 matrix.
    :param mat: a RTB transform NumPy matrix 
    :return obj: a VTK Matrix4x4 object
    """
    if mat.shape == (4, 4):
        obj = vtk.vtkMatrix4x4()
        for i in range(4):
            for j in range(4):
                obj.SetElement(i, j, mat[i, j])
    return obj

def rgb_named_colors(colors):
        """
        Returns a list of RGB vales for VTK color names.
        :param colors: list of color names supported by VTK
        :return rgb_colors: list of corresponding rgb color values
        """
        if type(colors) is not list:
            colors = [colors]
           
        rgb_colors = [0] * len(colors)
        for i in range(len(colors)):
            rgb_colors[i] = vtk.vtkNamedColors().GetColor3d(colors[i])
        return rgb_colors
    
    
###
### MODULE CLASS DEFINITIONS
###
    
class GraphicsVTK(Graphics):
    """ 
    Graphics rendering interface for the VTK rendering package.
      
    This class acts as the interface between RTB drawing and plotting
    routines and the VTK graphics library. Its attributes are private
    and its methods do not require access to RTB manipulator modeling 
    object methods and data structures.
    """
    def __init__(self, gRenderer, dispMode, rend, rendWin, irend,
                       total_time_steps, timer_rate, gif_file, frame_rate):

        ## Instance properties
        
        # Graphics environment properties
        self._dispMode = dispMode
        
        # rendering properties
        self._rend = rend
        self._rendWin = rendWin
        self._irend = irend
 
        # plotting (graphing) properties
        self._axesLimits = [-1.5, 1.5, -1.5, 1.5, -1.5, 1.5]
        
        # rendered actors properties
        self.actors_list = []
        self.mapper_list = []
        self.source_list = []
        
        self.hgtransforms = {}
        
        # animation properties
        self.screenshot_count = 0
        self.timer_rate_fps = timer_rate
        self.timer_step_msec = math.floor(1000.0 / self.timer_rate_fps)
        self.frame_rate = frame_rate
        self.frame_step_msec = math.floor(1000.0 / self.frame_rate)
        
        self.setTotalTimeSteps(total_time_steps)
        self.setGIFfile(gif_file)
        self.setGraphicsRenderer(gRenderer)

        ##super(Graphics, self).__init__()

    def setGraphicsRenderer(self, gRenderer):
        """ Sets graphic renderer for this VTK pipeline.
        """
        super(GraphicsVTK, self).setGraphicsRenderer(gRenderer)
        
    def setGtransform(self, *args, **kwargs):
        """ Set graphics transform.
        """
        super(GraphicsVTK, self).setGtransform()
             
    ### Class properties and methods
       
    theDispModes = ['VTK','IPY','PIL']
  
    @classmethod
    def isDispMode(cls, dmode):
        return dmode in cls.theDispModes
       
    @classmethod  # simply call a module scope routine
    def rgb_named_colors(cls, colors):
        return rgb_named_colors(colors)
    
    ### Instance property setters/getters

    
    """    
      _dispMode = property(fset=setDispMode, fget=getDispMode)
      _rend = property(fset=setRenderer, fget=getRenderer)
      _rendWin = property(fset=setRendWin, fget=getRendWin)
      _irend = property(fset=setIRend, fget=getIRend)
      _axesLimits = propertiy(fset=setAxesLimits, fget=getAxesLimits)
      actors_list = property(fset=setActors, fget=getActors, fdel=delActors)
      mapper_list = property(fset=setMappers, fget=getMappers, fdel=delMappers)
      source_list = property(fset=setSources, fget=getSources, fdel=delSources)
      timer_count = property(fset=setTimerCount, fget=getTimerCount)
      total_time_steps = property(fset=setTotalTimeSteps, fget=getTotalTimeSteps)
      screenshot_count = property(fset=setScreenshotCount, fget=getScreenshotcount)
      gif_file = property(fset=setGIFfile, fget=getGIFfile)
      gif_data = property(fset=setGIFdata, fget=getGIFdata, fdel=delGIFdata)
    """      
  
    def setDispMode(self, dispmode):
        self._dispMode = dispmode
        
    def getDispMode(self):
        return self._dispMode
    
    def setRenderer(self, renderer):
        self._rend = renderer
        
    def getRenderer(self):
        return self._rend
        
    def setRendWin(self, rendWin):
        self._rendWin = rendWin
        
    def getRendWin(self):
        return self._rendWin
    
    def setIRend(self, irend):
        self._irend = irend
        
    def getIRend(self):
        return self._irend
    
    def setAxesLimits(self, xmin, xmax, ymin, ymax, zmin, zmax):
        self._axesLimits = [xmin, xmax, ymin, ymax, zmin, zmax]
    
    def getAxesLimits(self):
        return self._axesLimits
    
    def setActors(self, actors):
        self.actors_list = actors
    
    def getActors(self):
        return self.actors_list
       
    def delActors(self):
        self.actors_list = []
        
    def addActors(self, actors):
        self.actors_list.append(actors)
        
    def setMappers(self, mappers):
        self.mapper_list = mappers
        
    def getMappers(self):
        return self.mapper_list
    
    def delMappers(self):
        self.mapper_list = []
 
    def addMappers(self, mappers):
        self.mapper_list.append(mappers)
        
    def setSources(self, sources):
        self.source_list = sources        
        
    def getSources(self):
        return self.source_list
    
    def delSources(self):
        self.source_list = []
 
    def addSources(self, sources):
        self.source_list.append(sources)
        
    def setTimerCount(self, k):
        self.timer_count = k
        
    def getTimerCount(self):
        return self.timer_count
    
    def incTimerCount(self, k):
        self.timer_count += k
    
    def setTotalTimeSteps(self, total_time_steps):
        if total_time_steps is not None:
            assert type(total_time_steps) is int
            self.setTimerCount(0)
            self.total_time_steps = total_time_steps
            
    def getTotalTimeSteps(self):
        return self.total_time_steps
    
    def setScreenshotCount(self, k):
        self.screenshot_count = k
        
    def getScreenshotCount(self):
        return self.screenshot_count
    
    def incScreenshotCount(self, k):
        self.timer_count += k
        
    def setGIFfile(self, gif_file):
        if gif_file is not None:
            try:
                assert type(gif_file) is str
            except AssertionError:
                gif_file = str(gif_file)
            self.gif_file = gif_file
            self.setGIFdata([])
            self.setScreenshotCount(0)
        else:
            self.gif_file = None
            self.setGIFdata(None)
            
    def getGIFfile(self):
        return self.gif_file
    
    def setGIFdata(self, data):
        self.gif_data = data
    
    def getGIFdata(self):
        return self.gif_data
    
    def addGIFdata(self, data):
        self.gif_data.append(data)
        
    def delGIFdata(self):
        self.gif_data = []
        
    ### Class methods (presented by functional group)
        
    ## Plot elements methods
    
    @staticmethod
    def axesUniversal():
        axes_uni = vtk.vtkAxesActor()
        axes_uni.SetXAxisLabelText("x'")
        axes_uni.SetYAxisLabelText("y'")
        axes_uni.SetZAxisLabelText("z'")
        axes_uni.SetTipTypeToSphere()
        axes_uni.SetShaftTypeToCylinder()
        axes_uni.SetTotalLength(2, 2, 2)
        axes_uni.SetCylinderRadius(0.02)
        axes_uni.SetAxisLabels(0)
        return axes_uni
    
    @staticmethod
    def axesCube(camera, limits):
        
        cube_axes_actor = vtk.vtkCubeAxesActor()

        cube_axes_actor.SetBounds(limits[0], limits[1], 
                                  limits[2], limits[3], 
                                  limits[4], limits[5])
        cube_axes_actor.SetCamera(camera)
        cube_axes_actor.GetTitleTextProperty(0).SetColor(1.0, 0.0, 0.0)
        cube_axes_actor.GetLabelTextProperty(0).SetColor(1.0, 0.0, 0.0)

        cube_axes_actor.GetTitleTextProperty(1).SetColor(0.0, 1.0, 0.0)
        cube_axes_actor.GetLabelTextProperty(1).SetColor(0.0, 1.0, 0.0)

        cube_axes_actor.GetTitleTextProperty(2).SetColor(0.0, 0.0, 1.0)
        cube_axes_actor.GetLabelTextProperty(2).SetColor(0.0, 0.0, 1.0)

        cube_axes_actor.XAxisMinorTickVisibilityOff()
        cube_axes_actor.YAxisMinorTickVisibilityOff()
        cube_axes_actor.ZAxisMinorTickVisibilityOff()

        cube_axes_actor.SetFlyModeToStaticTriad()

        return cube_axes_actor
    
    def axes_x_y(self, camera, limits):
        axis_x_y = self.axesCube(camera, limits)
        axis_x_y.SetUse2DMode(1)
        axis_x_y.ZAxisLabelVisibilityOff()
        axis_x_y.SetAxisOrigin(limits[0], limits[2], 0.0)
        axis_x_y.SetUseAxisOrigin(1)
        return axis_x_y
    
    @staticmethod
    def axesActor2d():
        axes = vtk.vtkAxesActor()
        axes.SetTotalLength(1.0, 1.0, 0.0)
        axes.SetZAxisLabelText("")
        return axes
 
    @staticmethod
    def floor():
        plane = vtk.vtkPlaneSource()
        reader = vtk.vtkJPEGReader()
        reader.SetFileName(pkg_resources.resource_filename("robopy", "media/imgs/floor.jpg"))
        texture = vtk.vtkTexture()
        texture.SetInputConnection(reader.GetOutputPort())
        map_to_plane = vtk.vtkTextureMapToPlane()
        map_to_plane.SetInputConnection(plane.GetOutputPort())
        mapper = vtk.vtkPolyDataMapper()

        mapper.SetInputConnection(map_to_plane.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.SetTexture(texture)
        return actor
    
    def axesCubeFloor(self, rend, xlims=[-1.5, 1.5],
                                  ylims=[-1.5, 1.5],
                                  zlims=[-1.5, 1.5],
                                  position=[0.0, -1.5, 0.0]):
        
        limits = [xlims[0], xlims[1], ylims[0], ylims[1], zlims[0], zlims[1]]
        camera = rend.GetActiveCamera()
        axes = self.axesCube(camera, limits)
        flr = self.floor()
        flr.RotateX(90)
        flr.SetPosition(position[0], position[1], position[2])
        flr.SetScale(3)
        assembly = vtk.vtkAssembly()
        assembly.AddPart(flr)
        assembly.AddPart(axes)
        return assembly
    
    def draw_axes2(self, rend, z_up=False, axes=True, limits=None, **kwargs):
        self.set_camera(rend, xyplot=True, z_up=z_up, limits=limits, **kwargs)
        camera = rend.GetActiveCamera()
        if axes:
            actor = self.axes_x_y(camera, limits)
            self.addActors(actor)
        
    def draw_axes3(self, rend, z_up=False, axes=True, limits=None, **kwargs):
        self.set_camera(rend, xyplot=False, z_up=z_up, limits=limits, **kwargs)
        camera = rend.GetActiveCamera()
        if axes:
            actor = self.axesCube(camera, limits)
            self.addActors(actor)
            
    def draw_cube(self):
        cube = vtk.vtkCubeSource()
        cube.SetCenter(0.0, 0.0, 0.0)
        
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInput(cube.GetOutput())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.0, 0.0, 1.0)
        self.addActors(actor)
        
    def draw_sphere(self):
        sphere = vtk.vtkSphereSource()
        sphere.SetCenter(0.0, 0.0, 0.0)
        sphere.SetRadius(0.5)
        sphere.SetPhiResolution(32)
        sphere.SetThetaResolution(32)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(1.0, 0.0, 0.0)
        self.addActors(actor)
    
    ### Rendering viewpoint methods
    
    def set_camera(self, rend, xyplot=False, z_up=False, **kwargs):
        """
        :param rend: vtk renderer
        :param xyplot: set to True if viewing an XY plot
        """
        
        opts = { 'xyplot' : xyplot,
                 'z_up'   : z_up,
                 'limits' : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        if len(opt.limits) == len(self.getAxesLimits()):
            self.setAxesLimits(opt.limits[0],
                               opt.limits[1],
                               opt.limits[2],
                               opt.limits[3],
                               opt.limits[4],
                               opt.limits[5],
                               )
            
        cam = rend.GetActiveCamera()
        if cam == None: cam = vtk.vtkCamera()
        limits = self.getAxesLimits()
        if opt.xyplot:
            # set camera position (0.0,0.0,zmax)
            cam.SetPosition(0.0, 0.0, opt.limits[5])
            # look towards axes origin
            #cam.SetFocalPoint(0.0, 0.0, 1.0)
            # set camera up to +Y axis
            cam.SetViewUp(0.0, 1.0, 0.0)
            #cam.Roll(-90)
            #cam.Elevation(-90)
            # zoom out a liitle.
            cam.Zoom(0.6)
        elif opt.z_up:
            ### Note: this are hardcode until a user interface is defined.
            # set camera position (xmax,ymax,zmax)
            cam.SetPosition(limits[1], limits[3]/1.5, limits[5]/2)
            # look towards axes origin
            cam.SetFocalPoint(0.0, 0.0, 0.0)
            # camera tilted downward 30 deg from vertical
            y_rad = 37.5 * (np.pi/180.0)  # yaw angle
            cosy = math.cos(y_rad)
            siny = math.sin(y_rad)
            t_rad = 30.0 * (np.pi/180.0)  # tilt angle
            cost = math.cos(t_rad)
            sint = math.sin(t_rad)
            cam.SetViewUp(-cosy*sint, -siny*sint, cost)
            # zoom out a liitle.
            cam.Zoom(0.9)
        else:
            # set camera position (0.0,0.0,zmax)
            cam.SetPosition(0.0, 0.0, opt.limits[5])
            # look towards axes origin
            #cam.SetFocalPoint(0.0, 0.0, 0.0)
            # set camera up to +Y axis
            cam.SetViewUp(0.0, 1.0, 0.0)
            #cam.Roll(-90)
            #cam.Elevation(-90)
            # zoom out a bit.
            cam.Zoom(0.4)

        # use this camera view
        rend.SetActiveCamera(cam)
        
    ### Animation display methods
    
    def ready_rendWin(self, renderer):
        """
        Returns ready vtkRenderer amd vtkRenderWindow.
        
        :param renderer: renderer to check for readiness
        :return: tuple (rend, rendWin)
        """
        if renderer is None:
            if self.getRendWin() is None:
                if self.getRenderer() is None:
                    self.setRenderer(vtk.vtkRenderer())
                self.setRendWin(vtk.vtkRenderWindow())
                self.getRendWin().AddRenderer(self.getRenderer())
            rend = self.getRenderer()
            rendWin = self.getRendWin()
        elif renderer is self.getRenderer():
            if self.getRendWin() is None:
                self.setRendWin(vtk.vtkRenderWindow())
                self.getRendWin().AddRenderer(self.getRenderer())
            rend = self.getRenderer()
            rendWin = self.getRendWin()                           
        else:
            rend = renderer
            rendWin = vtk.vtkRenderWindow()
            rendWin.AddRenderer(rend)
        
        return (rend, rendWin)
    
    def render(self, ui=True):
        """
        Renderers current actors in ready render window.
        """
        (rend, rendWin) = self.ready_rendWin(self.getRenderer())
        
        for each in self.getActors():
            rend.AddActor(each)
        rend.ResetCamera()
        rendWin.Render()

        if ui and (self.getDispMode() == 'VTK'):
            self.getIRend().Initialize()
            self.getIRend().Start()
        else:
            self.getIRend().Start()
        
    def vtk_animate(self, ui=False):
        """
        Creates animation of current actors in ready render window.
        """
        (rend, rendWin) = self.ready_rendWin(self.getRenderer())
    
        rend.ResetCamera()
        rendWin.Render()
        
        self.getIRend().Initialize()
        self.getIRend().CreateRepeatingTimer(self.timer_step_msec)
        
        self.render(ui=False)

    def screenshot(self, filename=None):
        """ Saves render content to a PNG image file.
            :param filename: a file name string
            :return: name of PNG image file of the form filename-####.png
        """
        w2if = vtk.vtkWindowToImageFilter()
        w2if.SetInput(self.getRendWin())
        w2if.Update()
        if filename is None:
            filename = 'screenshot'
        filename = filename + '-%04d.png' % (self.getScreenshotCount())
        writer = vtk.vtkPNGWriter()
        writer.SetFileName(filename)
        self.incScreenshotCount(1)
        writer.SetInputData(w2if.GetOutput())
        writer.Write()
        return filename

    def timer_tick(self):
        ### import imageio
        self.incTimerCount(1)
        
        if self.getTimerCount() >= self.getTotalTimeSteps():
            self.getIRend().DestroyTimer()
            if self.getGIFfile() is not None:
                assert len(self.getGIFdata()) > 0
                imgfile = self.getGIFfile() + '.gif'
                ###imageio.mimsave(imgfile, self.getGIFdata())
                img2gif.writeGif(imgfile, self.getGIFdata(),
                                 duration=self.frame_step_msec/1000.0, 
                                 repeat=False, dither=False,
                                 nq=0, subRectangles=True, dispose=None)
                import os
                for i in range(self.getScreenshotCount()):
                    os.remove(self.getGIFfile() + '-%04d.png' % (i))
                print("Done.")
                print("Animated GIF in file %s" % (imgfile) ) 
                return

        if self.getGIFfile() is not None:
            if ((self.getTimerCount()*self.timer_step_msec) % self.frame_step_msec) == 0:
                imgfile = self.screenshot(filename=self.getGIFfile())
                ### im = imageio.imread(imgfile)
                im = PIL.Image.open(imgfile)
                self.addGIFdata(im)

    ### Plotting display methods
    
    def vtk_show(self, renderer=None):

        (rend, rendWin) = self.ready_rendWin(renderer)
        
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(rendWin)
        iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        
        for actor in self.getActors():
            rend.AddActor(actor)

        rendWin.Render()
        iren.Initialize()
        iren.Start()
        
    @staticmethod
    def ipy_show(renderer, width=400, height=300):
        """
        Takes vtkRenderer instance and returns an IPython Image with 
        the given rendering.
        """
        ### Implemenation Note:
        ###
        ### Attempts to utilize an X virtual framebuffer server
        ### (Xvfb) to capture VTK rendered images for display in
        ### Jupyter/IPython notebooks have been unsuccesful as of
        ### 20 Jan. 2019.
        ###
        ### 1) Using xvfbwrapper
        ###
        ###vdisplay = Xvfb()
        ###vdisplay.start()

        rendWin = vtk.vtkRenderWindow()
        rendWin.SetOffScreenRendering(1)
        rendWin.AddRenderer(renderer)
        rendWin.SetSize(width, height)
        rendWin.Render()

        winToImgFilter = vtk.vtkWindowToImageFilter()
        winToImgFilter.SetInput(rendWin)
        winToImgFilter.Update()
     
        writer = vtk.vtkPNGWriter()
        writer.SetWriteToMemory(1)
        writer.SetInputConnection(winToImgFilter.GetOutputPort())
        writer.Write()

        png_data = memoryview(writer.GetResult()).tobytes()

        ###vdisplay.stop()

        return IPython.display.Image(png_data)
    
    @staticmethod
    def pil_show(renderer, width=400, height=300):
        """
        Takes vtkRenderer instance and returns an PIL Image with 
        the given rendering.
        """
        ### Implementation Note: (see ipy_show() above)
        ###
        ###vdisplay = Xvfb()
        ###vdisplay.start()

        rendWin = vtk.vtkRenderWindow()
        rendWin.SetOffScreenRendering(1)
        rendWin.AddRenderer(renderer)
        rendWin.SetSize(width, height)
        rendWin.Render()

        ###vdisplay.stop()

        winToImgFilter = vtk.vtkWindowToImageFilter()
        winToImgFilter.SetInput(rendWin)
        winToImgFilter.SetInputBufferTypeToRGB()
        winToImgFilter.Update()
     
        writer = vtk.vtkBMPWriter()
        writer.SetWriteToMemory(1)
        writer.SetInputConnection(winToImgFilter.GetOutputPort())
        writer.Write()
        bgr_data = memoryview(writer.GetResult()).tobytes()
    
        return PIL.Image.frombytes('RGB', (width, height), bgr_data,
                                   'raw', 'BGR', 0, -1)

    def show(self, renderer=None, dispMode='VTK'):
        if dispMode == 'IPY' :
            for actor in self.getActors():
                self.getRenderer().AddActor(actor)
            ipy_img = self.ipy_show(renderer=self.getRenderer())
            IPython.display.display(ipy_img)
        elif dispMode == 'PIL':
            for actor in self.getActors():
                self.getRenderer().AddActor(actor)
            pil_img = self.pil_show(renderer=self.getRenderer())
            pil_img.show()
        else:
            self.vtk_show(renderer=self.getRenderer())
    
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
        
    # Display List Interface - These methods must be defined in Mpl3dArtist Class

    def renderDisplayListItem(self, *args, **kwargs):
        """ GraphicsMPL class renderDisplayListItem
        """
        print("* Not yet implemented.")
        return None

    def renderDisplayList(self, *args, **kwargs):
        """ GraphicsMPL class renderDisplayList
        """
        print("* Not yet implemented.")
        return None

    def plotDisplayList(self, *args, **kwargs):
        """ GraphicsMPL class plotDisplayList
        """
        print("* Not yet implemented.")
        return None

    def animateDisplayList(self, *args, **kwargs):
        """ GraphicsMPL class animateDisplayList
        """
        print("* Not yet implemented.")
        return None

### Implementation Note:
###
### Some components of this class still exhibit non-traditional coupling
### between graphics providers and clients due to preservation of existing
### RoboPy code base. This coupling can be mitigated or eliminated in some
### instances by utilizing callback mechanisms as done in most graphical
### rendering and user interface toolkits. A specific example would be the
### RTB fkine function that should be passed to the VtkPipeline qplot()
### and animate() methods for SerialLink objects as a callback routine as
### one would pass animation update functions to an animator, or keypress
### and mouse event handlers to a GUI manager.

class VtkPipeline(GraphicsVTK):
    """ Vtk rendering pipeline for RTB plotting and animation.
     
        This class acts as the interface between RTB plotting and animation
        routines and the RTB manipulator modeling and simulation code.
        Its methods must have access to the RTB manipulator model object
        methods and data structures.
    """
    def __init__(self, dispMode='VTK', background=(0.15, 0.15, 0.15), 
                       total_time_steps=None, timer_rate=60, 
                       gif_file=None, frame_rate=30):
        
        self.gRenderer = self
        self.dispMode = dispMode
        self.rend = vtk.vtkRenderer()
        self.rend.SetBackground(background)
        self.rendWin = None
        self.irend = None
        self.timer_rate_fps = timer_rate
        self.timer_step_msec = math.floor(1000.0 / self.timer_rate_fps)
        self.frame_rate = frame_rate
        self.frame_step_msec = math.floor(1000.0 / self.frame_rate)
        
        self.setTotalTimeSteps(total_time_steps) 
        self.setGIFfile(gif_file)
        
        self._init_super(self.gRenderer,
                         self.dispMode, 
                         self.rend, 
                         self.rendWin, 
                         self.irend,
                         total_time_steps,
                         timer_rate,
                         gif_file,
                         frame_rate)        
        return None
    
    def _init_super(self, gRenderer, dispMode, rend, rendWin, irend,
                          total_time_steps, timer_rate, gif_file, frame_rate):
        super(VtkPipeline, self).__init__(gRenderer, dispMode, rend, rendWin, irend,
                                 total_time_steps, timer_rate, gif_file, frame_rate)
    
    def getAxesLimits(self):
        return super(VtkPipeline, self).getAxesLimits()
    
    ### Class methods
    ###
    
    def draw_cube(self):
        super(VtkPipeline, self).draw_cube()
        
    def draw_sphere(self):
        super(VtkPipeline, self).draw_sphere()
    
    ### Plotting methods
    
    def view(self, rend=None, xyplot=False, z_up=False, axes=True, 
                   limits=[-1.5, 1.5, -1.5, 1.5, -1.5, 1.5], **kwargs):
        opts = { 'rend'   : rend,
                 'xyplot' : xyplot,
                 'z_up'   : z_up,
                 'axes'   : axes,
                 'limits' : limits,
                }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        if opt.rend is None:
            opt.rend = self.getRenderer()
            
        if opt.xyplot:
            self.draw_axes2(opt.rend, z_up=opt.z_up,
                                      axes=opt.axes, 
                                      limits=opt.limits, **args)
        else:
            self.draw_axes3(opt.rend, z_up=opt.z_up,
                                      axes=opt.axes,
                                      limits=opt.limits, **args)

    def pose_plot2(self, pose, **kwargs):
        
        opts = { 'dispMode': self.getDispMode(),
                 'limits' : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        angles = pose.angle
        if type(angles) == int or type(angles) == float:
            angles = [angles]
        z = [0, ] * len(angles)
        x = []
        y = []
        if type(pose) is type(Pose.SO2()):
            x = [0, ] * len(angles)
            y = [0, ] * len(angles)
        elif type(pose) is type(Pose.SE2()):
            for each in pose.transl:
                x.append(each[0])
                y.append(each[1])
        pose_se3 = Pose.SE3().Rz(theta=angles, x=x, y=y, z=z)
        axes_pose = [self.axesActor2d() for each in pose_se3]
        vtk_mat = [np2vtk(each) for each in pose_se3]
        for i in range(pose_se3.length):
            axes_pose[i].SetUserMatrix(vtk_mat[i])
            axes_pose[i].SetAxisLabels(0)
            self.addActors(axes_pose[i])
            
        self.draw_axes2(self.getRenderer(), axes=True, limits=opt.limits)
        self.show(dispMode=opt.dispMode)
        '''
        self.rend(ui=False)
        self.screenshot()
        self.iren.Initialize()
        self.iren.Start()
        '''
    
    def pose_plot3(self, pose, **kwargs):
                    
        opts = { 'dispMode': self.getDispMode(),
                 'z_up'    : False,
                 'limits'  : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        pose_se3 = pose
        if type(pose) is type(Pose.SO3()):
            pose_se3 = pose.to_se3()

        axes = [vtk.vtkAxesActor() for i in range(pose.length)]
        vtk_mat = [np2vtk(each) for each in pose_se3]
        for i in range(len(axes)):
            axes[i].SetUserMatrix(vtk_mat[i])
            axes[i].SetAxisLabels(0)
            self.addActors(axes[i])
            
        self.draw_axes3(self.getRenderer(), z_up=opt.z_up, axes=True,
                        limits=opt.limits)
        
        self.show(dispMode=opt.dispMode)
        '''
        self.rend(ui=False)
        self.screenshot()
        self.iren.Initialize()
        self.iren.Start()
        '''
        
    def plot(self, obj, **kwargs):
        if type(obj) in [type(Pose.SO2()), type(Pose.SE2())]:
            self.pose_plot2(obj, **kwargs)
        elif type(obj) in [type(Pose.SO3()), type(Pose.SE3())]:
            self.pose_plot3(obj, **kwargs)
        else:
            pass
        
    def quat_plot(self, stances):
        pass
    
    def _setup_pipeline_objs(self, obj):   
        """
        Internal function to initialise vtk objects.
        :return: reader_list, actor_list, mapper_list
        """
        reader_list = [0] * len(obj.stl_files)
        actor_list = [0] * len(obj.stl_files)
        mapper_list = [0] * len(obj.stl_files)
        for i in range(len(obj.stl_files)):
            reader_list[i] = vtk.vtkSTLReader()
            loc = pkg_resources.resource_filename("robopy", '/'.join(('media', obj.name, obj.stl_files[i])))
            reader_list[i].SetFileName(loc)
            mapper_list[i] = vtk.vtkPolyDataMapper()
            mapper_list[i].SetInputConnection(reader_list[i].GetOutputPort())
            actor_list[i] = vtk.vtkActor()
            actor_list[i].SetMapper(mapper_list[i])
            actor_list[i].GetProperty().SetColor(obj.colors[i])  # (R,G,B)

        return (reader_list, actor_list, mapper_list)

    ### Implementation Note:
    ###
    ### Is pose rendering/animation performance adversely impacted by applying
    ### stance transforms to vtkActors here instead of in SerialLink.fkine()?

    @staticmethod
    def fkine(obj, stances, unit='rad', apply_stance=False, actor_list=None, timer=None):
        """
        Calculates forward kinematics for array of joint angles.
        :param stances: stances is a mxn array of joint angles.
        :param unit: unit of input angles (rad)
        :param apply_stance: If True, then applied to actor_list.
        :param actor_list: list of actors for given SerialLink object
        :param timer: used only (for animation).
        :return T: list of n+1 homogeneous transformation matrices.
        """
            
        T = obj.fkine(stances, unit=unit, timer=timer)
        
        if apply_stance and actor_list is not None \
                        and len(actor_list) >= len(T):
            for i in range(0,len(T)):
                actor_list[i].SetUserMatrix(np2vtk(T[i]))
                
        return T
    
    def qplot(self, obj, stance, unit='rad', dispMode='VTK', **kwargs):
        """
        Plots the SerialLink object in a desired stance.
        :param stance: list of joint angles for SerialLink object.
        :param unit: unit of input angles.
        :param: dispMode: display mode, one of ['VTK', 'IPY', 'PIL'].
        :return: None.
        """
        opts = { 'unit'     : unit,
                 'dispMode' : dispMode,
                 'z_up'     : False,
                 'limits'   : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        assert type(stance) is np.matrix

        if opt.unit == 'deg':
            stance = stance * (np.pi / 180)
            opt.unit = 'rad'
        
        (reader_list, actor_list, mapper_list) = self._setup_pipeline_objs(obj)

        self.setActors(actor_list)
        self.setMappers(mapper_list)
        #self.setReader(reader_list)
        
        self.fkine(obj, stance, unit=opt.unit, apply_stance=True, 
                   actor_list=self.getActors())
        
        if opt.limits is None:
            xlims = np.asarray(obj.param.get("cube_axes_x_bounds")).flatten()
            ylims = np.asarray(obj.param.get("cube_axes_y_bounds")).flatten()
            zlims = np.asarray(obj.param.get("cube_axes_z_bounds")).flatten()
            limits = [xlims[0], xlims[1], ylims[0], ylims[1], zlims[0], zlims[1]]
        else:
            limits = opt.limits
        
        rend = self.getRenderer()

        self.draw_axes3(rend, z_up=opt.z_up, axes=False, limits=limits, **args)
            
        position = np.asarray(obj.param.get("floor_position")).flatten()
        
        cube_axes = self.axesCubeFloor(rend,
                                       xlims=[limits[0], limits[1]],
                                       ylims=[limits[2], limits[3]],
                                       zlims=[limits[4], limits[5]],
                                       position=position)

        self.addActors(cube_axes)

        for each in self.getActors():
            each.SetScale(obj.scale)
        
        self.show(dispMode=dispMode)
        
    def trplot(self, T):
        return None
    
    def trplot2(self, T):
        return None
        
    def animate(self, obj, stances, unit='rad', gif=None, frame_rate=25, **kwargs):
        """
        Animates SerialLink object over nx6 dimensional input matrix, with each row representing list of 6 joint angles.
        :param stances: nx6 dimensional input matrix.
        :param unit: unit of input angles. Allowed values: 'rad' or 'deg'
        :param gif: name for the written animated GIF image file.
        :param frame_rate: frame_rate for animation.
        :return: null
        """       
 
        opts = { 'unit'       : unit,
                 'gif'        : gif,
                 'frame_rate' : frame_rate,
                 'dispMode'   : self.getDispMode(),
                 'z_up'       : False,
                 'limits'     : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        if opt.unit == 'deg':
            stances = stances * (np.pi / 180)
            opt.unit = 'rad'
            
        '''
        initFunc = None
        if 'init_func' in anim_params:
            initFunc = anim_params['init_func']
        if 'anim_func' in anim_params:
            animFunc = anim_params['anim_func']
        if 'anim_args' in anim_params:
            anim_args = anim_params['anim_args']
        '''
        
        (reader_list, actor_list, mapper_list) = self._setup_pipeline_objs(obj)   
        #self.setReaders(reader_list)
        self.setActors(actor_list)
        self.setMappers(mapper_list)
        
        self.fkine(obj, stances, unit=opt.unit, apply_stance=True,
                   actor_list=self.getActors())
        
        if opt.limits is None:
            xlims = np.asarray(obj.param.get("cube_axes_x_bounds")).flatten()
            ylims = np.asarray(obj.param.get("cube_axes_y_bounds")).flatten()
            zlims = np.asarray(obj.param.get("cube_axes_z_bounds")).flatten()
            limits = [xlims[0], xlims[1], ylims[0], ylims[1], zlims[0], zlims[1]]
        else:
            limits = opt.limits
            
        (rend, rendWin) =self.ready_rendWin(self.getRenderer())
        
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(rendWin)
        if self.getGIFfile() is None:
            iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        else:
            # try to prevent user from interrupting animation image save
            iren.SetInteractorStyle(vtk.vtkContextInteractorStyle())
            def myLeftButtonPressEvent(obj, ev):
                ##print("LeftButtonPressEvent")
                return
            def myWindowEventCallback(obj, ev):
                ##(w,h) = self.getRendWin().GetSize()
                ##print(w,h)
                self.getRendWin().SetSize(300, 300)
                self.getRendWin().Render()
                self.getRendWin().Modified()
                self.getRendWin().Render()
                return
            iren.RemoveObservers('LeftButtonPressEvent')
            iren.RemoveObservers('ModifiedEvent')
            iren.AddObserver('LeftButtonPressEvent', myLeftButtonPressEvent, 11.0)
            iren.AddObserver('ModifiedEvent', myWindowEventCallback, 10.0)
            
        self.setIRend(iren)
                
        self.draw_axes3(rend, z_up=opt.z_up, axes=False, limits=limits, **args)
        
        position = np.asarray(obj.param.get("floor_position")).flatten()
        
        cube_axes = self.axesCubeFloor(rend,
                                       xlims=[limits[0], limits[1]],
                                       ylims=[limits[2], limits[3]],
                                       zlims=[limits[4], limits[5]],
                                       position=position)

        self.addActors(cube_axes)
        
        def execute(pobj, event):
            """ Timer event callback
            """
            nonlocal stances  # Only animate the serial link elements
            nonlocal obj
            
            self.timer_tick()
            
            self.fkine(obj,stances, unit=opt.unit, apply_stance=True, 
                      actor_list=self.getActors(), 
                      timer=self.getTimerCount())
                
            self.setIRend(pobj)
            
            self.getIRend().GetRenderWindow().Render()
            
        self.getIRend().AddObserver('TimerEvent', execute)
        
        self.vtk_animate()
        
    def panimate(self, obj, other=None, duration=5, **kwargs):
        """
        Pose animation of a single pose, or iterpolated between two poses.
        :param other: other Pose SO3 object to transition towards.
        :param duration: alloted transition time period (sec).
        :param **kwargs: see below
        :return: None
        
        Keyword Arguments
          z_up   : whether or not the z-axis is upward
          limits : the plotting boundary x, y and z limits 
        """
        from .quaternion import UnitQuaternion
        assert duration > 0
        
        opts = { 'other'    : other,
                 'duration' : duration,
                 'z_up'     : False,
                 'limits'   : self.getAxesLimits(),
               }
        
        opt = asSimpleNs(opts)
        
        (opt, args) = tb_parseopts(opt, **kwargs)
        
        q1 = []
        q2 = []
        if other is not None:
            assert type(other) is type(Pose.SO3())
            assert obj.length == other.length
            for i in range(obj.length):
                q1.append(UnitQuaternion.rot(obj.data[i]))
                q2.append(UnitQuaternion.rot(other.data[i]))
        else:
            for i in range(obj.length):
                q1.append(UnitQuaternion())
                q2.append(UnitQuaternion.rot(obj.data[i]))

        axis_list = []
        for i in range(obj.length):
            axis_list.append(vtk.vtkAxesActor())
            axis_list[i].SetAxisLabels(0)
            axis_list[i].SetUserMatrix(np2vtk(q1[i].q2tr()))
            self.addActors(axis_list[i])
        
        (rend, rendWin) =self.ready_rendWin(self.getRenderer())
        
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(rendWin)
        if self.getGIFfile() is not None:
            iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        else:
            # try to prevent user from interrupting animation image save
            iren.SetInteractorStyle(vtk.vtkContextInteractorStyle())
            def myLeftButtonPressEvent(obj, ev):
                ##print("LeftButtonPressEvent")
                return
            def myWindowEventCallback(obj, ev):
                ##(w,h) = self.getRendWin().GetSize()
                ##print(w,h)
                self.getRendWin().SetSize(300, 300)
                self.getRendWin().Render()
                self.getRendWin().Modified()
                self.getRendWin().Render()
                return
            iren.RemoveObservers('LeftButtonPressEvent')
            iren.RemoveObservers('ModifiedEvent')
            iren.AddObserver('LeftButtonPressEvent', myLeftButtonPressEvent, 11.0)
            iren.AddObserver('ModifiedEvent', myWindowEventCallback, 10.0)
            
        self.setIRend(iren)
        
        self.draw_axes3(rend, z_up=opt.z_up, axes=True, limits=opt.limits, **args)

        def execute(obj, event):
            """ Timer event callback
            """
            nonlocal axis_list  # Only animate the pose frame
            self.timer_tick()
            r = self.getTimerCount() * (1.0/self.getTotalTimeSteps())
            # apply quaternion interpolation from q1 towards q2
            for i in range(len(axis_list)):
                axis_list[i].SetUserMatrix(np2vtk(q1[i].interp(q2[i], r=r).q2tr()))
            
            self.getRendWin().Render()

        self.getIRend().AddObserver('TimerEvent', execute)
        
        self.vtk_animate()
    
    def qanimate(self, obj, stances, unit='rad', frame_rate=25, gif=None, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def tranimate(self, T, **kwargs):
        print("* Not yet implemented.")
        return None
    
    def tranimate2(self, R, **kwargs):
        print("* Not yet implemented.")
        return None
