import pygame
from typing import Tuple

from .utils import Directions, Constants, Colors
from .objects import Snake, Food
from .ui import ScoreText

class SnakeGame:
    def __init__(self, width: int = Constants.WIDTH, height: int = Constants.HEIGHT) -> None:
        # display size
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        
        # init some useful class variables
        self.score = 0
        self.clock = pygame.time.Clock()

        # Screen Objects
        self.score_text = ScoreText(self.display)
        self.snake = Snake(start_position=(self.width/2, self.height/2), init_direction=Directions.RIGHT)
        self.food = Food()
        self.food.spawn()


        pass
    
    def collision_detection(self) -> bool:
        # collision with right end of screen
        if self.snake.head.x > self.width - Constants.BLOCK_SIZE:
            return True
        # collision with left end of screen
        elif self.snake.head.x < 0:
            return True
        # collision with bottom end of screen
        elif self.snake.head.y > self.height - Constants.BLOCK_SIZE:
            return True
        # collision with top end of screen
        elif self.snake.head.y < 0:
            return True
        # collision with itself
        elif self.snake.head in self.snake.tail[1:]:
            return True
        # no collision
        else:
            return False

    def step(self) -> Tuple[bool, float]:
        # listen to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.direction = Directions.LEFT if self.snake.direction != Directions.RIGHT else Directions.RIGHT
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = Directions.RIGHT if self.snake.direction != Directions.LEFT else Directions.LEFT
                elif event.key == pygame.K_UP:
                    self.snake.direction = Directions.UP if self.snake.direction != Directions.DOWN else Directions.DOWN
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = Directions.DOWN if self.snake.direction != Directions.UP else Directions.UP
        
        # move snake forward
        self.snake.move()
        self.snake.tail.insert(0, self.snake.head)

        # check for collision
        game_over = False
        if self.collision_detection():
            game_over = True
            return game_over, self.score
        
        # check if food has been eaten
        if self.food.point == self.snake.head:
            self.food.spawn()
            self.score += 1
        else:
            self.snake.tail.pop()

        # render screen
        self.render()

        # set frame rate
        self.clock.tick(Constants.PLAY_SPEED)

        return game_over, self.score

    def render(self):
        # make background black
        self.display.fill(Colors.BLACK)

        # draw snake, item and score text
        self.snake.draw(self.display)
        self.food.draw(self.display)
        self.score_text.draw(self.score)

        # update screen
        pygame.display.flip()
        pass