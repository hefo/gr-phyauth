/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_PHYAUTH_SAMPLE_AND_HOLD_H
#define INCLUDED_PHYAUTH_SAMPLE_AND_HOLD_H

#include <phyauth/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace phyauth {

    /*!
     * \brief <+description of block+>
     * \ingroup phyauth
     *
     */
    class PHYAUTH_API sample_and_hold : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<sample_and_hold> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of phyauth::sample_and_hold.
       *
       * To avoid accidental use of raw pointers, phyauth::sample_and_hold's
       * constructor is in a private implementation
       * class. phyauth::sample_and_hold::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace phyauth
} // namespace gr

#endif /* INCLUDED_PHYAUTH_SAMPLE_AND_HOLD_H */

