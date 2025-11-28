import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULTS = {
    "sim": {
        "timestep": 0.1,
        "max_steps": 1000
    },
    "agent": {
        "obs_dim": 16,
        "act_dim": 6,
        "lr": 1e-3
    },
    "paraview": {
        "enabled": False
    }
}
