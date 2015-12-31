# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:53:51 2015

@author: chaddai
"""

# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os.path
from constants import *
from labyrinthes import fabrique_labyrinthe
from assetsloader import create_assets
from worlddrawing import create_background, draw_world
from worldmanager import step, event_loop, random_position


# Initialisation du monde
laby = fabrique_labyrinthe(labwidth, labheight)

world = {'character position' : random_position(laby, "Character Boy")}

# Initialisation de la librairie
pygame.init()

# Création de la fenêtre et du labyrinthe en arrière plan
window = pygame.display.set_mode((winwidth, winheight))
assets = create_assets("images")
background = create_background(assets, laby)

window.blit(background, (0, 0))
pygame.display.flip()

# Boucle principale
continuer = True
while continuer == True:
    # On réaffiche totalement l'écran, en commençant par le fond
    window.blit(background, (0, 0))
    # Puis en traçant les diverses décorations et éléments interactifs
    draw_world(window, world, assets)
    
    pygame.display.flip()

    # puis on gère les événements
    (continuer, inputs) = event_loop()
    
    # et on modifie le monde selon les entrées
    step(world, inputs)

pygame.quit()
