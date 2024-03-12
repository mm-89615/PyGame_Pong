import pygame

from settings import *


class Scoreboard:
    """ Класс создания счета игроков """

    def __init__(self, game_screen):
        """ Инициализация таблицы результатов """
        self.screen = game_screen.screen
        # Добавление шрифта
        self.font = pygame.font.Font('fonts/KodeMono.ttf', 50)
        # Подсчет голов
        self.player1_goals = 0
        self.player2_goals = 0
        # Текст счета для игроков
        self.player1_score = self.font.render(f"{self.player1_goals}", True, SCORE_TEXT_COLOR)
        self.player2_score = self.font.render(f"{self.player2_goals}", True, SCORE_TEXT_COLOR)

    def draw_scoreboard(self):
        """ Отрисовка счета игроков """
        # Отрисовка счета первого игрока
        self.screen.blit(self.player1_score, ((SCREEN_WIDTH / 4), 20))
        # Отрисовка счета второго игрока
        self.screen.blit(self.player2_score, ((SCREEN_WIDTH - SCREEN_WIDTH / 4), 20))
