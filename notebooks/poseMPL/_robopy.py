"""
Imports RoboPy module

This file is a temporary component of the ipynb branch of RoboPy for the
porting RTB to Python development effort used to facilitate execution of
Python scripts from within the directory hierarchy for a cloned robopy
repository or unpacked robopy-ipynb repository source distribution work
space.

If this robopy module version is installed, then use of 'import _robopy'
statements in Python scripts within work space subdirectories containing
this file may be removed or replaced with 'import robopy' depending upon
usage context.

To avoid cluttering a repository's root directory with non package files,
it's common practice to perform development work and test efforts in work,
test and temp directories adjacent to the package module directory as
shown in the following directory tree for a cloned robopy repository or
unpacked robopy-ipynb repository source distribution.

Package directories such as eval and util are for development purposes
and it's not anticipated they would be included in user oriented source
distribution one would expect to install from PyPI or Conda-Forge.

  +- robopy or robopy-ipynb
     +- binder            - configuration files for MyBinder installation
     +- docs              - documentation
     +- eval              - development capability evaluation scripts
     +- examples          - example scripts
     +- notebooks         - Jupyter/IPython notebooks
     |  +- (folder)       - notebook folder
     |     |- _robopy.py  - copy of ../../robopy/_robopy.py
     |
     +- robopy            - robopy module and package sources
     |  +- base           - base module source
     |  +- media          - package media data files
     |  +- tests          - test module scripts
     |  |- _robopy.py     - this file
     |
     +- util              - repository configuraton management scripts
     |
     |- setup.py          - build and install script for robopy module
     |                      and distribution package
     |
    --- ^^^ Package ^^^ | vvv Development Test Scripts/Data vvv
     |
     +- test              - development test scripts
     |  |- _robopy.py     - copy of, or symbolic link to ../robopy/_robopy.py
     |
    --- ^^^ Development Test Scipts/Data ^^^ | vvv Development Workspace vvv
     |
     +- build             - created by 'python setup.py [build|install]'
     +- dist              - created by 'python setup.py install'
     +- robopy.egg-info   - created by 'python setup.py [build|install]'
     +- temp              - development work temporary files
     +- (venv)            - possible virtual environment created by an IDE
     +- work              - development work scripts/data
        |- _robopy.py     - copy of, or symbolic link to ../robopy/_robopy.py
"""

import os, sys

if 'BINDER_SERVICE_HOST' in os.environ:
        # Must be on MyBinder.org site; robopy should be installed!
        import robopy
        print('Using installed RoboPy module version %s.' % robopy.__version__)
else:
    try:
        import robopy as robopy
        print('Using installed RoboPy module version %s.' % robopy.__version__)

    except ImportError:
        thisdir = os.path.dirname(__file__)
        libdir = None
    
        # The following assumes this file is in a subdirectory adjacent
        # to ./robopy or in a ./notebooks subdirectory of the RoboPy
        # directory tree for a cloned robopy repository or unpacked
        # robopy-ipynb repository source distribution on an Ubuntu like
        # platform with Python 3 (see file header comment block above).

        # Determine if in the root directory tree of a cloned robopy 
        # repository or ropopy-ipynb respository source distribution. 

        dirs = thisdir.split(os.sep)

        if 'robopy' in dirs :
            root = 'robopy'
        elif 'robopy-ipynb' in dirs:
            root = 'robopy-ipynb'
        else:
            print("Could not locate RoboPy root.")
            sys.exit(-1)

        # find prefix to the root.

        k = len(dirs) - 1
        if dirs[k] == root:
            # Note: this file shouldn't be in root directory.
            prefix = '.'
        else:
            prefix = '..'
            k -= 1
            while dirs[k] != root:
                prefix = os.path.join('..', prefix)
                k -= 1

        # Processing control flow:
        #
        #   (1) If the ./build subdirectory exists, then it's intended
        #       for a robopy build configuration to be utilized.
        #   (2) Otherwise, it's intended for the pre-build robopy module
        #       source to be utilized.
        #
        # Note: Be sure to run 'pip uninstall robopy' if (1) is intended
        #       and 'python setup.py clean', or delete ./build directory
        #       if (2) is intended.

        libdir = os.path.join(thisdir, prefix, 'build', 'lib')
    
        if libdir is not None:
            # first try to find robopy module in build/lib directory
            if os.path.isdir(os.path.join(libdir,'robopy')):
                if libdir not in sys.path:
                    print('Using RoboPy module %s/robopy.' % libdir)
                    if sys.path[0] == '' or sys.path[0] == '.':
                        sys.path.insert(1, libdir)
                    else:
                        sys.path.insert(0, libdir)
            else:
                # now try robopy module source directory
                libdir = os.path.join(thisdir, prefix)
                if os.path.isdir(os.path.join(libdir,'robopy')):
                    if libdir not in sys.path:
                        print('Using RoboPy module %s/robopy.' % libdir)
                        if sys.path[0] == '' or sys.path[0] == '.':
                            sys.path.insert(1, libdir)
                        else:
                            sys.path.insert(0, libdir)
                else:
                    print("Could not locate RoboPy module.")
                    sys.exit(-1)
        else:
            print("Could not locate RoboPy module.")
            sys.exit(-1)