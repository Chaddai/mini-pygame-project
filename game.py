# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:53:51 2015

@author: chaddai
"""

# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os.path
from random import randint
from labyrinthes import fabrique_labyrinthe
from assetsloader import create_assets
from worlddrawing import create_background, draw_world
from worldmanager import step, event_loop

# Initialisation des constantes
winwidth = 750
winheight = 750

labwidth = 15
labheight = 15

tilewidth = winwidth // labwidth
tileheight = winheight // labheight

laby = fabrique_labyrinthe(labwidth, labheight)

world = ()

# Initialisation de la librairie
pygame.init()

# Création de la fenêtre et du labyrinthe en arrière plan
window = pygame.display.set_mode((winwidth, winheight))
assets = create_assets("images", tilewidth, tileheight)
background = create_background(assets, laby, labwidth, labheight, tilewidth, tileheight)

window.blit(background, (0, 0))
pygame.display.flip()

# Boucle principale
continuer = True
while continuer == True:
    # On réaffiche totalement l'écran, en commençant par le fond
    window.blit(background, (0, 0))
    # Puis en traçant les diverses décorations et éléments interactifs
    draw_world(window, world)
    
    pygame.display.flip()

    # puis on gère les événements
    (continuer, inputs) = event_loop()
    
    # et on modifie le monde selon les entrées
    step(world, inputs)

pygame.quit()
