Python Snake Game

This is a Python implementation of the Snake Game with the pygame as a separate board so the presentation layer can be replaced easily with other technology. And the user input is handled as an one-hot-encoding of [ forward, right, left ], which can be integrated to the Machine Learning.

![스크린샷 2022-05-21 오후 11 03 39](https://user-images.githubusercontent.com/13171662/169655238-0ecf4049-344f-4fc8-893b-1779fed5f23d.png)

That way, this can be used easily for the Machine Learnig such as the Genetic Algorithm or the Reinforcement Learning. The following snippet is the sample code of how to use the  snake.py/board.py.

```python
speed = kwargs['speed'] or 5
bsize = kwargs['bsize'] or (32, 20) 
board = GameBoard(x=bsize[0], y=bsize[1], block_size=35)
snake = Snake(board)
game_close = True
while game_close:
    stageOn = True
    while stageOn:
        action = getAction()
        if action is Snake.action_q:
            stageOn = False
        else:
            stageOn = snake.moveTo(action)
```       