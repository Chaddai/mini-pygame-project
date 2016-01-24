# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:53:51 2015

@author: chaddai
"""

import pygame
import constants
import gameworld
from labyrinthes import fabrique_labyrinthe
from assetsloader import create_assets

##### Initialisation de la librairie pygame #####

pygame.init()
window = pygame.display.set_mode((constants.winwidth, constants.winheight))
pygame.key.set_repeat(200, 200)


##### Initialisation du monde #####

laby = fabrique_labyrinthe(constants.labwidth, constants.labheight)

# Le monde est décrit dans un dictionnaire, la clé "objects" contient un
# dictionnaire de tous les éléments de premier plan (dont le joueur, le PC)
world = {
    'laby': laby,
    'objects': {},
    # initialiser le score à 0 pour tous les bonus possibles
    'score': {bonus_name: 0 for bonus_name in constants.bonus_sprites},
    'bonus map': None,
    'background': None
}

# Création et placement des bonus sur la carte
(bonus_map, bonus) = gameworld.create_bonus(laby, 10)
world['bonus map'] = bonus_map
# On ajoute les bonus dans la liste des objets
world['objects'].update(bonus)

# On positionne le joueur sur une position libre
world['objects']['pc'] = {
    'lpos': constants.random_free_position(world['bonus map']),
    'sprite': "Character Boy"
}

# Chargement des images ressources dans un dictionnaire qui à
# chaque nom de fichier (sans extension) associe l'image
# correctement redimensionnée
assets = create_assets("images")

# On crée l'arrière-plan et on en profite pour générer les
# "décorations" comme les arbres et les rochers...
(background, decos) = gameworld.create_background(laby, assets)
world['background'] = background
# ...qu'on ajoute alors aux objets d'avant plan dans le monde
world['objects'].update(decos)


##### Boucle principale #####

continuer = True
while continuer:
    # On dessine le monde
    gameworld.draw_world(window, world, assets)
    pygame.display.flip()

    # puis on gère les événements
    (continuer, inputs) = gameworld.event_handler()

    # et on modifie le monde selon les entrées
    gameworld.step(world, inputs)

pygame.quit()
