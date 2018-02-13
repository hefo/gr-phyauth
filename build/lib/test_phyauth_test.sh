#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/Users/henrikforssell/GNURadio/gr-phyauth/lib
export PATH=/Users/henrikforssell/GNURadio/gr-phyauth/build/lib:$PATH
export DYLD_LIBRARY_PATH=/Users/henrikforssell/GNURadio/gr-phyauth/build/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-phyauth 
