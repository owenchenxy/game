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

x,y = 0,0
move_x, move_y = 0, 0

while True:
    # 按下键盘的瞬间得到一个event，进入for循环，按下键盘期间不产生事件，不进入for循环
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1

        elif event.type == KEYUP:
            move_x, move_y = 0, 0

    #按下键盘后如果没有放开，move_*的值将不会变回0

    x += move_x
    y += move_y

    screen.fill((0,0,0))
    screen.blit(bkg_img, (x,y))
    pygame.display.update()
