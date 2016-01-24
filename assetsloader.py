# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:55:52 2015

@author: chaddai
"""

import glob
import os.path
import pygame
from constants import *

def filename(path):
    """Nettoie un chemin pour ne garder que le nom du fichier, sans l'extension"""
    base = os.path.basename(path)
    (name, ext) = os.path.splitext(base)
    return name

def load_asset(path, width, height):
    """Charge et réduit aux dimensions prescrites un fichier image pris en charge par pygame"""
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.smoothscale(image, (width, height))
    return image

def create_assets(im_dir):
    """Retourne un dictionnaire qui à chaque nom de fichier (sans l'extension)
    associe l'image correspondante"""

    # une liste de tous les fichiers d'extension .png dans le dossier im_dir
    im_paths = glob.glob(os.path.join(im_dir, "*.png"))
    assets_dict = {filename(path): load_asset(path, tilewidth, int(scale_factor * 171)) for path in im_paths}
    return assets_dict
