#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:08:41 2021

@author: daliagala
"""

import pygame

class Player:
    position = pygame.Vector2(100, 100)
    velocity = pygame.Vector2(1, 0)
    acceleration = pygame.Vector2(0, 0.1)
    NetLeft = pygame.image.load("assets/Net_pixel.gif")
    NetRight = pygame.transform.flip(NetLeft, True, False)
    currentNet = NetLeft