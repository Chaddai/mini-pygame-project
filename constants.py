# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:42:37 2015

@author: chaddai
"""

from random import randint

# Initialisation des constantes
tilehwscale = 80/101

winwidth = 900
winheight = int(tilehwscale * winwidth)

labwidth = 15
labheight = 15

tilewidth = winwidth // labwidth
tileheight = int(tilehwscale * tilewidth)

scale_factor = tilewidth / 101

assets_center = {
    'Character Boy': (50,140),
    'Grass Block': (50,90),
    'Water Block': (50,90)
    }

def laby_to_screen(x,y,assetname):
    (xc,yc)=assets_center.get(assetname, (50.5,140))
    return (int(x*tilewidth+tilewidth/2-scale_factor*xc)
        , int(y*tileheight+tileheight/2-scale_factor*yc) )

def random_position(laby, assetname):
    while True:
        (x,y) = (randint(1,labwidth-2),randint(1,labheight-2))
        if laby[y][x] == 0 :
            return laby_to_screen(x,y,assetname)