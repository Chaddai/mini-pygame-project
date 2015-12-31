# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:43:20 2015

@author: chaddai
"""

import pygame
from pygame.locals import *
from constants import *

def step(world, inputs):
    pass

def event_loop():
    continuer = True
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
    
    return (continuer, ())
