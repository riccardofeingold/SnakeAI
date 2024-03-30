import pygame
from snake_game import SnakeGame
if __name__ == "__main__":
    pygame.init()

    game = SnakeGame()
    while True:
        game_over, score = game.step()

        if game_over:
            break
    
    pygame.quit()