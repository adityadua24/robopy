#### Example scripts to demonstrate drawing, plotting and animation using VTK and Matplotlib.


-----------------
##### Instructions

Each of these examples, except eval_graphics_vtk_ipy.py, can be run from
a command shell (terminal window) using Python 3 as:

>$ python3 _scriptfile_

The eval_graphics_vtk_ipy.py script must be run using IPython in a
Jupyter qtconsole as:

>$ jupyter qtconsole
>
>\[1] run eval_graphics_vtk_ipy.py

-------------
##### Examples

````
_robopy.py                              - Ignore. RTB for Python development workspace
                                                    script imported by the following example scripts.

eval_graphics_mpl.py           - Evaluates graphics_mpl module's capability to
                                                   provide RTB SerialLink plots and animation
                                                   rendered from STL mesh data using matplotlib
                                                   graphics package.

eval_graphics_vtk.py            - Evaluates graphics_vtk module's capability to
                                                   provide RTB SO2 and SO3 Pose transform's xyz
                                                   coordinate frame plots and animation, and
                                                   SerialLink plots and animation rendered from
                                                   STL mesh data by VTK using vtk graphics package.

eval_graphics_vtk_ipy.py     - Same as 'eval_graphics_vtk.py", but must be
                                                   run within Jupyter qtconsole or Spyder3 ipython
                                                   console.

pose_multiply.py                   - Demonstrates multiplication operation on Pose
                                                   objects (no graphics).

poseSO3_animation.py        - Displays motion of a SO3 Pose transform's xyz
                                                   coordinate frame rendered by VTK, first without
                                                   creating, and then creating an animated GIF file
                                                   from captured VTK rendered images.

puma560_animation.py      - Displays motion of a Puma560 manipulater arm
                                                  over a range of stances rendered by VTK from
                                                  STL mesh data, and creates animated GIF file
                                                  from captured VTK rendered images.

puma560_plot.py                 - Displays Puma560 manipulater arm in nominal
                                                  stance rendered in an interactive trackball
                                                  camera window by VTK from STL mesh data files.
````