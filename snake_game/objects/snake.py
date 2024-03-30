import pygame
from typing import Tuple
from .game_object import GameObject
from snake_game.utils import Directions
from snake_game.utils import Colors, Point, Constants

class Snake(GameObject):
    def __init__(self, start_position: Tuple[float, float], init_direction: Directions):
        self.head = Point(start_position[0], start_position[1])
        self.tail = [self.head,
                     Point(self.head.x - Constants.BLOCK_SIZE.value, self.head.y),
                     Point(self.head.x - 2*Constants.BLOCK_SIZE.value, self.head.y)
                    ]
        self.direction = init_direction
        self.color = Colors.BLUE1
        pass
    
    def spawn(self):
        pass

    def move(self):
        new_head_x = self.head.x
        new_head_y = self.head.y

        if self.direction == Directions.RIGHT:
            new_head_x += Constants.BLOCK_SIZE.value
        elif self.direction == Directions.LEFT:
            new_head_x -= Constants.BLOCK_SIZE.value
        elif self.direction == Directions.DOWN:
            new_head_y += Constants.BLOCK_SIZE.value
        elif self.direction == Directions.UP:
            new_head_y -= Constants.BLOCK_SIZE.value

        self.head = Point(new_head_x, new_head_y)

    def draw(self, display):
        for piece in self.tail:
            pygame.draw.rect(display, Colors.BLUE1.value, pygame.Rect(piece.x, piece.y, Constants.BLOCK_SIZE.value, Constants.BLOCK_SIZE.value))
            pygame.draw.rect(display, Colors.BLUE2.value, pygame.Rect(piece.x+4, piece.y+4, 12, 12))
        pass

    def selfDestroy(self):
        pass