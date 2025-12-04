import pygame
from snake import Snake
from boards import GameBoard
import click

def getAction():
    action = Snake.action_f
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = Snake.action_q
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action = Snake.action_l
            elif event.key == pygame.K_RIGHT:
                action = Snake.action_r
            elif event.key == pygame.K_ESCAPE:
                action = Snake.action_q
    return action

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--speed', '-s', type=int, help='pygame speed')
@click.option('--grid_x', '-x', type=int, help='number of grid cells in x-axis')
@click.option('--grid_y', '-y', type=int, help='number of grid cells in y-axis')
def main(**kwargs):
    """\n\t\t\tWecome to Snakegame\n
    * Use Left and Right Key to change the direction\n
    * Click on the close control of the App, or hit Escpe to end the current episode\n
    * Use 'R' key' to start new episode when it dies or the episode ended\n
    * Double Click on the close control of the App, or hit Escpe twice to end the App
    """
    speed = kwargs['speed'] or 8
    x = kwargs['grid_x'] or 32
    y = kwargs['grid_y'] or 24
    board = GameBoard(x=x, y=y, block_size=35, speed=speed)
    snake = Snake(board)

    running = True
    while running:
        episode_active = True
        while episode_active:
            action = getAction()
            if action is Snake.action_q:
                episode_active = False
            else:
                episode_active = True if snake.moveTo(action) == 'ok' else False
            
        hold = True
        while hold:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = hold = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        snake.reset()
                        hold = False
                    elif event.key == pygame.K_ESCAPE:
                        running = hold = False
    
if __name__ == '__main__':
    main()