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
            land = "Grass Block" if laby[y][x] == 0 else "Water Block"
            tile = assets[land]
            bg.blit(tile, laby_to_screen(x,y,land))
    return bg
    
def draw_world(win, world, assets):
    def ypos(obj): 
        (name, prop) = obj
        if 'pos' in prop:
            return prop['pos']
        else:
            (x,y) = prop['lpos']
            prop['pos'] = laby_to_screen(x,y,prop['sprite'])
            return prop['pos']
    orderedWorld = sorted(world['objects'].items(), key=ypos)
    for (name,prop) in orderedWorld:
        win.blit(assets[prop['sprite']], prop['pos'])