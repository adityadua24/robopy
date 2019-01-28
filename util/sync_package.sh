#!/bin/bash

# FILE: sync_package.sh
# PROG: Synchronizes copies of _robopy.py to version in repository ./robopy subdirectory.
# DATE: Jan 23 2019
# AUTH: G. E. Deschaines
# DESC: This script must be located and executed within the robopy repository ./util
#       subdirectory and is used to synchronize all copies of ../_robopy.py located
#       within the repository robopy package subdirectories specified in PDIR_LIST.

PDIR_LIST="eval examples notebooks"

if [ -e ../robopy/_robopy.py ]
then
  COPIES=`find ../ -type f -name "_robopy.py" -exec diff -q ../robopy/_robopy.py {} \; | gawk '{ print $4 }'`
  for COPY in $COPIES
  do
    FPTH=${COPY##../}
    SDIR=${FPTH%%/*}
    for PDIR in $PDIR_LIST
    do
      if [ $SDIR == $PDIR ]
      then
        cp -v ../robopy/_robopy.py $COPY
      fi
    done
  done
else
  echo "* Error: this script must excuted in the robopy repository ./util subdirectory."
  exit -1
fi
