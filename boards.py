from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QColor, QFont
import random
from collections import namedtuple

Point = namedtuple('Point', 'x, y')

class Board:
    def __init__(self, x=32, y=24):             # number of blocks on the board
        self.x, self.y = x, y
        self.apple = None

    def generate_apple(self, snake):
        """Generate a new apple position avoiding occupied positions."""
        if snake is None or snake.body is None or len(snake.body) < 2:
            raise Exception("Snake Body Exception")
        while True:
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)
            apple_pos = Point(x, y)
            if apple_pos not in snake.body:     # apple and body not conflicting
                self.apple = apple_pos
                snake.set_apple(self.apple)
                return

    def reset(self):
        if self.snake:
            self.snake.reset()
            self.generate_apple(self.snake)

class GameBoard(Board, QWidget):
    def __init__(self, x=32, y=24, block_size=20, speed=8, background=(0, 0, 0)):
        Board.__init__(self, x, y)
        QWidget.__init__(self)
        
        self.BGROUND = QColor(*background)
        self.bs = block_size
        self.speed = speed
        self.score = 0
        
        # Set window properties
        self.setWindowTitle('Snake')
        self.setFixedSize(x * self.bs, y * self.bs)
        
        # Setup timer for game speed
        self.timer = QTimer()
        #self.timer.timeout.connect(self._on_timer)
        self.frame_delay = 1000 // speed  # Convert to milliseconds
        
    def start_timer(self):
        self.timer.start(self.frame_delay)
        
    def stop_timer(self):
        self.timer.stop()

    def paintEvent(self, event):
        if not self.snake.body:
            return
            
        painter = QPainter(self)
        
        # Fill background
        painter.fillRect(0, 0, self.width(), self.height(), self.BGROUND)
        
        # Draw snake
        BLUE1 = QColor(0, 0, 255)
        BLUE2 = QColor(0, 100, 255)
        
        offSet = self.bs // 5
        bSize = self.bs - 2 * offSet
        
        for pt in self.snake.body:
            painter.fillRect(int(pt.x * self.bs), int(pt.y * self.bs), self.bs, self.bs, BLUE1)
            painter.fillRect(int(pt.x * self.bs + offSet), int(pt.y * self.bs + offSet), bSize, bSize, BLUE2)
        
        # Draw apple
        if self.apple:
            RED = QColor(200, 0, 0)
            painter.fillRect(int(self.apple.x * self.bs), int(self.apple.y * self.bs), self.bs, self.bs, RED)

    def render(self, score):
        """Update the display with current game state."""
        self.score = score
        self.update()  # Trigger paintEvent
        QApplication.processEvents()  # Process events to update display
