#!/usr/bin/env python
import sys
import signal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont
from snake import Snake
from boards import GameBoard
import click

# Allow Ctrl+C to quit
signal.signal(signal.SIGINT, signal.SIG_DFL)
    
class SnakeGameWindow(GameBoard):
    def __init__(self, x=32, y=24, block_size=35, speed=8):
        super().__init__(x=x, y=y, block_size=block_size, speed=speed)
        self.snake = Snake(x, y)
        self.episode_active = False
        self.running = True
        self.current_action = Snake.action_f
        self.generate_apple(self.snake)
        self.timer.timeout.connect(self.game_step)
        
    def start_episode(self):
        self.episode_active = True
        self.current_action = Snake.action_f
        self.timer.start(self.frame_delay)
        
    def game_step(self):
        if self.episode_active:
            status = self.snake.moveTo(self.current_action)
            if status == 'apple':
                self.generate_apple(self.snake)
            
            self.render(self.snake.score)
            
            # Reset to forward after each move
            self.current_action = Snake.action_f
            
            if status not in ['ok', 'apple']:
                self.episode_active = False
                self.timer.stop()
                
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
                self.close()
        elif event.key() == Qt.Key_Space:
            if self.timer.isActive():
                self.timer.stop()
            else:
                status = self.snake.moveTo(self.current_action)
                if status == 'apple':
                    self.generate_apple(self.snake)
                self.render(self.snake.score)
                self.current_action = Snake.action_f
        elif self.episode_active:
            if event.key() == Qt.Key_Left:
                self.current_action = Snake.action_l
            elif event.key() == Qt.Key_Right:
                self.current_action = Snake.action_r
            elif event.key() == Qt.Key_R:
                self.start_episode()
        else:
            if event.key() == Qt.Key_R:
                self.snake.reset()
                self.generate_apple(self.snake)
                self.start_episode()
                
    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

    def paintEvent(self, event):
        if not self.snake.body:
            return
            
        super().paintEvent(event)  # Call parent to draw board, snake, apple
        
        painter = QPainter(self)
        painter.setPen(QColor(255, 255, 255))
        font = QFont('Arial', 25)
        painter.setFont(font)
        painter.drawText(10, 30, f"Score: {self.score}")

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--speed', '-s', type=int, help='game speed')
@click.option('--grid_x', '-x', type=int, help='number of grid cells in x-axis')
@click.option('--grid_y', '-y', type=int, help='number of grid cells in y-axis')
def main(**kwargs):
    """\n\t\t\tWecome to Snakegame\n
    * Use Left and Right Key to change the direction\n
    * Close the window or hit Escape to end the current episode\n
    * Use 'R' key to start new episode when it dies or the episode ended\n
    * Close the window or hit Escape twice to end the App
    """
    speed = kwargs['speed'] or 8
    x = kwargs['grid_x'] or 32
    y = kwargs['grid_y'] or 24
    
    app = QApplication(sys.argv)
    window = SnakeGameWindow(x=x, y=y, block_size=35, speed=speed)
    window.show()
    window.start_episode()
    
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()
