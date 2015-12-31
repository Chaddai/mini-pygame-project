# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:42:37 2015

@author: chaddai
"""

# Initialisation des constantes
tilehwscale = 80/101

winwidth = 750
winheight = int(tilehwscale * winwidth)

labwidth = 15
labheight = 15

tilewidth = winwidth // labwidth
tileheight = int(tilehwscale * tilewidth)

scale_factor = tilewidth / 101
