import pygame
import math
import datetime

class MickeyClock:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.cx = width // 2
        self.cy = height // 2
        self.radius = 150

        # Загрузка изображения руки Микки
        try:
            hand_img = pygame.image.load("images/mickey_hand.png")
            self.hand = pygame.transform.scale(hand_img, (40, 120))
        except:
            # Если изображение не найдено — рисуем вручную
            self.hand = None

        # Цвета
        self.BLACK = (30, 30, 30)
        self.WHITE = (255, 255, 255)
        self.RED   = (220, 50, 50)
        self.YELLOW= (255, 230, 50)
        self.SKIN  = (255, 210, 140)

    def _angle(self, value, total):
        # Угол по часовой стрелке, 0 = вверх
        return math.radians(value / total * 360 - 90)

    def _draw_hand(self, angle, length, color, width):
        end_x = self.cx + math.cos(angle) * length
        end_y = self.cy + math.sin(angle) * length
        pygame.draw.line(self.screen, color,
                         (self.cx, self.cy),
                         (int(end_x), int(end_y)), width)

    def _draw_mickey_hand(self, angle, length):
        # Рисуем "руку" Микки: рукав + перчатка
        end_x = self.cx + math.cos(angle) * length
        end_y = self.cy + math.sin(angle) * length

        # Рукав (толстая линия)
        pygame.draw.line(self.screen, self.YELLOW,
                         (self.cx, self.cy),
                         (int(end_x), int(end_y)), 8)

        # Перчатка (белый круг на конце)
        pygame.draw.circle(self.screen, self.WHITE,
                           (int(end_x), int(end_y)), 14)
        pygame.draw.circle(self.screen, self.BLACK,
                           (int(end_x), int(end_y)), 14, 2)

        # Пальцы (3 маленьких кружка)
        for i in [-1, 0, 1]:
            fx = int(end_x + math.cos(angle + i * 0.4) * 16)
            fy = int(end_y + math.sin(angle + i * 0.4) * 16)
            pygame.draw.circle(self.screen, self.WHITE, (fx, fy), 7)
            pygame.draw.circle(self.screen, self.BLACK, (fx, fy), 7, 1)

    def draw(self):
        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        # Циферблат
        pygame.draw.circle(self.screen, self.WHITE,
                           (self.cx, self.cy), self.radius)
        pygame.draw.circle(self.screen, self.BLACK,
                           (self.cx, self.cy), self.radius, 4)

        # Деления (12 штук)
        for i in range(12):
            a = math.radians(i * 30)
            x1 = self.cx + math.cos(a) * (self.radius - 10)
            y1 = self.cy + math.sin(a) * (self.radius - 10)
            x2 = self.cx + math.cos(a) * (self.radius - 22)
            y2 = self.cy + math.sin(a) * (self.radius - 22)
            pygame.draw.line(self.screen, self.BLACK,
                             (int(x1), int(y1)),
                             (int(x2), int(y2)), 3)

        # Уши Микки
        for dx in [-100, 100]:
            pygame.draw.circle(self.screen, self.BLACK,
                               (self.cx + dx, self.cy - 130), 60)

        # Стрелки с перчатками
        min_angle = self._angle(minutes, 60)
        sec_angle = self._angle(seconds, 60)

        # Правая рука = минуты
        self._draw_mickey_hand(min_angle, 110)
        # Левая рука = секунды
        self._draw_mickey_hand(sec_angle, 90)

        # Центральный кружок
        pygame.draw.circle(self.screen, self.BLACK,
                           (self.cx, self.cy), 8)

        # Цифровое время
        font = pygame.font.SysFont("arial", 28, bold=True)
        time_surf = font.render(
            f"{minutes:02d}:{seconds:02d}", True, self.BLACK)
        rect = time_surf.get_rect(center=(self.cx, self.cy + 60))
        self.screen.blit(time_surf, rect)