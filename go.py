"""
Описание классов игровых объектов: мяча
"""

import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self, img, initpos, speed):
        super().__init__()                          # инициализация родительского класса
        self.img = pg.image.load(img).convert()     # загрузка изображения мяча    
        self.rect = self.img.get_rect()             # снимаем прямоугольник для мяча
        self.rect.move_ip(initpos)                  # помещаем прямоугольник мяча в указанное место
        self.mask = pg.mask.from_surface(self.img)  # снимаем маску с мяча
        self.speed = speed                          # скорость мяча

class Sled(pg.sprite.Sprite):
	def __init__(self, img, initpos, speed):
		super().__init__()
		self.img = pg.image.load(img).convert()
		self.rect = self.img.get_rect()
		self.rect.move_ip(initpos)
		self.mask = pg.mask.from_surface(self.img)
		self.speed = speed
