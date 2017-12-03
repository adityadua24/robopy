# Created by: Aditya Dua
# 18 August 2017
import pkg_resources
import vtk


class VtkPipeline:
    def __init__(self, background=(0.15, 0.15, 0.15)):
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(background[0], background[1], background[2])
        self.ren_win = vtk.vtkRenderWindow()
        self.ren_win.AddRenderer(self.ren)
        self.iren = vtk.vtkRenderWindowInteractor()
        self.iren.SetRenderWindow(self.ren_win)
        self.iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.actor_list = []
        self.mapper_list = []

    def render(self):
        self.ren.ResetCamera()
        # self.set_camera()
        self.ren_win.Render()
        self.iren.Initialize()
        self.iren.Start()

    def add_actor(self, actor):
        self.actor_list.append(actor)
        self.ren.AddActor(actor)

    def set_camera(self):
        cam = self.ren.GetActiveCamera()
        cam.Roll(-90)
        cam.Elevation(-90)
        cam.Zoom(0.6)


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


def axesCube(ren):
    cube_axes_actor = vtk.vtkCubeAxesActor()
    cube_axes_actor.SetBounds(-1.5, 1.5, -1.5, 1.5, -1.5, 1.5)
    cube_axes_actor.SetCamera(ren.GetActiveCamera())
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


def axes_x_y(ren):
    axis_x_y = axesCube(ren)
    axis_x_y.SetUse2DMode(1)
    axis_x_y.ZAxisLabelVisibilityOff()
    axis_x_y.SetAxisOrigin(-3, -3, 0)
    axis_x_y.SetUseAxisOrigin(1)

    return axis_x_y


def axesActor2d():
    axes = vtk.vtkAxesActor()
    axes.SetTotalLength(1, 1, 0)
    axes.SetZAxisLabelText("")

    return axes


def vtk_colors(colors):
    """
    Returns a list of vtk colors
    :param colors: List of color names supported by vtk
    :return: A list of vtk colors
    """
    if type(colors) is not list:
        colors = [colors]
    colors_rgb = [0] * len(colors)
    for i in range(len(colors)):
        colors_rgb[i] = list(vtk.vtkNamedColors().GetColor3d(colors[i]))
    return colors_rgb


def floor():
    plane = vtk.vtkPlaneSource()
    reader = vtk.vtkJPEGReader()
    reader.SetFileName(pkg_resources.resource_filename(__name__, '/'.join(('media', 'imgs', 'floor.jpg'))))
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


def axesCubeFloor(ren):
    axes = axesCube(ren)
    flr = floor()
    flr.RotateX(90)
    flr.SetPosition(0, -1.5, 0)
    flr.SetScale(3)
    assembly = vtk.vtkAssembly()
    assembly.AddPart(flr)
    assembly.AddPart(axes)
    return assembly
