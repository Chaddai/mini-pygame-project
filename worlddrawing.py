# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:29:48 2015

@author: chaddai
"""

import pygame
from constants import *

def create_background(assets, laby):
    (lw, lh, tw, th, sf) = (labwidth, labheight, tilewidth, tileheight, scale_factor)
    bg = pygame.Surface((winwidth, winheight))
    for y in range(lh):
        for x in range(lw):
            tile = assets["Grass Block" if laby[y][x] == 0 else "Water Block"]
            bg.blit(tile, (x*tw,y*th-int(sf*50)))
    return bg
    
def draw_world(win, world, assets):
    win.blit(assets['Character Boy'], world['character position'])