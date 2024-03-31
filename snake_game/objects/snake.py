import pygame
from typing import Tuple
from .game_object import GameObject
from snake_game.utils import Directions
from snake_game.utils import Colors, Point, Constants

class Snake(GameObject):
    def __init__(self, start_position: Tuple[float, float], init_direction: Directions):
        self.head = Point(start_position[0], start_position[1])
        self.tail = [self.head,
                     Point(self.head.x - Constants.BLOCK_SIZE, self.head.y),
                     Point(self.head.x - 2*Constants.BLOCK_SIZE, self.head.y)
                    ]
        self.direction = init_direction
        self.color = Colors.BLUE1
        pass
    
    def spawn(self):
        pass

    def move(self, action):
        # action = [straight, left, right]
        clock_wise_directions = [Directions.UP, Directions.RIGHT, Directions.DOWN, Directions.LEFT]
        if action[1]:
            self.direction = clock_wise_directions[clock_wise_directions.index(self.direction) - 1]
        elif action[2]:
            self.direction = clock_wise_directions[(clock_wise_directions.index(self.direction) + 1)%len(clock_wise_directions)]

        new_head_x = self.head.x
        new_head_y = self.head.y

        if self.direction == Directions.RIGHT:
            new_head_x += Constants.BLOCK_SIZE
        elif self.direction == Directions.LEFT:
            new_head_x -= Constants.BLOCK_SIZE
        elif self.direction == Directions.DOWN:
            new_head_y += Constants.BLOCK_SIZE
        elif self.direction == Directions.UP:
            new_head_y -= Constants.BLOCK_SIZE

        self.head = Point(new_head_x, new_head_y)

    def draw(self, display):
        for piece in self.tail:
            pygame.draw.rect(display, Colors.BLUE1, pygame.Rect(piece.x, piece.y, Constants.BLOCK_SIZE, Constants.BLOCK_SIZE))
            pygame.draw.rect(display, Colors.BLUE2, pygame.Rect(piece.x+4, piece.y+4, 12, 12))
        pass

    def selfDestroy(self):
        pass