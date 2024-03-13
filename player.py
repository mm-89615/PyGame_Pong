import pygame
from pygame.sprite import Sprite

from settings import *


class Player(Sprite):
    """ Класс создания игрока """

    def __init__(self, player, game_screen):
        """ Инициализация игрока """
        super().__init__()
        self.screen = game_screen.screen
        self.player = player
        # Загрузка изображений игроков и размещение на своих местах
        if self.player == 1:
            self.image = pygame.image.load('images/player1.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.center_platform()
        if self.player == 2:
            self.image = pygame.image.load('images/player2.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.center_platform()

    def update(self):
        """ Обновление позиций игроков """
        self.check_player_events()

    def check_player_events(self):
        """ Отслеживание нажатий кнопок игроками """
        keys = pygame.key.get_pressed()
        # Управление первого игрока
        if self.player == 1:
            if keys[pygame.K_RIGHT] and self.rect.top >= 10:
                self.rect.y -= SPEEED_PLAYER
            if keys[pygame.K_LEFT] and self.rect.bottom <= SCREEN_HEIGHT - 10:
                self.rect.y += SPEEED_PLAYER
        # Управление второго игрока
        if self.player == 2:
            if keys[pygame.K_d] and self.rect.top >= 10:
                self.rect.y -= SPEEED_PLAYER
            if keys[pygame.K_a] and self.rect.bottom <= SCREEN_HEIGHT - 10:
                self.rect.y += SPEEED_PLAYER

    def blit(self):
        """ Отрисовка корабля в текущей позиции """
        self.screen.blit(self.image, self.rect)

    def center_platform(self):
        """ Размещение платформ в начальной позиции """
        # Размещение первого игрока слева по центру
        if self.player == 1:
            self.rect.midleft = (0, SCREEN_HEIGHT / 2)
        # Размещение второго игрока справа по центру
        if self.player == 2:
            self.rect.midright = (SCREEN_WIDTH, SCREEN_HEIGHT / 2)
