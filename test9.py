#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
 
screen = pygame.display.set_mode((640, 480), 0, 32)
 
color1 = (221, 99, 20)
color2 = (96, 130, 51)
factor = 0.

def blend_color(color1, color2, blend_factor):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = int(r1 + (r2 -r1) * blend_factor)
    g = int(g1 + (g2 -g1) * blend_factor)
    b = int(b1 + (b2 -b1) * blend_factor)
    return (r, g, b)

control_surface = pygame.surface.Surface((640,80))
control_surface.fill((255,255,255))

result_surface = pygame.surface.Surface((640,400))
color = (127, 127, 127)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if y > 0 and y < 80:
            blend_factor = x/640.
            color = blend_color(color1, color2, blend_factor)
            control_surface.fill((255,255,255))
            pygame.draw.circle(control_surface, (0,0,0), (x,40), 20)
    
    result_surface.fill(color)
    screen.blit(control_surface,(0,0))
    screen.blit(result_surface,(0,80))
    pygame.display.update()