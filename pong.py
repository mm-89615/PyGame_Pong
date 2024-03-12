import pygame

from settings import *


class Game:
    """Класс управления настройками и поведением игры"""

    def __init__(self):
        """Инициализация игры и создание игровых ресурсов"""
        # настройки игрового окна и FPS
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # основной цикл игры
        self.running = True

    def game_running(self):
        """Запуск основного цикла игры"""
        while self.running:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        """Обновление изображений на экране"""
        self.clock.tick(FPS)

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
