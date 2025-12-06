Python Snake Game
---

```shell
Usage: mygame.py [OPTIONS]

                      Wecome to Snakegame

  * Use Left and Right Key to change the direction

  * Close the window or hit Escape to end the current episode

  * Use 'R' key to start new episode when it dies or the episode ended

  * Close the window or hit Escape twice to end the App

Options:
  -s, --speed INTEGER   game speed
  -x, --grid_x INTEGER  number of grid cells in x-axis
  -y, --grid_y INTEGER  number of grid cells in y-axis
  -h, --help            Show this message and exit.
```

This is a Python implementation of the Snake Game with the PyQt5 as a separate board so the presentation layer can be extended easily for other purposes such as the Reinforcement Learning. And the user input is handled as an one-hot-encoding of [ forward, right, left ], which can be integrated to the Machine Learning.

![스크린샷 2022-05-21 오후 11 03 39](https://user-images.githubusercontent.com/13171662/169655238-0ecf4049-344f-4fc8-893b-1779fed5f23d.png)

