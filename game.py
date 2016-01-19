# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:53:51 2015

@author: chaddai
"""

import pygame
from pygame.locals import *
import os.path
from constants import *
from labyrinthes import fabrique_labyrinthe
from assetsloader import create_assets
from worlddrawing import create_background, draw_world
from worldmanager import step, event_loop


##### Initialisation du monde #####

laby = fabrique_labyrinthe(labwidth, labheight)

# Création et placement des bonus sur la carte
(tm, ts) = create_treasure_map(laby, 10)
objs = {'pc' : {'lpos' : random_position(laby), 'sprite': "Character Boy"}}
# On ajoute les bonus dans la liste des objets 
objs.update(ts)

# Le monde est décrit dans un dictionnaire, la clé "objects" contient un 
# dictionnaire de tous les éléments de premier plan (dont le joueur)
world = {
    'laby' : laby,
    'treasures' : tm,
    'objects' : objs,
    'score' : dict([(cat, 0) for cat in treasure_sprites])
}


##### Initialisation de la librairie pygame #####

pygame.init()
window = pygame.display.set_mode((winwidth, winheight))


##### Création du labyrinthe en arrière plan #####

# Chargement des images ressources dans un dictionnaire qui à
# chaque nom de fichier (sans extension) associe l'image
# correctement redimensionnée
assets = create_assets("images")

# On crée l'arrière-plan et on en profite pour générer les 
# "décorations" comme les arbres et les rochers...
(background, decos) = create_background(assets, laby)
# ...qu'on ajoute alors aux objets d'avant plan dans le monde
world['objects'].update(decos)


##### Boucle principale #####

window.blit(background, (0, 0))
pygame.display.flip()

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
    step(laby, world, inputs)

pygame.quit()
