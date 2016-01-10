# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:42:37 2015

@author: chaddai
"""

from random import randint, choice
from pygame.locals import *

# Initialisation des constantes
tilehwscale = 80/101

labwidth = 21
labheight = 15

winwidth = 1050
winheight = int(labheight / labwidth * tilehwscale * winwidth)



tilewidth = winwidth // labwidth
tileheight = int(tilehwscale * tilewidth)

scale_factor = tilewidth / 101

assets_center = {
    'Character Boy': (50,140),
    'Grass Block': (50,90),
    'Water Block': (50,90),
    'Dirt Block' : (50,90),
    'Rock' : (50,135),
    'Tree Short' : (50,135),
    'Tree Tall' : (50,135),
    'Tree Ugly' : (50,135),
    'Star' : (50,125),
    'Heart' : (50,125)
    }

def laby_to_screen(x,y,assetname):
    (xc,yc)=assets_center.get(assetname, (50.5,140))
    # Ceci correspond à une translation de sf*(xc,yc) au centre de la tuile
    # de coordonnées x, y
    return (int(x*tilewidth+tilewidth/2-scale_factor*xc)
        , int(y*tileheight+tileheight/2-scale_factor*yc) )

def random_position(laby):
    while True:
        (x,y) = (randint(1,labwidth-2),randint(1,labheight-2))
        if laby[y][x] == 0 :
            return (x,y)

def pos_valid(laby, x, y):
    return 0 <= x < labwidth and 0 <= y < labheight and laby[y][x] == 0

def isolated(laby, x, y):
    for (dx,dy) in directions.values():
        (nx, ny) = (x+dx, y+dy)
        if 0 <= nx < labwidth and 0 <= ny < labheight and laby[ny][nx] == 1:
            return False
    return True

treasure_sprites = ['Star', 'Heart']
deco_sprites = ['Rock', 'Tree Short', 'Tree Tall', 'Tree Ugly']

def create_treasure_map(laby, n):
    tm = [list(line) for line in laby]
    ts = {}
    for i in range(n):
        name = 't%03d' % i
        (x,y) = random_position(tm)
        tm[y][x] = name
        ts[name] = {'lpos' : (x,y), 'sprite' : choice(treasure_sprites)}
    return (tm, ts)

directions = {
    K_KP1 : (-1,1),
    K_KP2 : (0,1),
    K_KP3 : (1,1),
    K_KP4 : (-1,0),
    K_KP6 : (1,0),
    K_KP7 : (-1,-1),
    K_KP8 : (0,-1),
    K_KP9 : (1,-1),
}