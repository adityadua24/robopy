import vtk


def setupStack():
    """Sets renderer, renderWindow and renderWindowInteractor with TrackballCamera interaction style. """
    ren = vtk.vtkRenderer()
    ren.SetBackground(1, 1, 1)
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
