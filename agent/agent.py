import torch
import random 
import numpy as np
from collections import deque

from algo import DQN
from .nn_model import MLP
from snake_game.utils import Directions, Constants, Point

class Agent:
    def __init__(self) -> None:
        self.num_games = 0
        self.epsilon = Constants.HyperParams.EXPLORATION # controls the randomness
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=Constants.HyperParams.MAX_MEMORY) # if we exceed MAX_MEMORY it will automatically remove elements from the left using popleft()
        self.model = MLP(11, 256, 3) # TODO
        self.dqn = DQN(self.model, Constants.HyperParams.LR, self.gamma) # TODO
        pass

    def get_state(self, env):
        # define four points around the head
        head = env.snake.head
        point_top = Point(head.x, head.y - Constants.BLOCK_SIZE)
        point_right = Point(head.x + Constants.BLOCK_SIZE, head.y)
        point_bottom = Point(head.x, head.y + Constants.BLOCK_SIZE)
        point_left = Point(head.x - Constants.BLOCK_SIZE, head.y)

        # get direction as a bool
        dir_left = env.snake.direction == Directions.LEFT
        dir_right = env.snake.direction == Directions.RIGHT
        dir_up = env.snake.direction == Directions.UP
        dir_down = env.snake.direction == Directions.DOWN

        # check for potential collisions
        collision_straight = ((dir_left and env.collision_detection(point_left))
                              or
                              (dir_right and env.collision_detection(point_right))
                              or
                              (dir_down and env.collision_detection(point_bottom))
                              or 
                              (dir_up and env.collision_detection(point_top))
                            )
        
        collision_left = ((dir_left and env.collision_detection(point_bottom))
                          or
                          (dir_right and env.collision_detection(point_top))
                          or
                          (dir_up and env.collision_detection(point_left))
                          or
                          (dir_down and env.collision_detection(point_right)))
        
        collision_right = ((dir_left and env.collision_detection(point_top))
                          or
                          (dir_right and env.collision_detection(point_bottom))
                          or
                          (dir_up and env.collision_detection(point_right))
                          or
                          (dir_down and env.collision_detection(point_left)))

        # food location bools
        food_left = env.food.point.x < head.x
        food_right = env.food.point.x > head.x
        food_down = env.food.point.y > head.y
        food_up = env.food.point.y < head.y

        state = [
            collision_straight,
            collision_right,
            collision_left,
            dir_left,
            dir_right,
            dir_up,
            dir_down,
            food_left,
            food_right,
            food_up,
            food_down
        ]
        
        return np.array(state, dtype=int)
    
    def store_memory(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
        pass

    def train_long_memory(self):
        if len(self.memory) > Constants.HyperParams.BATCH_SIZE:
            mini_batch = random.sample(self.memory, Constants.HyperParams.BATCH_SIZE)
        else:
            mini_batch = self.memory
        
        states, actions, rewards, next_states, dones = zip(*mini_batch)
        self.dqn.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.dqn.train_step(state, action, reward, next_state, done)
        pass

    def get_action(self, state):
        # random moves: tradeoff exploration and exploitation
        self.epsilon = 100 - self.num_games
        action = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            action[random.randint(0, 2)] = 1
        else:
            state_torch = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state_torch)
            action[torch.argmax(prediction).item()] = 1
        
        return action
