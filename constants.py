# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:42:37 2015

@author: chaddai
"""

from random import randint
from pygame.locals import *


##### Constantes ajustables #####

# Attention, ces largeurs et hauteurs doivent être impaires
labwidth = 15
labheight = 15

# Ajustez seulement la largeur, la hauteur sera automatiquement ajustée selon
# les dimensions du labyrinthe et l'aspect des tuiles de terrain
winwidth = 750

# la liste des bonus possibles
bonus_sprites = ['Star', 'Heart']

# la liste des décorations possibles
deco_sprites = ['Rock', 'Tree Short', 'Tree Tall', 'Tree Ugly']

# les coordonnées dans l'image ressource qui doivent se retrouver au centre de la tuile
assets_center = {
    'Character Boy': (50, 140),
    'Grass Block': (50, 90),
    'Water Block': (50, 90),
    'Dirt Block': (50, 90),
    'Rock': (50, 135),
    'Tree Short': (50, 135),
    'Tree Tall': (50, 135),
    'Tree Ugly': (50, 135),
    'Star': (50, 125),
    'Heart': (50, 125)
}


##### Quelques fonctions utilitaires #####

def laby_to_screen(x, y, assetname):
    """Traduit une position dans le labyrinthe en coordonnées absolue
    dans la fenêtre. Le nom de la ressource est nécessaire pour un ajustement
    fin"""

    # par défaut on considère que le centre d'une tuile est aux coordonnée (50.5, 140)
    # mais on privilégie les données dans le dictionnaire assets_center
    (xc, yc) = assets_center.get(assetname, (50.5, 140))

    # Ceci correspond à une translation de scale_factor*(xc,yc) au centre de la tuile
    # de coordonnées (x, y) dans la fenêtre
    return (int(x*tilewidth+tilewidth/2 - scale_factor*xc)
            , int(y*tileheight+tileheight/2 - scale_factor*yc))

def random_free_position(laby):
    """Retourne une position aléatoire complètement vide d'après l'argument passé"""
    while True:
        (x, y) = (randint(1, labwidth-2), randint(1, labheight-2))
        if laby[y][x] == 0:
            return (x, y)

def pos_valid(world, x, y):
    """Vérifie si une position est accessible pour le joueur"""
    return (0 <= x < labwidth
            and 0 <= y < labheight
            and world['bonus map'][y][x] != 1)


##### Constantes à ne pas toucher #####

# générées automatiquement ou d'après les fichiers images
tilehwscale = 80/101
winheight = int(labheight / labwidth * tilehwscale * winwidth)
tilewidth = winwidth // labwidth
tileheight = int(tilehwscale * tilewidth)
scale_factor = tilewidth / 101

# dictionnaire associant à une touche du pavé numérique le déplacement correspondant
directions = {
    K_KP1: (-1, 1),
    K_KP2: (0, 1),
    K_KP3: (1, 1),
    K_KP4: (-1, 0),
    K_KP6: (1, 0),
    K_KP7: (-1, -1),
    K_KP8: (0, -1),
    K_KP9: (1, -1),
}
