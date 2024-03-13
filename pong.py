import pygame

from settings import *
from player import Player
from ball import Ball
from scoreboard import Scoreboard


class Game:
    """ Класс управления настройками и поведением игры """

    def __init__(self):
        """ Инициализация игры и создание игровых ресурсов """
        pygame.init()
        # Настройки игрового окна и FPS
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pong')
        self.icon = pygame.image.load('images/icon.png')
        pygame.display.set_icon(self.icon)
        # Шрифт
        self.font = pygame.font.Font('fonts/KodeMono.ttf', FONS_SIZE_SCORE)
        # Создание игрока
        self.player1 = Player(player=1, game_screen=self)
        self.player2 = Player(player=2, game_screen=self)
        # Создание игрового мяча
        self.ball = Ball(game_screen=self)
        # Создание счета игроков
        self.score = Scoreboard(game_screen=self)
        # Основной цикл игры
        self.running = True
        # Проверка на гол
        self.is_goal = False
        # Обратный отсчет при голе
        self.countdown = pygame.USEREVENT + 1
        self.counter = 3
        self.font = pygame.font.Font('fonts/KodeMono.ttf', FONS_SIZE_GOAL_TIMER)
        self.timer = self.font.render(f"{self.counter}", True, TIMER_COLOR)
        self.timer_rect = self.timer.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    def game_running(self):
        """ Запуск основного цикла игры """
        while self.running:
            # Обновление экрана
            self.update_screen()
            # Отрисовка на экране
            self.draw_on_screen()
            # Обработка событий на экране
            self.check_events()

    def update_screen(self):
        """ Обновление изображений на экране """
        # Обновление игроков
        self.player1.update()
        self.player2.update()
        # Обновление мяча если нет гола
        if not self.is_goal:
            self.ball.update()
        # Обновление экрана
        self.draw_on_screen()
        self.clock.tick(FPS)
        pygame.display.flip()

    def draw_on_screen(self):
        """ Отрисовка объектов на экране """
        # Прорисовка игрового поля
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, BG_LINE_COLOR, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
        # Прорисовка игроков
        self.player1.blit()
        self.player2.blit()
        # Прорисовка счета
        self.score.draw_scoreboard()
        # Прорисовка мяча
        self.ball.blit()
        # Отрисовка таймера если забит гол
        if self.is_goal:
            self.timer = self.font.render(f"{self.counter}", True, TIMER_COLOR)
            self.screen.blit(self.timer, self.timer_rect)

    def check_events(self):
        """ Обработка происходящих событий """
        # Проверка столкновения мяча с игроками
        self.check_collisions()
        # Проверка ушел ли мяч за края экрана
        self.check_goal()
        # Проверка событий игры
        for event in pygame.event.get():
            # Обратный отсчет на экране
            if event.type == self.countdown:
                self.counter -= 1
                if self.counter == 0:
                    pygame.time.set_timer(self.countdown, 0)
                    self.is_goal = False
            # Событие закрытия игры
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

    def check_collisions(self):
        """ Отслеживание столкновение мяча с игроками и смена направления"""
        # Столкновение с первым игроком
        if pygame.Rect.colliderect(self.ball.rect, self.player1.rect):
            self.ball.change_direction_x()
        # Столкновение со вторым игроком
        if pygame.Rect.colliderect(self.ball.rect, self.player2.rect):
            self.ball.change_direction_x()

    def check_goal(self):
        """ Проверка ушел ли мяч за края """
        # Гол первому игроку
        if self.ball.rect.right < 10:
            self.score.player2_goals += 1
            self.is_goal = True
            self.goal_handing()
        # Гол второму игроку
        if self.ball.rect.left > SCREEN_WIDTH + 10:
            self.score.player1_goals += 1
            self.is_goal = True
            self.goal_handing()

    def goal_handing(self):
        """ Обработка гола """
        # Возвращение в центр
        self.ball.ball_on_center()
        self.ball.random_start()
        # Запуск обратного отсчета
        self.counter = 3
        pygame.time.set_timer(self.countdown, 1000)


if __name__ == "__main__":
    # Создание экземпляра игры и запуск
    game = Game()
    game.game_running()
