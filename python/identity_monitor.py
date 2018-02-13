#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
import pmt
from gnuradio import gr
from pygame.locals import *
import pygame
import os
import sys

class EQ2440animation(gr.basic_block):
    """
    docstring for block EQ2440animation
    """
    msg_in = pmt.intern('msgtrigger')
    #innoccence_bool = 0;

    def __init__(self, innocence_bool):
        gr.basic_block.__init__(self,
            name="EQ2440animation",
            in_sig=[],
            out_sig=[])
        self.innocence_bool = innocence_bool

        self.message_port_register_in(self.msg_in)
        self.set_msg_handler(self.msg_in, self.handle_trigger)

        pygame.init()
        self.CAPTION = "EQ2440 Tx Identity"
        pygame.display.set_caption(self.CAPTION)
        os.environ["SDL_VIDEO_CENTERED"] = "True"
        self.fps = 60.0
        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = [450,250]
        self.screen = pygame.display.set_mode(self.screen_res,pygame.HWSURFACE)
        #self.rect = pygame.image.load('pic/Eve.png')
        # self.tmp1 = pygame.image.load('tmp/Eve1.jpg')
        # self.tmp2 = pygame.image.load('tmp/Alice.jpg')
        self.tmp1 = pygame.image.load('EveWhite.png')
        self.tmp2 = pygame.image.load('Alice.jpg')
        self.screen.blit(self.tmp1,(225,20))
        self.screen.blit(self.tmp2,(0,20))
        self.font1 = pygame.font.SysFont(None,25)
        self.font2 = pygame.font.SysFont(None,25)
        self.screentext1 = self.font1.render("USRP MAC:192.168.50.176",True,(0,252,0))
        self.screentext2 = self.font2.render("USRP MAC:192.168.50.173",True,(0,252,0))
        self.screen.blit(self.screentext1,[225,0])
        self.screen.blit(self.screentext2,[0,0])
        pygame.display.update()

        #self.rect = pygame.Surface((100, 100))
        # while 1:
        #     if self.innocence_bool == 1:
        #         self.rect = self.tmp2
        #
        #         self.alpha = 1
        #         self.a_change = True
        #         # Tweek the speed
        #         self.blink_spd = 0.6
        #         self.clock.tick(self.fps)
        #         self.Loop()
        #
        #     else:
        #         self.rect = self.tmp1
        #         self.alpha = 1
        #         self.a_change = True
        #         # Tweek the speed
        #         self.blink_spd = 0.6
        #
        #         #start loop
        #         self.clock.tick(self.fps)
        #         self.Loop()

        #self.rect.fill((250, 0,0))



    def handle_trigger(self, msgtrigger):
        # while 1
        #
        if self.innocence_bool == 1:
            #blink the ALice
            print 'Poor Alice'


            self.alpha = 1
            self.a_change = True
            # Tweek the speed
            self.blink_spd = 0.6

            #start loop
            self.clock.tick(self.fps)
            while 1:
                self.ALiceLoop()
                # if self.innocence_bool == 0:
                #     self.rect = self.tmp1

        else:
            print 'Eve is approaching'
            # Tweek the speed
            #start loop


            self.alpha = 1
            self.a_change = True
            # Tweek the speed
            self.blink_spd = 0.6

            #start loop

            self.clock.tick(self.fps)
            while 1:
                self.EveLoop()
        print "hello"

    def ALiceLoop(self):
        # main game loop
        self.eventLoop()

        self.last_tick = pygame.time.get_ticks()

        self.screen.fill((0,0,0))
        #Check if alpha is going up
        if self.a_change:
            self.alpha += self.blink_spd
            if self.alpha >= 175:#if all the way up go down
                self.a_change = False
        #Check if alpha is going down
        elif self.a_change == False:
            self.alpha += -self.blink_spd
            if self.alpha <= 30: #if all the way down go up
                self.a_change = True


        self.tmp2.set_alpha(self.alpha)
        self.screen.blit(self.screentext1,[225,0])
        self.screen.blit(self.screentext2,[0,0])
        self.screen.blit(self.tmp2,(0,20))
        self.screen.blit(self.tmp1,(225,20))

        pygame.display.update()

    def EveLoop(self):
        # main game loop
        self.eventLoop()

        self.last_tick = pygame.time.get_ticks()

        self.screen.fill((0,0,0))
        #Check if alpha is going up
        if self.a_change:
            self.alpha += self.blink_spd
            if self.alpha >= 175:#if all the way up go down
                self.a_change = False
        #Check if alpha is going down
        elif self.a_change == False:
            self.alpha += -self.blink_spd
            if self.alpha <= 30: #if all the way down go up
                self.a_change = True

        self.tmp1.set_alpha(self.alpha)
        self.screen.blit(self.screentext1,[225,0])
        self.screen.blit(self.screentext2,[0,0])
        self.screen.blit(self.tmp1,(225,20))
        self.screen.blit(self.tmp2,(0,20))

        pygame.display.update()


    def eventLoop(self):
        # the main event loop, detects keypresses
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def set_innocence_bool(self,innocence_bool):
        self.innocence_bool = innocence_bool


    # def forecast(self, noutput_items, ninput_items_required):
    #     #setup size of input_items[i] for work call
    #     for i in range(len(ninput_items_required)):
    #         ninput_items_required[i] = noutput_items

    # def general_work(self, input_items, output_items):
    #     output_items[0][:] = input_items[0]
    #     consume(0, len(input_items[0]))
    #     #self.consume_each(len(input_items[0]))
    #     return len(output_items[0])
