Python Snake Game

```shell
pygame 2.6.1 (SDL 2.28.4, Python 3.12.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Usage: mygame.py [OPTIONS]

                      Welcome to Snakegame

  * Use Left and Right Key to change the direction

  * Click on the close control of the App, or hit Escape to end the current
  episode

  * Use 'R' key to start new episode when it dies or the episode ended

  * Double Click on the close control of the App, or hit Escape twice to end
  the App

Options:
  -s, --speed INTEGER   pygame speed
  -x, --grid_x INTEGER  number of grid cells in x-axis
  -y, --grid_y INTEGER  number of grid cells in y-axis
  -h, --help            Show this message and exit.
```

This is a Python implementation of the Snake Game with the pygame as a separate board so the presentation layer can be replaced easily with other technology. And the user input is handled as an one-hot-encoding of [ forward, right, left ], which can be integrated to the Machine Learning.

![스크린샷 2022-05-21 오후 11 03 39](https://user-images.githubusercontent.com/13171662/169655238-0ecf4049-344f-4fc8-893b-1779fed5f23d.png)



That way, this can be used easily for Machine Learning such as the Genetic Algorithm or Reinforcement Learning. The following snippet is the sample code of how to use the  snake.py/board.py.

```python
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
            
            text = board.font.render("Score: " + str(snake.score), True, (255,255,255))
            board.display.blit(text, [0, 0])
            pygame.display.flip()
```       