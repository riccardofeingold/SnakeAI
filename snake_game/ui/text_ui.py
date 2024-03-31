import pygame
from snake_game.utils import Colors

class ScoreText:
    def __init__(self, display: pygame.display) -> None:
        self.display = display
        self.font = pygame.font.Font(None, 40)

    def draw(self, score: int):
        text = self.font.render("Score: " + str(score), True, Colors.WHITE)
        self.display.blit(text, [0, 0])