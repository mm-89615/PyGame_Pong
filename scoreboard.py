import pygame

from settings import *


class Scoreboard:
    """ Класс создания счета игроков """

    def __init__(self, game_screen):
        """ Инициализация таблицы результатов """
        self.screen = game_screen.screen
        # Добавление шрифта
        self.score_font = pygame.font.Font('fonts/KodeMono.ttf', FONS_SIZE_SCORE)
        # Подсчет голов
        self.player1_goals = 0
        self.player2_goals = 0
        # Рендеринг счета
        self.player1_score = self.score_font.render(f"{self.player1_goals}", True, SCORE_TEXT_COLOR)
        self.player2_score = self.score_font.render(f"{self.player2_goals}", True, SCORE_TEXT_COLOR)
        # Прямоугольник текста счета
        self.player1_rect = self.player1_score.get_rect(center=(SCREEN_WIDTH / 4, 30))
        self.player2_rect = self.player2_score.get_rect(center=(SCREEN_WIDTH - SCREEN_WIDTH / 4, 30))

    def draw_scoreboard(self):
        """ Отрисовка счета игроков """
        # Отрисовка счета первого игрока
        self.player1_score = self.score_font.render(f"{self.player1_goals}", True, SCORE_TEXT_COLOR)
        self.screen.blit(self.player1_score, self.player1_rect)
        # Отрисовка счета второго игрока
        self.player2_score = self.score_font.render(f"{self.player2_goals}", True, SCORE_TEXT_COLOR)
        self.screen.blit(self.player2_score, self.player2_rect)
