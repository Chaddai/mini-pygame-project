# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:43:20 2015

@author: chaddai
"""

import pygame
from pygame.locals import *
from constants import *
from random import randint

def step(laby, world, inputs):
    pc = world['objects']['pc']
    (lx,ly) = pc['lpos']
    (dx,dy) = inputs
    (nx,ny) = (lx+dx, ly+dy)
    if pos_valid(laby, nx, ny):
        pc['lpos'] = (nx,ny)
        del pc['pos']

def event_loop():
    continuer = True
    delta = (0,0)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
            elif event.key in directions.keys():
                # Une des touches directionnelles a été enfoncée. On
                # déplace le pc
                delta = directions[event.key]
    
    return (continuer, delta)
    
