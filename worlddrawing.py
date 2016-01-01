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
    render_score(win,world,assets,0,0)

def render_score(win,world,assets,x,y):
    sf=0.5
    count = len(treasure_sprites)
    font = pygame.font.SysFont('ComicSans', 50, bold=True)
    score_im = pygame.Surface((count*tilewidth, 2*count*tileheight), flags=SRCALPHA)
    score_im.fill((255,255,255,0))
    for j in range(count):
        sprite = treasure_sprites[j]
        score_im.blit( font.render( "%d ×" % world['score'][sprite], True, (255,255,255,0) ), (0, (j*2+1)*tileheight) )
        score_im.blit( assets[sprite], laby_to_screen(1,1+j*2,sprite) )
    score_im = pygame.transform.smoothscale(score_im, ( int(sf*score_im.get_width()), int(sf*score_im.get_height()) ) )
    win.blit(score_im,(x,y))