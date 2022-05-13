import pygame
from snake import Snake

snake = Snake()

stage_end = [0, 0, 0]       # [ forward, right, left ] one hot encoding
clock = pygame.time.Clock()
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

game_close = True
while game_close:
    done = False
    while done == False:
        clock.tick(5)
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
