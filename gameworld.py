# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:29:48 2015

@author: chaddai
"""

import pygame
from pygame.locals import *
from constants import *
from random import choice

##### Creating the world #####

def create_bonus(laby, n):
    """Positionne aléatoirement des bonus à des positions valides du labyrinthe,
    retourne leurs positions et les objets créés"""

    # initialise la carte des bonus à partir du labyrinthe (mais fait une copie en
    # profondeur pour éviter de modifier le labyrinthe dans la suite)
    bonus_map = [list(line) for line in laby]
    bonus_objects = {}
    for i in range(n):
        # id du bonus : b + 3 chiffres
        name = 'b%03d' % i
        (x, y) = random_free_position(bonus_map)
        # la carte des bonus indique l'id à l'emplacement du bonus
        bonus_map[y][x] = name
        bonus_objects[name] = {'lpos': (x, y), 'sprite': choice(bonus_sprites)}
    return (bonus_map, bonus_objects)

def create_background(laby, assets):
    """Crée l'image d'arrière-plan et la retourne, accompagnée des décorations
    nécessaires au premier-plan"""

    # teste si une case impassable est isolée dans le labyrinthe
    def isolated(x, y):
        for (dx, dy) in directions.values():
            (nx, ny) = (x+dx, y+dy)
            if 0 <= nx < labwidth and 0 <= ny < labheight and laby[ny][nx] == 1:
                return False
        return True

    bg = pygame.Surface((winwidth, winheight))
    deco = {}
    decocount = 0

    # peuplement de l'arrière plan par des blocs de terrain
    for y in range(labheight):
        for x in range(labwidth):
            # par défaut de l'herbe
            land = "Grass Block"
            if laby[y][x] == 1:
                # de l'eau si le labyrinthe est impassable
                land = "Water Block"
                if isolated(x, y):
                    # de la terre si la case est isolée
                    land = "Dirt Block"
                    decocount += 1
                    # sur laquelle on ajoute d'un élément de décoration avec l'id
                    # d + le compte des décorations jusqu'ici sur 3 chiffres
                    deco["d%03d" % decocount] = {'lpos': (x, y), 'sprite': choice(deco_sprites)}
            tile = assets[land]

            # placement de la tuile en position x y
            bg.blit(tile, laby_to_screen(x, y, land))
    return (bg, deco)


##### Drawing the world #####

def draw_world(window, world, assets):
    """Dessine le monde dans la fenêtre passée, à l'aide des ressources en paramètre"""

    # retourne la coordonnée y d'un objet
    def ypos(obj):
        (name, prop) = obj

        # si la position graphique n'existe pas, la calculer depuis
        # la position dans le labyrinthe
        if 'pos' not in prop:
            (x, y) = prop['lpos']
            prop['pos'] = laby_to_screen(x, y, prop['sprite'])

        return prop['pos'][1]


    # On commence par le fond, le terrain (parce qu'il est plat)
    window.blit(world['background'], (0, 0))

    # Puis on ajoute les objets de premier plan dans l'ordre croissant
    # de coordonnée y pour éviter les superpositions erronées
    for (name, prop) in sorted(world['objects'].items(), key=ypos):
        window.blit(assets[prop['sprite']], prop['pos'])

    # Et finalement on dessine le score dans le coin en haut à gauche
    render_score(window,world, assets, 0, 0)

def render_score(window,world, assets, x, y):
    """Dessine le score stocké dans le monde aux coordonnées (x,y) de la fenêtre"""

    # réduction appliquée aux icônes du score par rapport aux bonus sur la carte
    scale_score = 0.5
    count = len(bonus_sprites)

    # on utilisera la police "ComicSans", le summum du goût en typographie...
    font = pygame.font.SysFont('ComicSans', 50, bold=True)

    # on dessine le score sur une surface transparente
    score_im = pygame.Surface((count*tilewidth, 2*count*tileheight), flags=SRCALPHA)
    score_im.fill((255, 255, 255, 0))

    # pour chacun des types de bonus
    for j in range(count):
        sprite = bonus_sprites[j]
        # on écrit sur une tuile le nombre de bonus capturés
        score_im.blit(font.render("%d ×" % world['score'][sprite], True,
                                  (255, 255, 255, 0)), (0, (j*2+1)*tileheight))
        # et sur la tuile à côté on représente le type de bonus
        score_im.blit(assets[sprite], laby_to_screen(1, 1+j*2, sprite))

    # puis on réduit le score pour qu'il ne gêne pas le jeu
    score_im = pygame.transform.smoothscale(score_im,
                                        (int(scale_score*score_im.get_width()),
                                         int(scale_score*score_im.get_height())))

    # et on le recopie aux coordonnées (x,y) de la fenêtre
    window.blit(score_im, (x, y))


##### Managing the world #####

def step(world, inputs):
    """Une étape de la simulation du monde"""
    pc = world['objects']['pc']

    # on déplace le joueur selon les entrées
    (lx, ly) = pc['lpos']
    (dx, dy) = inputs
    (nx, ny) = (lx+dx, ly+dy)

    # mais uniquement s'il aboutit sur une case valide
    if pos_valid(world, nx, ny):
        pc['lpos'] = (nx, ny)
        # la position d'affichage du joueur doit être invalidée
        # elle sera regénérée à partir de sa position dans le labyrinthe
        del pc['pos']

        # les éventuels bonus sur la case d'arrivée sont récoltés
        bonus_name = world['bonus map'][ny][nx]
        if type(bonus_name) == str:
            world['bonus map'][ny][nx] = 0
            # en plus de retourner le bonus, pop() le supprime du dictionnaire
            bonus = world['objects'].pop(bonus_name)
            world['score'][bonus['sprite']] += 1

def event_handler():
    """Gère les évènements, principalement clavier pour l'instant"""
    continuer = True
    delta = (0, 0)
    for event in pygame.event.get():
        # On gère le clic sur la croix et la touche ECHAP pour quitter
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
            elif event.key in directions.keys():
                # Une des touches du pavé numérique a été enfoncée. On
                # déplace le joueur dans la direction adéquate
                delta = directions[event.key]

    return (continuer, delta)
