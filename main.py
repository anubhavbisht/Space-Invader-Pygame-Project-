import pygame
import os
import time
import random
pyagame.font.init()

width, height = 700, 700
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
background = pygame.transform.scale(pygame.image.load(os.path.join("images", "background-black.png")),(width,height))


def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()
    level=1
    lives=5
    mainfont=pygame.font.SysFont("comicsans",50)
    def redrawwindow():
        win.blit(background,(0,0))
        liveslabel=mainfont.render(f "Live:{lives}",1,(255,255,255))
        levelslabel=mainfont.render(f "Level:{levels}",1,(255,255,255))
        win.blit(liveslabel,(0,0))
        win.blit(levelslabel,(width,0))
        pygame.display.update()
    while run:
        clock.tick(fps)
        redrawwindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()
