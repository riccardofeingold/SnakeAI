from enum import Enum
from collections import namedtuple

Point = namedtuple("Point", "x, y")

class Constants(Enum):
    WIDTH = 800
    HEIGHT = 600
    MARGIN = 10
    SPEED = 10
    BLOCK_SIZE = 20

class Colors(Enum):
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