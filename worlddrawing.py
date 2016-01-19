# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:29:48 2015

@author: chaddai
"""

import pygame
from constants import *
from random import choice
    
def draw_world(window, world, assets):
    """Dessiner le monde dans la fenêtre passée, à l'aide des ressources"""

    # retourne la coordonnée y d'un objet
    def ypos(obj): 
        (name, prop) = obj

        # si la position graphique n'existe pas, la calculer depuis 
        # la position dans le labyrinthe
        if 'pos' not in prop: 
            (x,y) = prop['lpos']
            prop['pos'] = laby_to_screen(x,y,prop['sprite'])

        return prop['pos'][1]
    
    
    # On commence par le fond, le terrain (parce qu'il est plat)
    window.blit(world['background'], (0, 0))

    # Puis on ajoute les objets de premier plan dans l'ordre croissant 
    # de coordonnée y pour éviter les superpositions erronées
    for (name,prop) in sorted(world['objects'].items(), key=ypos):
        window.blit(assets[prop['sprite']], prop['pos'])
    render_score(window,world,assets,0,0)

def render_score(window,world,assets,x,y):
    """Dessine le score stocké dans le monde aux coordonnées (x,y) de la fenêtre"""

    # réduction appliquée aux icônes du score par rapport aux bonus sur la carte
    scale_score=0.5
    count = len(bonus_sprites)

    # on utilisera la police "ComicSans", le summum du goût en typographie...
    font = pygame.font.SysFont('ComicSans', 50, bold=True)

    # on dessine le score sur une surface transparente
    score_im = pygame.Surface((count*tilewidth, 2*count*tileheight), flags=SRCALPHA)
    score_im.fill((255,255,255,0))

    # pour chacun des types de bonus
    for j in range(count):
        sprite = bonus_sprites[j]
        # on écrit sur une tuile le nombre de bonus capturés
        score_im.blit( font.render( "%d ×" % world['score'][sprite], True, (255,255,255,0) ), (0, (j*2+1)*tileheight) )
        # et sur la tuile à côté on représente le type de bonus
        score_im.blit( assets[sprite], laby_to_screen(1,1+j*2,sprite) )

    # puis on réduit le score pour qu'il ne gêne pas le jeu
    score_im = pygame.transform.smoothscale(score_im, ( int(scale_score*score_im.get_width()), int(scale_score*score_im.get_height()) ) )

    # et on le recopie aux coordonnées (x,y) de la fenêtre
    window.blit(score_im,(x,y))
