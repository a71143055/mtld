from src.mtld.simulator.robot_sim import RobotSim

def test_sim_reset_step():
    sim = RobotSim(obs_dim=8)
    obs = sim.reset()
    assert "pose" in obs and "sensors" in obs
    next_obs = sim.step([0.1]*6)
    assert next_obs["time"] > obs["time"]
