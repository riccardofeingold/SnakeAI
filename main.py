import pygame
import random
from snake_game.utils import Directions
from snake_game import SnakeGame
from agent import train

if __name__ == "__main__":
    pygame.init()
    train()

    # game = SnakeGame()
    # while True:
    #     game_over, score = game.step()

    #     if game_over:
    #         break
    
    # pygame.quit()