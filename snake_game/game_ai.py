import pygame
from typing import Tuple

from .utils import Directions, Constants, Colors
from .objects import Snake, Food
from .ui import ScoreText
from agent.rewards import collision_penalty, food_reward

class SnakeGameAI:
    def __init__(self, width: int = Constants.WIDTH, height: int = Constants.HEIGHT) -> None:
        # display size
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        
        self.score_text = ScoreText(self.display)
        self.clock = pygame.time.Clock()
        self.reset()
        pass

    def reset(self):
        # init some useful class variables
        self.score = 0
        self.iteration = 0

        # Screen Objects
        self.snake = Snake(start_position=(self.width/2, self.height/2), init_direction=Directions.RIGHT)
        self.food = Food()
        self.food.spawn()
    
    def collision_detection(self, point = None) -> bool:
        # if no specific point is given to check for collision use snake's head
        if point is None:
            point = self.snake.head
        # collision with right end of screen
        if point.x > self.width - Constants.BLOCK_SIZE:
            return True
        # collision with left end of screen
        elif point.x < 0:
            return True
        # collision with bottom end of screen
        elif point.y > self.height - Constants.BLOCK_SIZE:
            return True
        # collision with top end of screen
        elif point.y < 0:
            return True
        # collision with itself
        elif point in self.snake.tail[1:]:
            return True
        # no collision
        else:
            return False

    def step(self, action: Directions) -> Tuple[bool, float]:
        # update frame iteration 
        self.iteration += 1

        # listen to user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # move snake
        self.snake.move(action)
        self.snake.tail.insert(0, self.snake.head)

        # get reward
        reward = collision_penalty(env=self, penalty=-20) + food_reward(env=self, reward=10)
        
        # check for collision
        game_over = False
        if self.collision_detection() or self.iteration > Constants.HyperParams.EPISODE_LENGTH_SCALE * len(self.snake.tail):
            game_over = True
            return game_over, self.score, reward
        
        # check if food has been eaten
        if self.food.point == self.snake.head:
            self.food.spawn()
            self.score += 1
        else:
            self.snake.tail.pop()

        # render screen
        self.render()

        # set frame rate
        self.clock.tick(Constants.SPEED)

        return game_over, self.score, reward

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