#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

bkg_file = "/home/cxy/game/images/sushiplate.jpg"
bkg_img = pygame.image.load(bkg_file).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            print str(event.key)
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    
    screen.blit(bkg_img,(0,0))
    pygame.display.update()