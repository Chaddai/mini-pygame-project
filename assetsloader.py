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
    base = os.path.basename(path)
    (name,ext) = os.path.splitext(base)
    return name
    
def load_asset(path, width, height):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.smoothscale(image, (width, height))
    return image

def create_assets(im_dir):
    im_paths = glob.glob(os.path.join(im_dir, "*.png"))
    assets_dict = dict([(filename(path), load_asset(path, tilewidth, int(scale_factor * 171))) for path in im_paths])
    return assets_dict