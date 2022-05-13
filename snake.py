import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.SysFont('arial', 25)

Point = namedtuple('Point', 'x, y')

class Direction(Enum):          # clock wise sequenced enum, so keep the order
    RIGHT = (1, 0)
    DOWN  = (0, 1)
    LEFT  = (-1, 0)
    UP    = (0, -1)

class Snake:

    game_over = True
    game_on = False

    def __init__(self, x=32, y=24, block_size = 20):             # number of blocks on the board
        self.x, self.y, self.bs = x, y, block_size
        self.directionRing = list(Direction)
        self.display = pygame.display.set_mode((x * self.bs, y * self.bs))
        pygame.display.set_caption('Snake')
        self.reset()

    def reset(self):
        self.score = 0
        self.apple = None
        self.moves = 0          # count of moves

        self.direction = random.choice(list(Direction))
        self.head = Point(self.x/2, self.y/2)
        #self.head = Point(random.randint(2, self.x - 2), random.randint(2, self.y - 2))
        bx, by = self.direction.value[0], self.direction.value[1]
        self.body = [self.head,
                      Point(self.head.x - bx, self.head.y - by),
                      Point(self.head.x - bx * 2, self.head.y - by * 2)]
        self.__newApple()

    def __newApple(self):
        x = random.randint(0, self.x - 1)
        y = random.randint(0, self.y - 1)
        self.apple = Point(x, y)
        if self.apple in self.body:
            self.__newApple()

    def moveTo(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        self.moves += 1

        self.__newHead(action)
        self.body.insert(0, self.head)
        
        if self.is_coliding(self.head) or self.moves > 100*len(self.body):
            return Snake.game_over, self.score
        else:
            if self.head == self.apple:
                self.score += 1
                self.__newApple()
            else:
                self.body.pop()

            self.__update_board()
            return Snake.game_on, self.score

    def is_coliding(self, head):
        # hits wall
        if head.x >= self.x or head.x < 0 or head.y >= self.y or head.y < 0:
            return True
        # hits itself
        if head in self.body[1:]:
            return True
        return False

    def __update_board(self):
        WHITE = (255, 255, 255)
        RED =   (200,   0,   0)
        BLUE1 = (  0,   0, 255)
        BLUE2 = (  0, 100, 255)
        BLACK = (  0,   0,   0)

        self.display.fill(BLACK)

        for pt in self.body:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x * self.bs, pt.y * self.bs, self.bs, self.bs))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x * self.bs +4, pt.y * self.bs +4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.apple.x * self.bs , self.apple.y * self.bs , self.bs, self.bs))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def __newHead(self, action):
        # action = [ forward, right, left ]
        idx = self.directionRing.index(self.direction)
        if action == [0, 1, 0]:             # Right 
            self.direction = self.directionRing[(idx + 1) % 4]
        elif action == [0, 0, 1]:           # Left
            self.direction = self.directionRing[(idx - 1) % 4]

        x = self.head.x + self.direction.value[0]
        y = self.head.y + self.direction.value[1]
        self.head = Point(x, y)