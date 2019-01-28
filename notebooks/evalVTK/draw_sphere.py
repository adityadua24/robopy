import _robopy
from robopy.base.graphics import GraphicsRenderer

# Select a Graphics Rendering package to use.

gobj = GraphicsRenderer('VTK')  # this sets graphics.gRenderer

# Define some GraphicsVTK parameters which will be used in draw()
# function calls..

dMode = 'IPY'
limits = [-4.0, 4.0, -4.0, 4.0, -4.0, 4.0]

# Draw a red sphere using VTK and display below.

gobj.view(z_up=True, axes=True, limits=limits)
gobj.draw_sphere()
gobj.show(dispMode=dMode)
