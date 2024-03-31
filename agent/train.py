import snake_game as sg
from snake_game.utils import plot
from agent import Agent

def train():
    plot_scores = []
    plot_mean_scores = []
    best_score = 0
    total_score = 0
    agent = Agent()
    game = sg.SnakeGameAI()

    while True:
        # get state
        current_state = agent.get_state(env=game)

        # get action based on current state
        action = agent.get_action(current_state)

        # run one step in game
        done, score, reward = game.step(action)

        # get new state
        next_state = agent.get_state(env=game)

        # train short memory
        agent.train_short_memory(current_state, action, reward, next_state, done)

        # store in memory
        agent.store_memory(current_state, action, reward, next_state, done)

        # experience replay
        if done:
            game.reset()
            agent.num_games += 1
            agent.train_long_memory()

            if score > best_score:
                best_score = score
                agent.model.save(file_name=f"model_{agent.num_games}.pt")
            
            print("Game: ", agent.num_games, "Score: ", score, "Best Score: ", best_score)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.num_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)
    pass

if __name__ == "__main__":
    train()