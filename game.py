#!/usr/bin/env python3
import pygame, sys, random
from pygame.locals import *
from player import Player
from fly import Fly
from background import Background
from tools import checkCollisions

pygame.init()
clock = pygame.time.Clock()

def main():
    DISPLAY = pygame.display.set_mode((500,400),0,32)
    pygame.display.set_caption('FlyNet')

    flies, small_lamp_positions, flyCount, lamps_collected, message_displayed = [], [], 0, 0, False
    bar, lamp_image, player, background = setup_game(DISPLAY)

    while True:
        process_events(player)
        update_player_position(player, DISPLAY.get_height())
        DISPLAY.fill((255,255,255))
        draw_background(DISPLAY, background, player)
        handle_flies(flies, player, DISPLAY, flyCount, lamps_collected, message_displayed)
        draw_ui(DISPLAY, bar, player, flyCount, flies, small_lamp_positions)
        pygame.display.update()
        pygame.time.delay(10)
        clock.tick(100)

def setup_game(DISPLAY):
    bar = pygame.image.load('assets/bottom_bar.png')
    lamp_image = pygame.image.load('assets/lamp_pixel.png').convert_alpha()
    return bar, lamp_image, Player(), Background()

def process_events(player):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.velocity.y = -3

def update_player_position(player, play_area_height):
    # Update player position and velocity here

def draw_background(DISPLAY, background, player):
    # Code to draw the background here

def handle_flies(flies, player, DISPLAY, flyCount, lamps_collected, message_displayed):
    # Code to handle flies, collision, and updating game state here

def draw_ui(DISPLAY, bar, player, flyCount, flies, small_lamp_positions):
    # Code to draw the user interface here

if __name__ == "__main__":
    main()