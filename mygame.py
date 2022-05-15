import pygame
from snake import Snake
import click

def getDirection():
    dir = [1,0,0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dir = stage_end
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir = [0,0,1]
            elif event.key == pygame.K_RIGHT:
                dir = [0,1,0]
            elif event.key == pygame.K_ESCAPE:
                dir = stage_end
    return dir

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
    bsize = kwargs['bsize'] or (32, 24)
    snake = Snake(x=bsize[0], y=bsize[1])
    stage_end = [0, 0, 0]       # [ forward, right, left ] one hot encoding
    clock = pygame.time.Clock()
    game_close = True
    while game_close:
        done = False
        while done == False:
            clock.tick(speed)
            dir = getDirection()
            if dir is stage_end:
                done = True
            else:
                done, score = snake.moveTo(dir)
    
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
    
main()