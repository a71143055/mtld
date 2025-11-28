"""
Simple robot simulator: stateful, deterministic placeholder.
State is a dict with 'pose' (list), 'sensors' (list), and 'time'.
"""
from typing import Dict, Any, List
import numpy as np

class RobotSim:
    def __init__(self, obs_dim: int = 16):
        self.time = 0.0
        self.timestep = 0.1
        self.obs_dim = obs_dim
        self.state = {
            "pose": np.zeros(6).tolist(),   # x,y,z,roll,pitch,yaw
            "sensors": np.zeros(obs_dim).tolist()
        }

    def reset(self) -> Dict[str, Any]:
        self.time = 0.0
        self.state["pose"] = np.zeros(6).tolist()
        self.state["sensors"] = np.random.randn(self.obs_dim).tolist()
        return self._get_obs()

    def step(self, action: List[float]) -> Dict[str, Any]:
        # action: delta pose (6)
        pose = np.array(self.state["pose"])
        delta = np.array(action[:6])
        pose = pose + delta * self.timestep
        self.state["pose"] = pose.tolist()
        # update sensors deterministically from pose
        sensors = np.tanh(pose[:self.obs_dim] if self.obs_dim <= 6 else np.concatenate([pose[:6], np.zeros(self.obs_dim-6)]))
        self.state["sensors"] = sensors.tolist()
        self.time += self.timestep
        return self._get_obs()

    def _get_obs(self) -> Dict[str, Any]:
        return {
            "time": self.time,
            "pose": self.state["pose"],
            "sensors": self.state["sensors"]
        }
