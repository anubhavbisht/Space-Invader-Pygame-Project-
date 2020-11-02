import pygame
from pygame.locals import *
import os
import time
import random

width, height = 750, 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("m@jin XX space XX invader")

redspaceship = pygame.image.load(
    os.path.join("images", "pixel_ship_red_small.png"))
bluespaceship = pygame.image.load(
    os.path.join("images", "pixel_ship_blue_small.png"))
greenspaceship = pygame.image.load(
    os.path.join("images", "pixel_ship_green_small.png"))
yellowspaceship = pygame.image.load(
    os.path.join("images", "pixel_ship_yellow.png"))
redlaser = pygame.image.load(os.path.join("images", "pixel_laser_red.png"))
greenlaser = pygame.image.load(os.path.join("images", "pixel_laser_green.png"))
bluelaser = pygame.image.load(os.path.join("images", "pixel_laser_blue.png"))
yellowlaser = pygame.image.load(
    os.path.join("images", "pixel_laser_yellow.png"))
background = pygame.image.load(os.path.join("images", "background-black.png"))


def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
