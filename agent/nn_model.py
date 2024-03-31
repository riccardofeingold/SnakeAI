import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size) -> None:
        super().__init__()
        
        self.input_layer = nn.Linear(input_size, hidden_size)
        self.hidden_layer = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.input_layer(x))
        x = self.hidden_layer(x)
        return x
    
    def save(self, file_name="model.pt"):
        model_folder_path = "./model"
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)
