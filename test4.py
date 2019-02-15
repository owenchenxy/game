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

my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')
pygame.event.post(my_event)

while True:
    for event in pygame.event.get():
        print str(event)