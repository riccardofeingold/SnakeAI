import pygame
import random
from typing import Tuple
from .game_object import GameObject
from .snake import Snake
from snake_game.utils import Constants, Colors, Point

class Food(GameObject):
    def __init__(self) -> None:
        self.color = Colors.RED

        self.spawn()
        pass
    
    def spawn(self):
        self.x = random.randint(Constants.BLOCK_SIZE, (Constants.WIDTH - Constants.BLOCK_SIZE)//Constants.BLOCK_SIZE) * Constants.BLOCK_SIZE
        self.y = random.randint(Constants.BLOCK_SIZE, (Constants.HEIGHT - Constants.BLOCK_SIZE)//Constants.BLOCK_SIZE) * Constants.BLOCK_SIZE

        self.point = Point(self.x, self.y)
        pass

    def move(self):
        pass
    
    def draw(self, display):
        pygame.draw.rect(display, self.color, pygame.Rect(self.x, self.y, Constants.BLOCK_SIZE, Constants.BLOCK_SIZE))

    def selfDestroy(self):
        pass