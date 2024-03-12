import pygame

from settings import *
from player import Player


class Game:
    """Класс управления настройками и поведением игры"""

    def __init__(self):
        """Инициализация игры и создание игровых ресурсов"""
        # настройки игрового окна и FPS
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pong')
        self.icon = pygame.image.load('images/icon.png')
        pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()
        # основной цикл игры
        self.running = True
        # создание игрока
        self.player1 = Player(player=1, game_screen=self)
        self.player2 = Player(player=2, game_screen=self)

    def game_running(self):
        """Запуск основного цикла игры"""
        while self.running:
            # обновление игроков
            self.player1.update()
            self.player2.update()
            # обновление экрана
            self.update_screen()
            self.draw_on_screen()
            # обработка событий на экране
            self.check_events()

    def update_screen(self):
        """Обновление изображений на экране"""
        pygame.display.flip()
        self.draw_on_screen()
        self.clock.tick(FPS)

    def draw_on_screen(self):
        # прорисовка игрового поля
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, BG_LINE_COLOR, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
        # прорисовка игроков
        self.player1.blit()
        self.player2.blit()

    def check_events(self):
        """Обработка происходящих событий"""
        for event in pygame.event.get():
            # событие закрытия и гры
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()


if __name__ == "__main__":
    # Создание экземпляра игры и запуск
    game = Game()
    game.game_running()
