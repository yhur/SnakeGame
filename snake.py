import random
from enum import Enum
from collections import namedtuple

Point = namedtuple('Point', 'x, y')

class Direction(Enum):          # clock wise sequenced enum, so keeping this order is critical
    RIGHT = (1, 0)
    DOWN  = (0, 1)
    LEFT  = (-1, 0)
    UP    = (0, -1)

class Snake:
    # one hot encoding of [ forward, right, left ]
    action_r    = [0, 1, 0]
    action_l    = [0, 0, 1]
    action_f    = [1, 0, 0]
    action_q    = [0, 0, 0]

    def __init__(self, grid_width, grid_height):
        self.directionRing = list(Direction)
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.reset()

    def reset(self):
        self.score = 0
        self.moves = 0          # count of moves

        self.direction = random.choice(list(Direction))
        self.head = Point(self.grid_width/2, self.grid_height/2)
        #self.head = Point(random.randint(2, self.grid_width - 2), random.randint(2, self.grid_height - 2))
        bx, by = self.direction.value[0], self.direction.value[1]
        self.body = [self.head,
                      Point(self.head.x - bx, self.head.y - by),
                      Point(self.head.x - bx * 2, self.head.y - by * 2)]
        self.apple = None

    def set_apple(self, apple_pos):
        """Let the Snake know the apple position."""
        self.apple = apple_pos

    def newHead(self, action):
        # action = [ forward, right, left ]
        idx = self.directionRing.index(self.direction)
        if action == self.action_r:             # Right 
            self.direction = self.directionRing[(idx + 1) % 4]
        elif action == self.action_l:           # Left
            self.direction = self.directionRing[(idx - 1) % 4]

        x = self.head.x + self.direction.value[0]
        y = self.head.y + self.direction.value[1]
        self.head = Point(x, y)

    def moveTo(self, action):
        """Move snake and return status. Apple position must be provided."""
        self.moves += 1

        self.newHead(action)
        self.body.insert(0, self.head)
        head = self.head
        
        if head.x >= self.grid_width or head.x < 0 or head.y >= self.grid_height or head.y < 0:
            return 'wall'
        elif head in self.body[1:]:
            return 'body'
        elif self.moves > 100 * len(self.body):
            return 'starved'
        else:
            if self.head == self.apple:
                self.score += 1
                self.apple = None  # Clear apple after eating
                # Don't pop tail when eating apple (snake grows)
                return 'apple'
            else:
                self.body.pop()
            return 'ok'                 # moveTo succeeded
