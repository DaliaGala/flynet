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
from background import Background

pygame.init()
clock = pygame.time.Clock()

def main():
    flies = []
    buttons = []
    background = Background()
    player = Player()
    DISPLAY=pygame.display.set_mode((500,400),0,32)
    pygame.display.set_caption('FlyNet')
    pygame.display.set_icon(Fly().sprite)
    WHITE=(255,255,255)
    # getting 5 flies
    for i in range(5): flies.append(Fly())
    # now looping through the beans list
    for fly in flies:
        fly.position.xy = random.randrange(0, DISPLAY.get_width() - fly.sprite.get_width()), flies.index(fly)*-200 - player.position.y
        
    
#get fonts
#get some images
#get sounds
#colors
#variables
#creating Player object
#creating flies and buttons list  
#Main game loop
#Events
#Update game elements
#Draw surface
#Show surface
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.velocity.y = -3
        player.position.xy += player.velocity.xy
        player.velocity.xy += player.acceleration.xy
        if player.position.x < 0:
            player.velocity.x = 3
            player.currentNet = player.NetRight
        if player.position.x + 20 > DISPLAY.get_width():
            player.velocity.x = -3
            player.currentNet = player.NetLeft
        if player.position.y < 0:
            player.velocity.y = 3
        if player.position.y + 30 > DISPLAY.get_height():
            player.velocity.y = -3
        DISPLAY.fill(WHITE)
        DISPLAY.blit(background.sprite, (background.position, background.position))
        DISPLAY.blit(player.currentNet, (player.position.x, player.position.y))
        
        for fly in flies:
            DISPLAY.blit(fly.sprite, (fly.position.x, fly.position.y))
        pygame.display.update()
        pygame.time.delay(10)
        clock.tick(100)
main()