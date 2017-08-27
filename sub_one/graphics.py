import vtk


def setupStack():
    """Sets renderer, renderWindow and renderWindowInteractor with TrackballCamera interaction style. """
    ren = vtk.vtkRenderer()
    ren.SetBackground(0.15, 0.15, 0.15)
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
    return ren, renWin, iren


def render(ren, renWin, iren):
    ren.ResetCamera()
    renWin.Render()
    iren.Initialize()
    iren.Start()


def axesUniversal():
    axesUni = vtk.vtkAxesActor()
    axesUni.SetXAxisLabelText("x'")
    axesUni.SetYAxisLabelText("y'")
    axesUni.SetZAxisLabelText("z'")
    axesUni.SetTipTypeToSphere()
    axesUni.SetShaftTypeToCylinder()
    axesUni.SetTotalLength(2, 2, 2)
    axesUni.SetCylinderRadius(0.02)
    axesUni.SetAxisLabels(0)
    # axesUni.SetCylinderResolution(40)
    # axesUni.SetSphereResolution(40)
    return axesUni


def axesCube(ren):
    cubeAxesActor = vtk.vtkCubeAxesActor()
    cubeAxesActor.SetBounds(-1.5, 1.5, -1.5, 1.5,-1.5, 1.5)
    cubeAxesActor.SetCamera(ren.GetActiveCamera())
    cubeAxesActor.GetTitleTextProperty(0).SetColor(1.0, 0.0, 0.0)
    cubeAxesActor.GetLabelTextProperty(0).SetColor(1.0, 0.0, 0.0)

    cubeAxesActor.GetTitleTextProperty(1).SetColor(0.0, 1.0, 0.0)
    cubeAxesActor.GetLabelTextProperty(1).SetColor(0.0, 1.0, 0.0)

    cubeAxesActor.GetTitleTextProperty(2).SetColor(0.0, 0.0, 1.0)
    cubeAxesActor.GetLabelTextProperty(2).SetColor(0.0, 0.0, 1.0)

    cubeAxesActor.DrawXGridlinesOn()
    cubeAxesActor.DrawYGridlinesOn()
    cubeAxesActor.DrawZGridlinesOn()

    cubeAxesActor.XAxisMinorTickVisibilityOff()
    cubeAxesActor.YAxisMinorTickVisibilityOff()
    cubeAxesActor.ZAxisMinorTickVisibilityOff()

    cubeAxesActor.SetAxisOrigin(1.5, 1.5, 1.5)
    cubeAxesActor.SetUseAxisOrigin(1)
    return cubeAxesActor
