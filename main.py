#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:07:34 2021

@author: daliagala
"""
import pygame, sys, time, random, colorsys, math
from pygame.math import Vector2
from pygame.locals import *
from player import Player
from fly import Fly

def main():
    player = Player()
    DISPLAY=pygame.display.set_mode((500,400),0,32)
    pygame.display.set_caption('FlyNet')
    pygame.display.set_icon(Fly().sprite)
    WHITE=(255,255,255)
    
#get fonts
#get some images
#get sounds
#colors
#variables
#creating Player object
    player = Player()
#creating flies and buttons list 
    flies = [] 
    buttons = []


    
# Main game loop
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.velocity.y = -1
        player.position.xy += player.velocity.xy
        player.velocity.xy += player.acceleration.xy
        if player.position.x < 0:
            player.velocity.x = 1
        if player.position.x + 100 > DISPLAY.get_width():
            player.velocity.x = -0.1
        if player.position.y < 0:
            player.velocity.y = 1
        if player.position.y +20> DISPLAY.get_height():
               player.velocity.y = -1
        DISPLAY.fill(WHITE)
        DISPLAY.blit(player.rightSprite, (player.position.x, player.position.y))
        pygame.display.update()

main()