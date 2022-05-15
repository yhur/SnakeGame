import random
from enum import Enum
from collections import namedtuple

Point = namedtuple('Point', 'x, y')

class Direction(Enum):          # clock wise sequenced enum, so keep the order
    RIGHT = (1, 0)
    DOWN  = (0, 1)
    LEFT  = (-1, 0)
    UP    = (0, -1)

class Snake:
    action_r    = [0, 1, 0]
    action_l    = [0, 0, 1]
    action_f    = [1, 0, 0]
    action_q    = [0, 0, 0]

    def __init__(self, board):             # number of blocks on the board
        self.directionRing = list(Direction)
        self.board = board
        self.x, self.y = board.x, board.y
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
        self.newApple()

    def newApple(self):
        x = random.randint(0, self.x - 1)
        y = random.randint(0, self.y - 1)
        self.apple = Point(x, y)
        if self.apple in self.body:
            self.newApple()

    def moveTo(self, action):
        self.moves += 1

        self.newHead(action)
        self.body.insert(0, self.head)
        
        if self.is_colliding(self.head) or self.moves > 100*len(self.body):
            return False                # moveTo failed
        else:
            if self.head == self.apple:
                self.score += 1
                self.newApple()
            else:
                self.body.pop()
            self.update_board()
            return True                 # moveTo succeeded

    def is_colliding(self, head) -> bool:    # return True if colliding else False
        # hits wall
        if head.x >= self.x or head.x < 0 or head.y >= self.y or head.y < 0:
            return True
        # hits itself
        if head in self.body[1:]:
            return True
        return False

    def newHead(self, action) -> bool:    # return True if succeeded else False
        # action = [ forward, right, left ]
        idx = self.directionRing.index(self.direction)
        if action == self.action_r:             # Right 
            self.direction = self.directionRing[(idx + 1) % 4]
        elif action == self.action_l:           # Left
            self.direction = self.directionRing[(idx - 1) % 4]

        x = self.head.x + self.direction.value[0]
        y = self.head.y + self.direction.value[1]
        self.head = Point(x, y)

    def update_board(self):
        self.board.update_board(self)