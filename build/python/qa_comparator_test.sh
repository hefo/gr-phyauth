#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/Users/henrikforssell/GNURadio/gr-phyauth/python
export PATH=/Users/henrikforssell/GNURadio/gr-phyauth/build/python:$PATH
export DYLD_LIBRARY_PATH=/Users/henrikforssell/GNURadio/gr-phyauth/build/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=/Users/henrikforssell/GNURadio/gr-phyauth/build/swig:$PYTHONPATH
/opt/local/bin/python2.7 /Users/henrikforssell/GNURadio/gr-phyauth/python/qa_comparator.py 
