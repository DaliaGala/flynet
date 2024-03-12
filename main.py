#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys, random
from player import Player
from fly import Fly
from background import Background
from tools import checkCollisions

pygame.init()
clock = pygame.time.Clock()

def main():
    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('FlyNet')
    pygame.display.set_icon(Player().NetLeft)

    background = Background()
    player = Player()
    bar = pygame.image.load('assets/bottom_bar.png')
    lamp_image = pygame.image.load('assets/lamp_pixel.png').convert_alpha()
    small_lamp = pygame.transform.scale(lamp_image, (25, 25))
    font_small = pygame.font.Font('assets/fonts/font.ttf', 32)
    WHITE = (255, 255, 255)
    BAR_HEIGHT = 50
    PLAY_AREA_HEIGHT = DISPLAY.get_height() - BAR_HEIGHT

    flies = [Fly() for _ in range(10)]
    flyCount = 0
    flyCountSinceLast = 0
    lamps_collected = 0
    small_lamp_positions = []  # List to store positions of small lamps
    LAMP_WIDTH = 25  # Width of a small lamp
    lamp_spacing = 5  # Space between lamps
    bar_right_margin = 20  # Space from the right edge of the screen
    player_speed_multiplier = 1  # Multiplier for player speed
    for fly in flies:
        fly.position.xy = random.randrange(0, DISPLAY.get_width() - fly.sprite.get_width()), random.randrange(0, DISPLAY.get_height() - fly.sprite.get_height())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.velocity.y = -3

        player.position.xy += player.velocity.xy
        player.velocity.xy += player.acceleration.xy * player_speed_multiplier

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
        background.position += 1
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

        if flyCountSinceLast >= 10:
            flyCountSinceLast = 0  # Reset fly count for next bonus
            lamps_collected += 1  # Increment lamp collection

            # Check if 3 lamps collected to increase player's speed
            if lamps_collected > 3:
                player_speed_multiplier *= 1.00005
                lamps_collected = 0  # Reset lamps collected
                small_lamp_positions.clear()  # Clear lamp display
                flies = [Fly() for _ in range(10)] # Reset flies
            else:
                # Calculate new lamp position and add it to the list
                new_lamp_x = DISPLAY.get_width() - (len(small_lamp_positions) + 1) * (LAMP_WIDTH + lamp_spacing) - bar_right_margin
                small_lamp_positions.append((new_lamp_x, 350))
                # Add 10 more flies for each lamp collected
                for _ in range(10):
                    flies.append(Fly())

        flyCountDisplay = font_small.render(str(flyCount).zfill(7), True, (0, 0, 0))
        DISPLAY.blit(bar, (10, 340))
        DISPLAY.blit(flyCountDisplay, (50, 350))

        for pos in small_lamp_positions:
            DISPLAY.blit(small_lamp, pos)

        pygame.display.update()
        pygame.time.delay(10)
        clock.tick(100)

main()