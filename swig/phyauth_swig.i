/* -*- c++ -*- */

#define PHYAUTH_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "phyauth_swig_doc.i"

%{
#include "phyauth/comparator.h"
#include "phyauth/sample_and_hold.h"
%}


%include "phyauth/comparator.h"
GR_SWIG_BLOCK_MAGIC2(phyauth, comparator);
%include "phyauth/sample_and_hold.h"
GR_SWIG_BLOCK_MAGIC2(phyauth, sample_and_hold);
