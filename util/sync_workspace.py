#!/usr/bin/env python3
#
# FILE: sync_workspace.py
# PROG: Synchronizes copies of REF_FILE to version in repository ./robopy subdirectory.
# DATE: Jan 23 2019
# AUTH: G. E. Deschaines
# DESC: This script must be located in the robopy repository ./util
#       subdirectory and is used to synchronize all copies of REF_FILE
#       found within the repository work space subdirectories that are
#       not specified in the IGNORE_SDIR list.

import sys
import os
import filecmp
import shutil


REF_FILE = '_robopy.py'

IGNORE_SDIR = ['.git', '.idea']
IGNORE_SDIR = IGNORE_SDIR + ['binder', 'docs', 'eval', 'examples', 'notebooks', 'robopy', 'utils']
IGNORE_SDIR = IGNORE_SDIR + ['build', 'dist', 'robopy.egg-info', 'venv']
IGNORE_PATH = []


def search_dir_name_path(name, path):
    """
    Returns True if given directory name and path are to be searched for
    copies of REF_FILE, otherwise returns False.
    :param name: directory name
    :param path: directory path
    :return: True or False
    """
    return name[0] != '.' and path not in IGNORE_PATH


def get_dirpaths(path):
    """
    Get list of directory paths for given directory path.
    :param path: given directory path
    :return dir_paths: list of directory paths (can be empty list)
    """
    dir_paths = []
    for entry in os.scandir(path):
        if entry.is_dir() and search_dir_name_path(entry.name, entry.path):
            dir_paths.append(entry.path)

    return dir_paths


def get_filecopies(dir_path, ref_file):
    """
    Returns list of reference file copies found within given directory path.
    :param dir_path: directory path
    :param ref_file: reference file
    :return file_copies: list of file copies (can be empty list)
    """
    file_copies = []

    # Initialize dirpaths stack
    dirpaths_stack = [get_dirpaths(dir_path)]

    # Process dirpaths_stack until empty
    while len(dirpaths_stack) > 0:
        dir_paths = dirpaths_stack.pop()
        if len(dir_paths) > 0:
            for path in dir_paths:  # look for REF_FILE in this directory path
                for entry in os.scandir(path):
                    if entry.is_file():
                        if entry.name == ref_file and entry.path != REF_PATH:
                            # found a copy of REF_FILE
                            file_copies.append(entry.path)
                    elif entry.is_dir() and search_dir_name_path(entry.name, entry.path):
                        # found another directory to search
                        dpaths = get_dirpaths(entry.path)
                        if len(dpaths) > 0:
                            dirpaths_stack.append(dpaths)

    return  file_copies


def copy_from_ref(ref_path, tgt_path):
    """
    Copies over file at tgt_path with reference file at ref_path
    :param ref_path: filepath of copy reference
    :param tgt_path: filepath of copy target
    :return: None
    """
    shutil.copy2(ref_path, tgt_path, follow_symlinks=False)


if __name__ == '__main__':

    # Get path to util directory containing this file.
    util_path = os.path.dirname(os.path.realpath(__file__))

    # Determine repository path containing robopy module subdirectory.
    REPO_PATH = util_path.replace('/util', '')

    # Determine path of reference file.
    REF_PATH = os.sep.join([REPO_PATH, 'robopy', REF_FILE])
    if not os.path.isfile(REF_PATH):
        print("* Error: this script must be in robopy repository ./util subdirectory.")
        sys.exit(-1)

    # Prepend REPO_PATH to IGNORE_SDIR to create IGNORE_PATH list.
    for sdir in IGNORE_SDIR:
        IGNORE_PATH.append(os.sep.join([REPO_PATH, sdir]))

    # Reference file stat info.
    r_statinfo = os.stat(REF_PATH)

    # Get all relevant copies of REF_FILE located in repository directory tree.
    file_copies = get_filecopies(REPO_PATH, REF_FILE)

    # Copy over copies of REF_FILE that are not the same as REF_FILE.
    for f in file_copies:
        f_statinfo = os.stat(f)
        if f_statinfo.st_size != r_statinfo.st_size:
            print("%s not same size as %s" % (f, REF_PATH))
            copy_from_ref(REF_PATH, f)
        elif filecmp.cmp(f, REF_PATH, shallow=False) is not True:
            print("%s not same content as %s" % (f, REF_PATH))
            copy_from_ref(REF_PATH, f)