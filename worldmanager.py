# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:43:20 2015

@author: chaddai
"""

import pygame
from pygame.locals import *
from constants import *
from random import randint

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

def random_position(laby, assetname):
    while True:
        (x,y) = (randint(1,labwidth-2),randint(1,labheight-2))
        if laby[y][x] == 0 :
            return convert_to_screen(x,y,assetname)
    
def convert_to_screen(x,y,assetname):
    (xc,yc)=assets_center.get(assetname, (50.5,140))
    return (int(x*tilewidth+tilewidth/2-scale_factor*xc), int(y*tileheight+tileheight/2-scale_factor*yc) )