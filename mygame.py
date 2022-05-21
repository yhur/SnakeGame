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
@click.option('--bsize', '-b', type=(int, int), help='board size')
def main(**kwargs):
    """\n\t\t\tWecome to Snakegame\n
    * Use Left and Right Key to change the direction\n
    * Click on the close control of the App, or hit Escpe to end the current stage\n
    * Use 'R' key' to start new stage when it dies or the stage ended\n
    * Double Click on the close control of the App, or hit Escpe twice to end the App
    """
    speed = kwargs['speed'] or 5
    bsize = kwargs['bsize'] or (32, 20)
    board = GameBoard(x=bsize[0], y=bsize[1])
    snake = Snake(board)
    clock = pygame.time.Clock()
    game_close = True
    while game_close:
        stageOn = True
        while stageOn:
            clock.tick(speed)
            action = getAction()
            if action is Snake.action_q:
                stageOn = False
            else:
                stageOn = snake.moveTo(action)
    
        hold = True
        while hold:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = hold = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        snake.reset()
                        hold = False
                    elif event.key == pygame.K_ESCAPE:
                        game_close = hold = False
    
if __name__ == '__main__':
    main()