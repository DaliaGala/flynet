#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:08:41 2021

@author: daliagala
"""

import pygame

class Player:
    position = pygame.Vector2(100, 100)
    velocity = pygame.Vector2(3, 0)
    acceleration = pygame.Vector2(0, 0.01)
    rightSprite = pygame.image.load("/Users/daliagala/Documents/flynet/Net_pixel.gif")
    leftSprite = pygame.transform.flip(rightSprite, True, False)
    currentSprite = rightSprite