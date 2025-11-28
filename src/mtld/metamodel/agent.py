"""
MetaAgent: a small neural network representing a policy.
Designed to be simple and easily testable.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

class MetaAgent(nn.Module):
    def __init__(self, obs_dim: int = 16, act_dim: int = 6, hidden: int = 128):
        super(MetaAgent, self).__init__()
        self.fc1 = nn.Linear(obs_dim, hidden)
        self.fc2 = nn.Linear(hidden, hidden)
        self.fc_out = nn.Linear(hidden, act_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc_out(x)
