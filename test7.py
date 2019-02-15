#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import pygame
from pygame.locals import *
from sys import exit
 
SCREEN_SIZE = (640, 480)
 
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

font = pygame.font.SysFont("simsunnsimsun",40)
text_surface = font.render(u'hello world', True, (0,0,255))

x=0
y=text_surface.get_height()/2

while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    x -= 0.1
    if x < -text_surface.get_width():
        x = 640
    screen.fill((255,255,255))
    screen.blit(text_surface,(x, y))
    
    pygame.display.update()