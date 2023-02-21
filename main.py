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
from tools import checkCollisions

pygame.init()
clock = pygame.time.Clock()

        
def main():
    flies = []
    buttons = []
    background = Background()
    player = Player()
    bar = pygame.image.load('assets/bottom_bar.png')
    DISPLAY=pygame.display.set_mode((500,400),0,32)
    pygame.display.set_caption('FlyNet')
    pygame.display.set_icon(Player().NetLeft)
    font = pygame.font.Font('assets/fonts/font.ttf', 100)
    font_small = pygame.font.Font('assets/fonts/font.ttf', 32)
    WHITE=(255,255,255)
    # getting 5 flies
    for i in range(10): flies.append(Fly())
    # now looping through the flies list
    for fly in flies:
        fly.position.xy = random.randrange(0, DISPLAY.get_width() - fly.sprite.get_width()), random.randrange(0, DISPLAY.get_height() - fly.sprite.get_height())
    #defining some game variables
    flyCount = 0
#get fonts
#get some images remember .convert()
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
        background.position += 1
        DISPLAY.blit(background.sprite.convert(), (0, background.position))
        DISPLAY.blit(background.sprite.convert(), (0, background.position - DISPLAY.get_height()))
        if background.position >= DISPLAY.get_height():
            background.position = 0
        DISPLAY.blit(player.currentNet.convert(), (player.position.x, player.position.y))
        
        for fly in flies:
            DISPLAY.blit(fly.sprite.convert(), (fly.position.x, fly.position.y))
            if (checkCollisions(player.position.x, player.position.y, player.currentNet.get_width(), player.currentNet.get_height(), fly.position.x, fly.position.y, fly.sprite.get_width(), fly.sprite.get_height())):
                flyCount += 1
                fly.position.xy = random.randrange(0, DISPLAY.get_width() - fly.sprite.get_width()), random.randrange(0, DISPLAY.get_height() - fly.sprite.get_height())
                print("collision, fly number:",flyCount)
        flyCountDisplay = font_small.render(str(flyCount).zfill(7), True, (0,0,0))
        DISPLAY.blit(bar, (10, 340))
        DISPLAY.blit(flyCountDisplay, (50, 350))
        DISPLAY.blit(fly.sprite, (20, 350))
        pygame.display.update()
        pygame.time.delay(10)
        clock.tick(100)
main()