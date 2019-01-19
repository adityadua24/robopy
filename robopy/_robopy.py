""" Imports RoboPy module

    This file is a temporary component of the ipynb branch of RoboPy for the 
    porting RTB to Python development effort used to facilitate execution of 
    Python scripts from within an unpacked robopy-ipynb distribution directory
    work space. If the robopy-ipynb robopy module is installed then use of
    of 'import _robopy' statements in Python scripts may be replaced with 
    'import robopy'.

    To avoid cluttering a repository's root directory with non package files,
    it's common practice to perform development and test efforts in work and 
    and temp directories adjacent to the package directory as shown in the 
    following directory hierarchy for a RoboPy robopy-ipynb repository clone
    or source distribution. 

       +- binder          - configuration files for MyBinder installation
       +- build           - created by 'python setup.py [build|install]'
       +- docs            - robopy documentation
       +- examples        - robopy example scripts
       +- notebooks       - robopy Jupyter/IPython notebooks
       +- robopy          - robopy module source
       +- robopy.egg-info - created by 'python setup.py install'
       +- temp            - workspace temporary files
       +- test            - test scripts
       +- (venv)          - possible virtual environment created by an IDE
       +- work            - workspace
"""

import os, sys

if 'BINDER_SERVICE_HOST' in os.environ:
        # Must be on MyBinder.org site; robopy should be installed!
        import robopy
else:
    try:
        import robopy as robopy
        print('Using installed RoboPy module.')

    except ImportError:
        thisdir = os.path.dirname(__file__)
        libdir = None
    
        # The following assumes this file is in a subdirectory adjacent
        # to ./robopy or in a ./notebooks subdirectory for an unpacked 
        # RoboPy robopy-ipynb distribution directory hierarchy on an 
        # Ubuntu like platform with Python 3.

        # Determine if in the root directory tree of a cloned robopy 
        # repository or ropopy-ipynb respository source distribution. 

        dirs = thisdir.split(os.sep)

        if 'robopy' in dirs :
            root = 'robopy'
        elif 'robopy-ipynb' in dirs:
            root = 'robopy-ipynb'
        else:
            print("Could not locate RoboPy module.")
            sys.exit(1); 

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
        # Note: Be sure to run 'python setup.py clean', or delete the
        #       ./build directory if (2) is intended. 

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
                    sys.exit(1);
        else:
            print("Could not locate RoboPy module")
            sys.exit(1);
