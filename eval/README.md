#### Scripts to evaluate drawing, plotting and animation using VTK and Matplotlib.

-----------------
##### Instructions

Each of these capability evaluation scripts, except eval_display_list_ipv.py
and eval_graphics_vtk_ipy.py, can be run from a command shell (terminal window)
using Python 3 as:

>$ python3 _scriptfile_

The eval_display_list_ipv.py can only be run in a Jupyter notebooks. See the
Jupyter notebooks sample ./notebooks/dListIPV/dListIPV.ipynb.

The eval_graphics_vtk_ipy.py script must be run using IPython in a
Jupyter qtconsole as:

>$ jupyter qtconsole
>
>\[1] run eval_graphics_vtk_ipy.py

-------------
##### Scripts

````
_robopy.py                   - Ignore. RTB for Python development workspace
                               script imported by the following evaluation
                               scripts.

eval_display_list_mpl.py     - Evaluates graphics_mpl module's capability to
                               provide RTB DisplayList plots and animation of
                               graphics entities, such as rendered geometric
                               shapes defined with mesh grid arrays, using
                               matplotlib graphics package. This script is
                               also provided as the Jupyter notebooks sample
                               ./notebooks/dListMPL/dListMPL.ipynb

eval_display_list_ipv.py     - Evaluates graphics_ipv module's capability to
                               provide RTB DisplayList plots and animation of
                               graphics entities, such as rendered geometric
                               shapes defined with mesh grid arrays, using
                               ipyvolume graphics package. This script is
                               also provided as the Jupyter notebooks sample
                               ./notebooks/dListIPV/dListIPV.ipynb

eval_graphics_mpl.py         - Evaluates graphics_mpl module's capability to
                               provide RTB SerialLink plots and animation
                               rendered from STL mesh data using matplotlib
                               graphics package.

eval_graphics_vtk.py         - Evaluates graphics_vtk module's capability to
                               provide RTB SO2 and SO3 Pose transform's xyz
                               coordinate frame plots and animation, and
                               SerialLink plots and animation rendered from
                               STL mesh data by VTK using vtk graphics package.

eval_graphics_vtk_ipy.py     - Same as 'eval_graphics_vtk.py", but must be
                               run within Jupyter qtconsole or Spyder3 ipython
                               console.

````