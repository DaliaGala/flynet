#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:54:46 2021

@author: daliagala
"""

import pygame
class Background:
    def __init__(self):
        self.sprite = pygame.image.load('assets/background.jpg')
        self.position = 0