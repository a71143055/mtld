"""
Trainer: simple supervised/regression-style training loop for the MetaAgent.
This is a placeholder for meta-learning workflows; it demonstrates training,
checkpointing, and evaluation hooks without any biological content.
"""
import torch
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm
from .agent import MetaAgent
from ..utils import get_logger
import os

logger = get_logger("trainer")

class Trainer:
    def __init__(self, obs_dim=16, act_dim=6, lr=1e-3, device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = MetaAgent(obs_dim=obs_dim, act_dim=act_dim).to(self.device)
        self.opt = torch.optim.Adam(self.model.parameters(), lr=lr)
        self.criterion = torch.nn.MSELoss()

    def train(self, dataset, epochs=10, batch_size=32, ckpt_path=None):
        loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        for epoch in range(1, epochs+1):
            self.model.train()
            total_loss = 0.0
            for xb, yb in tqdm(loader, desc=f"Epoch {epoch}"):
                xb = xb.to(self.device).float()
                yb = yb.to(self.device).float()
                pred = self.model(xb)
                loss = self.criterion(pred, yb)
                self.opt.zero_grad()
                loss.backward()
                self.opt.step()
                total_loss += loss.item() * xb.size(0)
            avg_loss = total_loss / len(loader.dataset)
            logger.info(f"Epoch {epoch} avg_loss={avg_loss:.6f}")
            if ckpt_path:
                self.save_checkpoint(ckpt_path)
        return avg_loss

    def save_checkpoint(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        torch.save(self.model.state_dict(), path)
        logger.info(f"Saved checkpoint to {path}")

    def load_checkpoint(self, path):
        self.model.load_state_dict(torch.load(path, map_location=self.device))
        logger.info(f"Loaded checkpoint from {path}")
