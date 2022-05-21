import pygame
import random
from collections import namedtuple

Point = namedtuple('Point', 'x, y')

pygame.init()

font = pygame.font.SysFont('arial', 25)

class Board:
    def __init__(self, x=32, y=24):             # number of blocks on the board
        self.x, self.y = x, y

    def update_board(self, snake):
        pass

    def newApple(self, snake):
        x = random.randint(0, self.x - 1)
        y = random.randint(0, self.y - 1)
        self.apple = Point(x, y)
        if self.apple in snake.body:
            self.newApple(snake)

class GameBoard(Board):
    def __init__(self, x=32, y=24, block_size = 20):             # number of blocks on the board
        super().__init__(x, y)
        self.bs = block_size
        self.display = pygame.display.set_mode((x * self.bs, y * self.bs))
        pygame.display.set_caption('Snake')

    def update_board(self, snake):
        WHITE = (255, 255, 255)
        RED =   (200,   0,   0)
        BLUE1 = (  0,   0, 255)
        BLUE2 = (  0, 100, 255)
        BLACK = (  0,   0,   0)

        self.display.fill(BLACK)

        for pt in snake.body:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x * self.bs, pt.y * self.bs, self.bs, self.bs))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x * self.bs +4, pt.y * self.bs +4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.apple.x * self.bs , self.apple.y * self.bs , self.bs, self.bs))

        text = font.render("Score: " + str(snake.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()