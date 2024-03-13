import pygame

from settings import *


class GameMenu:
    """ Класс создания меню паузы """

    def __init__(self, game_screen):
        """ Инициализация меню паузы """
        # Параметры фона паузы
        self.screen = game_screen.screen
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.surface.set_alpha(BG_PAUSE_ALPHA)
        self.surface.fill(BG_PAUSE_COLOR)
        # Текст на экране
        self.menu_font = pygame.font.Font('fonts/KodeMono.ttf', FONS_SIZE_PAUSE_MENU)
        self.menu_text = self.menu_font.render(f"PAUSE GAME", True, MENU_TEXT_COLOR)
        self.menu_rect = self.menu_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        # Игра на паузе
        self.game_paused = False

    def is_pause(self):
        # Отрисовка меню
        self.screen.blit(self.surface, (0, 0))
        self.screen.blit(self.menu_text, self.menu_rect)
