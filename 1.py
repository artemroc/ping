#!/usr/bin/env python3

import pygame as pg
from pygame.locals import *
from go import Ball # игровые объекты
from go import Sled

pg.init()

FPS  = 60
SIZE = width, height = 640, 480
BGCOLOR = 90, 90, 90

screen = pg.display.set_mode(SIZE)         # создаём окошко
clock  = pg.time.Clock()                   # создаем таймер

ball = Ball("ball.png", (50, 20), [4, 4])  # создаём мяч
sled = Sled("sled.png", (20, 0), [0,0])    # создаем платформу

again = True
while again:
    for event in pg.event.get():
        if event.type == pg.QUIT: again = False
    
    # логика перемещения платформы
    pressed = pg.key.get_pressed() # вернем все зажатые клавиши
    if pressed[pg.K_UP]:
        sled.speed[1] = -2 if sled.rect.top >= 0 else 0
    elif pressed[pg.K_DOWN]:
        sled.speed[1] = 2 if sled.rect.bottom <= height else 0
    else: sled.speed[1] = 0

    # логика столкновения мяча с платформой
    if sled.rect.colliderect(ball.rect):
        ball.speed[0] = -ball.speed[0]

    # логика отскока мяча от границ экрана
    if ball.rect.left < 0 or ball.rect.right > width:
        ball.speed[0] = -ball.speed[0]
    if ball.rect.top < 0 or ball.rect.bottom > height:
        ball.speed[1] = -ball.speed[1]
        
    sled.rect = sled.rect.move(sled.speed)    # сдвинуть прямоугольник платформы
    ball.rect = ball.rect.move(ball.speed) # сдвинуть прямоугольник мяча

    # отрисовка изображений
    screen.fill(BGCOLOR)
    screen.blit(sled.img, sled.rect)
    screen.blit(ball.img, ball.rect)

    pg.display.update()
    clock.tick(FPS)

# выход из программы
pg.quit()
