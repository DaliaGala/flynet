#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:19:29 2021

@author: daliagala
"""

import pygame
class Fly:
    def __init__(self):
        self.sprite = pygame.image.load("assets/Fly_pixel.gif")
        self.position = pygame.Vector2()
        self.position.xy