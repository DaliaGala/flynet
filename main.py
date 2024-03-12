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
    background = Background()
    player = Player()

    bar = pygame.image.load('assets/bottom_bar.png')
    DISPLAY=pygame.display.set_mode((500,400),0,32)
    pygame.display.set_caption('FlyNet')
    pygame.display.set_icon(Player().NetLeft)

    font = pygame.font.Font('assets/fonts/font.ttf', 100)
    font_small = pygame.font.Font('assets/fonts/font.ttf', 25)

    lamp_image = pygame.image.load('assets/lamp_pixel.png').convert_alpha()
    small_lamp = pygame.transform.scale(lamp_image, (40, 40))
    large_lamp = pygame.transform.scale(lamp_image, (120, 120))  # Adjust the scaling as needed

    WHITE = (255,255,255)
    BAR_HEIGHT = 60
    PLAY_AREA_HEIGHT = DISPLAY.get_height() - BAR_HEIGHT

    message_displayed = False
    message_timer = 0
    message_duration = 2  # duration in seconds

    def get_flies(n):
        for i in range(n):
            flies.append(Fly())
        for fly in flies:
            fly.position.xy = random.randrange(0, DISPLAY.get_width() - fly.sprite.get_width()), random.randrange(0, DISPLAY.get_height() - fly.sprite.get_height())

        return flies
    
    def display_msg(msg):
        msg_x = (DISPLAY.get_width() - msg.get_width()) // 2
        msg_y = 353  # Adjust to position within the bottom bar
        DISPLAY.blit(msg, (msg_x, msg_y))

    n = 10
    m = 10
    o = 500
    flies = get_flies(n)
    flyCount = 0
    flyCountSinceLast = 0
    lamps_collected = 0
    small_lamp_positions = []
    LAMP_WIDTH = 28
    lamp_spacing = 5
    bar_right_margin = 20
    player_speed_multiplier = 1

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.velocity.y = -3

        player.position.xy += player.velocity.xy * player_speed_multiplier
        player.velocity.xy += player.acceleration.xy 

        if player.position.y + player.currentNet.get_height() > PLAY_AREA_HEIGHT:
            player.position.y = PLAY_AREA_HEIGHT - player.currentNet.get_height()
        if player.position.x < 0:
            player.velocity.x = 3
            player.currentNet = player.NetRight
        if player.position.x + 20 > DISPLAY.get_width():
            player.velocity.x = -3
            player.currentNet = player.NetLeft
        if player.position.y < 0:
            player.velocity.y = 3

        DISPLAY.fill(WHITE)
        background.position = -player.position.y % background.sprite.get_height()
        DISPLAY.blit(background.sprite.convert(), (0, background.position))
        DISPLAY.blit(background.sprite.convert(), (0, background.position - DISPLAY.get_height()))

        if background.position >= DISPLAY.get_height():
            background.position = 0

        DISPLAY.blit(player.currentNet.convert(), (player.position.x, player.position.y))
        
        for fly in flies:
            if fly.position.y + fly.sprite.get_height() > PLAY_AREA_HEIGHT:
                fly.position.y = PLAY_AREA_HEIGHT - fly.sprite.get_height()
            DISPLAY.blit(fly.sprite.convert(), (fly.position.x, fly.position.y))
            if checkCollisions(player.position.x, player.position.y, player.currentNet.get_width(), player.currentNet.get_height(), fly.position.x, fly.position.y, fly.sprite.get_width(), fly.sprite.get_height()):
                flyCount += 1
                flyCountSinceLast += 1
                fly.position.xy = random.randrange(0, DISPLAY.get_width() - fly.sprite.get_width()), random.randrange(0, PLAY_AREA_HEIGHT - fly.sprite.get_height())

            if flyCountSinceLast >= m:
                flyCountSinceLast = 0
                m = m*2
                lamps_collected += 1
                message_displayed = True
                message_timer = pygame.time.get_ticks()  # Set timer
                if lamps_collected > 3:
                    lamps_collected = 0
                    flyCount += 100
                    small_lamp_positions.clear()
                    message_type = 1
                    flies.clear()
                    flies.extend(get_flies(10))
                else:
                    new_lamp_x = DISPLAY.get_width() - (len(small_lamp_positions) + 1) * (LAMP_WIDTH + lamp_spacing) - bar_right_margin
                    small_lamp_positions.append((new_lamp_x, 348))
                    message_type = 2
                    flies.extend(get_flies(10))

            if flyCount >= o:
                player_speed_multiplier *= 1.5
                o = o*2
                message_displayed = True
                message_timer = pygame.time.get_ticks()  # Set timer
                message_type = 3

        DISPLAY.blit(bar, (10, 340))
        flyCountDisplay = font_small.render(str(flyCount).zfill(7), True, (0, 0, 0))
        y = DISPLAY.get_height() - BAR_HEIGHT / 2 - flyCountDisplay.get_height() / 2  # Center vertically within the bottom bar
        DISPLAY.blit(flyCountDisplay, (70, y))
        scaled_fly_sprite = pygame.transform.scale(fly.sprite, (50, 50))
        y = DISPLAY.get_height() - BAR_HEIGHT / 2 - scaled_fly_sprite.get_height() / 2  # Center vertically within the bottom bar
        DISPLAY.blit(scaled_fly_sprite, (20, y))

        if message_displayed:
            if message_type == 1:
                msg = font_small.render("ZAPPED", True, (0, 0, 255))
                lamp_x = (DISPLAY.get_width() - large_lamp.get_width()) // 2
                lamp_y = (DISPLAY.get_height() - large_lamp.get_height()) // 2
                DISPLAY.blit(large_lamp, (lamp_x, lamp_y))
                display_msg(msg)
            elif message_type == 2:
                msg = font_small.render("MORE FLIES!", True, (255, 0, 0))
                display_msg(msg)
            else:
                msg = font_small.render("EXTRA SPEED", True, (0, 255, 0))
                display_msg(msg)

            if pygame.time.get_ticks() - message_timer > message_duration * 1000:
                message_displayed = False

        for pos in small_lamp_positions:
            DISPLAY.blit(small_lamp, pos)

        pygame.display.update()
        pygame.time.delay(10)
        clock.tick(100)

main()