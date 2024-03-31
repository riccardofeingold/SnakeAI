from enum import Enum
from collections import namedtuple

Point = namedtuple("Point", "x, y")

class Constants(object):
    WIDTH = 800
    HEIGHT = 600
    MARGIN = 10
    SPEED = 100
    PLAY_SPEED = 20
    BLOCK_SIZE = 20

    class HyperParams(object):
        MAX_ITERATION = 500
        MAX_GAMES_WITH_EXPLORATION = 80
        EXPLORATION = 0.4
        EPISODE_LENGTH_SCALE = 100
        MAX_MEMORY = 100_000
        BATCH_SIZE = 1000
        LR = 0.001

class Colors(object):
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    BLUE1 = (0, 0, 255)
    BLUE2 = (0, 100, 255)
    BLACK = (0, 0, 0)

class Directions(Enum):
    UP: int = 0
    DOWN: int = 1
    LEFT: int = 2
    RIGHT: int = 3