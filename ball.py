import random
from random import choice

import pygame
from pygame.sprite import Sprite

from settings import *


class Ball(Sprite):
    """ Класс создания мяча """

    def __init__(self, game_screen):
        """ Инициализация параметров мяча """
        super().__init__()
        self.screen = game_screen.screen
        # Загрузка изображения мяча и размещение в центре
        self.image = pygame.image.load('images/ball2.png')
        self.rect = self.image.get_rect()
        self.ball_on_center()
        # Случайное направление движения мяча при старте
        self.random_start()

    def update(self):
        """ Обновление позиции мяча """
        # Движение мяча по Х и Y
        self.rect.x += SPEEED_BALL * self.direction_x
        self.rect.y += SPEEED_BALL * self.direction_y
        # Отслеживание столкновений сверху и снизу
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_direction_y()


    def blit(self):
        """ Отрисовка мяча """
        self.screen.blit(self.image, self.rect)

    def ball_on_center(self):
        """ Координаты центра для мяча """
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def change_direction_x(self):
        """ Смена направления по Х при ударе """
        self.direction_x *= -1

    def change_direction_y(self):
        """ Смена направления по Y при ударе """
        self.direction_y *= -1

    def random_start(self):
        """ Выбор случайного направления """
        self.direction_x = random.choice([1, -1])
        self.direction_y = random.choice([1, -1])
