def food_reward(env, reward: float = 10):
    if env.food.point == env.snake.head:
        return reward
    return 0

def collision_penalty(env, penalty: float = -20):
    if env.collision_detection():
        return penalty   
    return 0

def distance_to_food_penalty(env):
    return - (env.food.point.x - env.snake.head.x)**2 - (env.food.point.y - env.snake.head.y)**2
