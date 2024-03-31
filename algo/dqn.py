import torch
import torch.nn as nn
import torch.optim as optim

class DQN:
    def __init__(self, model: nn.Module, lr, gamma) -> None:
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(self.model.parameters(), self.lr)
        self.loss_func = nn.MSELoss()
        pass

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        
        if len(state.shape) == 1:
            # we want to convert (x,) to (1, x)
            state = torch.unsqueeze(state, dim=0)
            action = torch.unsqueeze(action, dim=0)
            reward = torch.unsqueeze(reward, dim=0)
            next_state = torch.unsqueeze(next_state, dim=0)
            done = (done, )

        # get predicted Q values with the current states
        Q_pred = self.model(state)

        target = Q_pred.clone()
        for index in range(len(done)):
            Q_new = reward[index]
            if not done[index]:
                Q_new = reward[index] + self.gamma * torch.max(self.model(next_state[index]))
            
            target[index][torch.argmax(action).item()] = Q_new
        
        self.optimizer.zero_grad()
        loss = self.loss_func(target, Q_pred)
        loss.backward()

        self.optimizer.step()
        pass