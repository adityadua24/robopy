#### Example scripts to demonstrate drawing, plotting and animation using VTK and Matplotlib.

------------------
##### Instructions

Each of these examples can be run from a command shell (terminal window)
using Python 3 as:

>$ python3 _scriptfile_

--------------
##### Examples

````
_robopy.py                   - Ignore. RTB for Python development workspace
                               script imported by the following example scripts.

pose_multiply.py             - Demonstrates multiplication operation on Pose
                               objects (no graphics).

poseSO3_animation.py         - Displays motion of a SO3 Pose transform's xyz
                               coordinate frame rendered by VTK, first without
                               creating, and then creating an animated GIF file
                               from captured VTK rendered images.

puma560_animation.py         - Displays motion of a Puma560 manipulater arm
                               over a range of stances rendered by VTK from
                               STL mesh data, and creates animated GIF file
                               from captured VTK rendered images.

puma560_plot.py              - Displays Puma560 manipulater arm in nominal
                               stance rendered in an interactive trackball
                               camera window by VTK from STL mesh data files.
````