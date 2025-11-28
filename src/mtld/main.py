"""
Entry point for mtld package.
Provides demo modes: simulation demo, training demo, and ParaView demo (if available).
"""
from .ui import run_from_cli
from .simulator.robot_sim import RobotSim
from .simulator.scaffold_model import ScaffoldModel
from .metamodel.trainer import Trainer
from .metamodel.agent import MetaAgent
from .paraview_integration import create_demo_source, create_render_pipeline, cleanup
from .utils import get_logger
import numpy as np
import torch

logger = get_logger("main")

def demo_simulation(steps=50):
    sim = RobotSim(obs_dim=16)
    obs = sim.reset()
    logger.info(f"Initial obs time={obs['time']}")
    for i in range(steps):
        # simple policy: small sinusoidal motions
        action = (np.sin(i*0.1) * 0.01) * np.ones(6)
        obs = sim.step(action.tolist())
    logger.info(f"Final pose: {obs['pose']}")
    return obs

def demo_training():
    # create synthetic dataset: map sensors -> small pose deltas
    obs_dim = 16
    act_dim = 6
    N = 1024
    X = torch.randn(N, obs_dim)
    Y = torch.randn(N, act_dim) * 0.05
    dataset = torch.utils.data.TensorDataset(X, Y)
    trainer = Trainer(obs_dim=obs_dim, act_dim=act_dim, lr=1e-3)
    trainer.train(dataset, epochs=3, batch_size=64)
    return trainer

def demo_paraview():
    src = create_demo_source()
    view, rep = create_render_pipeline(src)
    # cleanup if needed
    cleanup(src)
    return view, rep

def main():
    args = run_from_cli()
    if args.mode == "demo":
        demo_simulation(steps=args.steps)
    elif args.mode == "train":
        demo_training()
    elif args.mode == "paraview":
        demo_paraview()

if __name__ == "__main__":
    main()
