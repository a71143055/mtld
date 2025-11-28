import torch
from src.mtld.metamodel.agent import MetaAgent

def test_agent_forward():
    model = MetaAgent(obs_dim=16, act_dim=6)
    x = torch.randn(4,16)
    y = model(x)
    assert y.shape == (4,6)
