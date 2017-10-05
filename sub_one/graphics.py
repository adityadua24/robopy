import vtk


def setupStack():
    """Sets renderer, renderWindow and renderWindowInteractor with TrackballCamera interaction style. """
    ren = vtk.vtkRenderer()
    ren.SetBackground(0.15, 0.15, 0.15)
    ren_win = vtk.vtkRenderWindow()
    ren_win.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
    return ren, ren_win, iren


def render(ren, ren_win, iren):
    ren.ResetCamera()
    ren_win.Render()
    iren.Initialize()
    iren.Start()


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
    # axes_uni.SetCylinderResolution(40)
    # axes_uni.SetSphereResolution(40)
    return axes_uni


def axesCube(ren):
    cube_axes_actor = vtk.vtkCubeAxesActor()
    cube_axes_actor.SetBounds(-3, 3, -3, 3, -3, 3)
    cube_axes_actor.SetCamera(ren.GetActiveCamera())
    cube_axes_actor.GetTitleTextProperty(0).SetColor(1.0, 0.0, 0.0)
    cube_axes_actor.GetLabelTextProperty(0).SetColor(1.0, 0.0, 0.0)

    cube_axes_actor.GetTitleTextProperty(1).SetColor(0.0, 1.0, 0.0)
    cube_axes_actor.GetLabelTextProperty(1).SetColor(0.0, 1.0, 0.0)

    cube_axes_actor.GetTitleTextProperty(2).SetColor(0.0, 0.0, 1.0)
    cube_axes_actor.GetLabelTextProperty(2).SetColor(0.0, 0.0, 1.0)

    cube_axes_actor.DrawXGridlinesOff()
    cube_axes_actor.DrawYGridlinesOff()
    cube_axes_actor.DrawZGridlinesOff()

    cube_axes_actor.XAxisMinorTickVisibilityOff()
    cube_axes_actor.YAxisMinorTickVisibilityOff()
    cube_axes_actor.ZAxisMinorTickVisibilityOff()

    cube_axes_actor.SetFlyModeToStaticTriad()

    return cube_axes_actor


# def axes_x_y():
#     axis_actor_2d_x = vtk.vtkAxisActor2D()
#     axis_actor_2d_y = vtk.vtkAxisActor2D()
#
#     axis_actor_2d_x.SetPoint1(0.2, 0.2)
#     axis_actor_2d_x.SetPoint2(0.2, 0.8)
#     axis_actor_2d_y.SetPoint1(0.2, 0.2)
#     axis_actor_2d_y.SetPoint2(0.8, 0.2)
#
#     axis_actor_2d_x.SetNumberOfMinorTicks(10)
#     axis_actor_2d_y.SetNumberOfMinorTicks(10)
#
#     # assemble_x_y = vtk.vtkActor2DCollection()
#     # assemble_x_y.AddItem(axis_actor_2d_x)
#     # assemble_x_y.AddItem(axis_actor_2d_y)
#
#     return axis_actor_2d_x, axis_actor_2d_y


def axesActor2d():
    axes = vtk.vtkAxesActor()
    axes.SetTotalLength(1, 1, 0)
    axes.SetZAxisLabelText("")

    return axes

class VtkPipeline():
    def __init__(self):
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(0.15, 0.15, 0.15)
        self.ren_win = vtk.vtkRenderWindow()
        self.ren_win.AddRenderer(self.ren)
        self.iren = vtk.vtkRenderWindowInteractor()
        self.iren.SetRenderWindow(self.ren_win)
        self.iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.actor_list = []
        self.mapper_list = []

    def render(self):
        self.ren.ResetCamera()
        self.ren_win.Render()
        self.iren.Initialize()
        self.iren.Start()